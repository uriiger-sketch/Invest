from __future__ import annotations

from datetime import date, timedelta

import numpy as np

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
