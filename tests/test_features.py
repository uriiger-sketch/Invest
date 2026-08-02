from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pytest

from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Price, Stock
from invest.pipeline.features import build_features


def _seed_prices(ticker: str, days: int = 120) -> None:
    today = date.today()
    rng = np.random.default_rng(ord(ticker[-1]))
    with session_scope() as s:
        s.add(Stock(ticker=ticker, name=ticker, sector="Tech", in_universe=True))
        price = 100.0
        for i in range(days):
            d = today - timedelta(days=days - i)
            price *= 1 + float(rng.normal(0, 0.01))
            s.add(
                Price(
                    ticker=ticker,
                    date=d,
                    close=price,
                    adj_close=price,
                    volume=1_000_000,
                )
            )


def test_build_features_emits_one_row_per_ticker_with_zero_fill():
    _seed_prices("AAA")
    _seed_prices("BBB")
    df = build_features(["AAA", "BBB"])
    assert len(df) == 2
    # Every feature column must exist and be numeric.
    for col in ("consensus_z", "upside_z", "rating_mom_7d", "risk_penalty", "price_mom_21d"):
        assert col in df.columns
        assert df[col].notna().all()
    # Volatility should be positive magnitude -> risk_penalty negative.
    assert (df["risk_penalty"] <= 0).all()


def test_build_features_picks_up_consensus_and_actions():
    _seed_prices("AAA")
    today = date.today()
    with session_scope() as s:
        s.add(
            Consensus(
                ticker="AAA",
                as_of_date=today,
                source="yfinance",
                strong_buy=10,
                buy=5,
                hold=2,
                sell=0,
                strong_sell=0,
                mean_target=150.0,
                high_target=170.0,
                low_target=140.0,
                num_analysts=17,
            )
        )
        s.add(
            AnalystAction(
                ticker="AAA",
                firm="Goldman Sachs",
                action="upgrade",
                from_grade="Hold",
                to_grade="Buy",
                date=today - timedelta(days=3),
                source="yfinance",
            )
        )

    df = build_features(["AAA"])
    row = df.iloc[0]
    assert row["consensus_z"] > 0
    # Most recent close in seeded path is near 100-110; target 150 gives positive upside.
    assert row["upside_z"] > 0
    assert row["rating_mom_7d"] >= 1


def test_consensus_shrinkage_prefers_broad_coverage():
    """A 3-analyst unanimous buy must NOT outrank a 30-analyst 80 % buy.

    Shrinkage multiplies raw consensus by n/(n+k): with k=10 the tiny
    unanimous name lands ≈ 0.35, the broadly-covered one ≈ 0.53.
    """
    _seed_prices("TINY")
    _seed_prices("BROAD")
    today = date.today()
    with session_scope() as s:
        s.add(Consensus(ticker="TINY", as_of_date=today, source="yfinance",
                        strong_buy=3, buy=0, hold=0, sell=0, strong_sell=0,
                        mean_target=150.0, high_target=160.0, low_target=140.0,
                        num_analysts=3))
        s.add(Consensus(ticker="BROAD", as_of_date=today, source="yfinance",
                        strong_buy=12, buy=12, hold=6, sell=0, strong_sell=0,
                        mean_target=150.0, high_target=170.0, low_target=130.0,
                        num_analysts=30))
    df = build_features(["TINY", "BROAD"]).set_index("ticker")
    assert df.loc["BROAD", "consensus_z"] > df.loc["TINY", "consensus_z"]


def test_cross_source_median_target():
    """mean_target is the MEDIAN across sources' latest rows, so one broken
    aggregator can't skew the upside."""
    _seed_prices("MED")
    today = date.today()
    with session_scope() as s:
        for src, tgt in [("yfinance", 120.0), ("finnhub", 122.0), ("fmp", 500.0)]:
            s.add(Consensus(ticker="MED", as_of_date=today, source=src,
                            strong_buy=10, buy=10, hold=5, sell=0, strong_sell=0,
                            mean_target=tgt, high_target=tgt * 1.1, low_target=tgt * 0.9,
                            num_analysts=25))
    from invest.pipeline.features import _latest_consensus

    cons = _latest_consensus(["MED"]).set_index("ticker")
    # median(120, 122, 500) = 122 — the broken 500 target is ignored.
    assert cons.loc["MED", "mean_target"] == 122.0


def test_momentum_windows_are_distinct_and_off_by_one_fixed():
    """price_mom_5d / price_mom_21d / price_mom_63d must each reflect their
    OWN window, not all collapse to the same number, and a ticker with
    EXACTLY 22 closes must get a real price_mom_21d (previously `> 22`
    zeroed out tickers with exactly 22, off by one).

    With 64 closes (index 0..63), the code reads index 0 for the 63d
    window, 42 for the 21d window, and 58 for the 5d window, all against
    today's close at index 63. Setting distinct step levels at exactly
    those checkpoints makes each window's expected value exact and
    unambiguous: most of the total move happened long ago, so the windows
    must come out strictly decreasing as they shorten.
    """
    from invest.models import Price

    today = date.today()
    prices = [50.0] * 42 + [180.0] * 16 + [195.0] * 5 + [200.0]
    assert len(prices) == 64
    with session_scope() as s:
        s.add(Stock(ticker="MOM", name="MOM", sector="Tech", in_universe=True))
        for i, price in enumerate(prices):
            s.add(Price(ticker="MOM", date=today - timedelta(days=64 - i),
                        close=price, adj_close=price, volume=1_000_000))
    df = build_features(["MOM"]).set_index("ticker")
    mom_5, mom_21, mom_63 = (
        df.loc["MOM", "price_mom_5d"], df.loc["MOM", "price_mom_21d"], df.loc["MOM", "price_mom_63d"]
    )
    assert mom_63 == pytest.approx(200.0 / 50.0 - 1)
    assert mom_21 == pytest.approx(200.0 / 180.0 - 1)
    assert mom_5 == pytest.approx(200.0 / 195.0 - 1)
    assert mom_63 > mom_21 > mom_5 >= 0

    # Off-by-one: exactly 22 closes must still yield a nonzero 21d momentum.
    with session_scope() as s:
        s.add(Stock(ticker="EXACT22", name="EXACT22", sector="Tech", in_universe=True))
        for i in range(22):
            price = 100.0 * (1.5 if i == 21 else 1.0)
            s.add(Price(ticker="EXACT22", date=today - timedelta(days=22 - i),
                        close=price, adj_close=price, volume=1_000_000))
    df2 = build_features(["EXACT22"]).set_index("ticker")
    assert df2.loc["EXACT22", "price_mom_21d"] != 0.0


def test_inst_flow_ignores_non_adjacent_quarters_and_new_positions():
    """The old implementation diffed consecutive STORED rows regardless of
    how many real quarters apart they were, and regardless of whether the
    filer even held a position before — comparing "1 filer's holding" one
    quarter to "28 filers' aggregate" the next produced changes over
    +200,000 %. The fix only accepts a same-filer, adjacent-quarter,
    nonzero-prior-position comparison."""
    from invest.models import Holding13F
    from invest.pipeline.features import _inst_flow

    with session_scope() as s:
        # FILER1: real adjacent-quarter growth 1000 -> 1200 shares (+20%).
        s.add(Holding13F(filer_cik="C1", filer_name="Filer One", ticker="FLOW",
                        shares=1000.0, value_usd=1e6, quarter="2026Q1",
                        filing_date=date.today()))
        s.add(Holding13F(filer_cik="C1", filer_name="Filer One", ticker="FLOW",
                        shares=1200.0, value_usd=1.2e6, quarter="2026Q2",
                        filing_date=date.today()))
        # FILER2: a stale one-off quarter from 2024 with a totally different
        # (much larger) position, then nothing until 2026Q2 — NOT adjacent,
        # must not be compared.
        s.add(Holding13F(filer_cik="C2", filer_name="Filer Two", ticker="FLOW",
                        shares=1.0, value_usd=1.0, quarter="2024Q1",
                        filing_date=date.today()))
        s.add(Holding13F(filer_cik="C2", filer_name="Filer Two", ticker="FLOW",
                        shares=50000.0, value_usd=5e7, quarter="2026Q2",
                        filing_date=date.today()))
        # FILER3: brand-new position this quarter (no prior holding at all)
        # — a 0 -> N move is undefined/infinite, must be excluded.
        s.add(Holding13F(filer_cik="C3", filer_name="Filer Three", ticker="FLOW",
                        shares=9999.0, value_usd=1e6, quarter="2026Q2",
                        filing_date=date.today()))

    out = _inst_flow(["FLOW"]).set_index("ticker")
    # Only FILER1's valid +20% comparison should survive.
    assert abs(out.loc["FLOW", "inst_flow_13f"] - 0.20) < 1e-9


def test_insider_unknown_action_codes_are_neutral_not_bearish():
    """Any action string other than exactly "buy"/"sell" (e.g. the coarse
    "activity" placeholder for unparsed filings) must contribute ZERO to
    insider_net_buy_90d, not be miscoded as a sell."""
    from invest.models import InsiderTrade

    with session_scope() as s:
        s.add(InsiderTrade(ticker="INSTEST", filer="(aggregated form-4 activity)",
                            action="activity", shares=None, price=None, date=date.today()))
        s.add(InsiderTrade(ticker="INSTEST", filer="JANE DOE",
                            action="buy", shares=100.0, price=50.0, date=date.today()))
    _seed_prices("INSTEST")
    df = build_features(["INSTEST"]).set_index("ticker")
    # Only the real $5,000 buy should register; the "activity" row is inert.
    assert df.loc["INSTEST", "insider_net_buy_90d"] == 5000.0


def test_historic_consensus_uses_cross_source_median():
    """`_historic_consensus` must aggregate the SAME way `_latest_consensus`
    does (cross-source median), or `target_revision_30d` compares
    apples to a non-deterministic tie-broken oranges the moment more than
    one source is enabled."""
    from invest.pipeline.features import _historic_consensus

    old_date = date.today() - timedelta(days=40)
    with session_scope() as s:
        for src, tgt in [("yfinance", 100.0), ("finnhub", 104.0), ("fmp", 999.0)]:
            s.add(Consensus(ticker="HIST", as_of_date=old_date, source=src,
                            strong_buy=10, buy=5, hold=2, sell=0, strong_sell=0,
                            mean_target=tgt, high_target=tgt * 1.1, low_target=tgt * 0.9,
                            num_analysts=17))
    out = _historic_consensus(["HIST"], days_ago=30).set_index("ticker")
    # median(100, 104, 999) = 104 — the broken 999 outlier is ignored.
    assert out.loc["HIST", "mean_target"] == 104.0
