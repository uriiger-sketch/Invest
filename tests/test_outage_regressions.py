"""Regression tests for the five-week silent outage.

The pipeline stopped persisting scores on 2026-06-04 and nobody noticed:
`min_total_sources = 50` rejected 100 % of the universe, `composite_scores`
returned empty, `rank_all` returned quietly, `cli rank` exited 0, and the
workflow stayed green while the published page served a frozen ranking with
freshly-computed coverage numbers stitched onto it.

Every test here targets one link in that chain so it cannot happen again.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from invest.config import FEATURE_NAMES, get_settings
from invest.db import session_scope
from invest.models import Consensus, Price, Stock
from invest.pipeline.rank import (
    InsufficientAnalystDataError,
    RankingProducedNothingError,
    rank_all,
)
from invest.pipeline.score import gate_survivors


def _features(n: int = 5, **overrides) -> pd.DataFrame:
    rng = np.random.default_rng(7)
    df = pd.DataFrame(
        {"ticker": [f"T{i:02d}" for i in range(n)], "dollar_volume_20d": 1e9}
    )
    for col in FEATURE_NAMES:
        df[col] = rng.normal(size=n)
    df["last_close"] = 100.0
    df["num_analysts"] = 20
    df["total_sources_count"] = get_settings().min_total_sources + 5
    df["last_price_age_days"] = 1
    df["price_history_days"] = 120
    df["consensus_z"] = 0.5
    df["upside_z"] = 0.10
    for k, v in overrides.items():
        df[k] = v
    return df


def _seed(ticker: str, *, analysts: int = 25, target_mult: float = 1.2) -> None:
    """Seed one fully-covered, gate-passing ticker.

    Includes named AnalystAction rows, not just a Consensus snapshot:
    `total_sources_count` counts distinct named contributors, so a ticker
    with consensus but no attributed firms scores 0 sources and is
    (correctly) gated out.
    """
    from invest.firms import canonical_firm_key
    from invest.sources.base import upsert_analyst_actions

    rng = np.random.default_rng(abs(hash(ticker)) % 2**32)
    with session_scope() as s:
        if not s.get(Stock, ticker):
            s.add(Stock(ticker=ticker, name=f"{ticker} Inc", sector="Technology", in_universe=True))
        price = 100.0
        for i in range(120):
            price *= 1 + float(rng.normal(0.001, 0.01))
            s.add(
                Price(ticker=ticker, date=date.today() - timedelta(days=120 - i),
                      close=price, adj_close=price, volume=5_000_000)
            )
        s.add(
            Consensus(ticker=ticker, as_of_date=date.today(), source="yfinance",
                      strong_buy=analysts - 6, buy=4, hold=2, sell=0, strong_sell=0,
                      mean_target=price * target_mult, high_target=price * 1.5,
                      low_target=price, num_analysts=analysts)
        )

    # Enough distinct named firms to clear the coverage floor.
    n_firms = get_settings().min_total_sources + 4
    upsert_analyst_actions([
        {
            "ticker": ticker, "firm": f"Firm{j:02d}",
            "firm_key": canonical_firm_key(f"Firm{j:02d}"),
            "analyst": None, "action": "upgrade", "from_grade": "Hold",
            "to_grade": "Buy", "target_price": 150.0,
            "date": date.today() - timedelta(days=j % 60), "source": "yfinance",
        }
        for j in range(n_firms)
    ])


def test_gate_survivors_pinpoints_the_culprit_gate():
    """When a gate wipes out the universe, the diagnostics must name it.

    The original failure logged a generic warning that blamed the *liquidity*
    gate while the coverage gate was the real culprit — which is a large part
    of why it went unnoticed for five weeks.
    """
    df = _features(5, total_sources_count=0)  # coverage gate rejects everything
    counts = gate_survivors(df)
    assert counts["universe"] == 5
    assert counts["combined"] == 0
    assert counts["outlook.total_sources"] == 0, "the guilty gate must report 0 survivors"
    assert counts["liquidity"] == 5, "innocent gates must not be blamed"


def test_rank_all_raises_when_every_ticker_is_gated_out(monkeypatch):
    """A total wipeout must fail LOUDLY, not return an empty frame quietly."""
    import invest.pipeline.score as score_mod

    for t in ("AAA", "BBB", "CCC"):
        _seed(t)

    # Make the coverage gate unsatisfiable, exactly as min_total_sources=50 did.
    real = score_mod.get_settings()

    class _Unsatisfiable:
        def __getattr__(self, name):
            if name == "min_total_sources":
                return 10_000
            return getattr(real, name)

    # monkeypatch restores the original automatically, so the patch cannot
    # leak into other tests.
    monkeypatch.setattr(score_mod, "get_settings", lambda: _Unsatisfiable())

    with pytest.raises(RankingProducedNothingError) as excinfo:
        rank_all(["AAA", "BBB", "CCC"])
    # The error must carry the per-gate breakdown so the cause is obvious.
    assert "total_sources" in str(excinfo.value)


def test_rank_all_refuses_to_rank_without_analyst_data():
    """If the DB was wiped, ranking on nothing must fail rather than publish noise."""
    with session_scope() as s:
        for t in ("EMP1", "EMP2"):
            s.add(Stock(ticker=t, name=t, sector="Technology", in_universe=True))
            price = 100.0
            for i in range(120):
                price *= 1.001
                s.add(Price(ticker=t, date=date.today() - timedelta(days=120 - i),
                            close=price, adj_close=price, volume=5_000_000))
    with pytest.raises(InsufficientAnalystDataError):
        rank_all(["EMP1", "EMP2"])


def test_successful_rank_persists_scores():
    """The happy path must actually write Score rows — the thing that silently
    stopped happening for five weeks."""
    from invest.models import Score

    tickers = [f"OK{i}" for i in range(6)]
    for t in tickers:
        _seed(t)
    df = rank_all(tickers)
    assert not df.empty
    with session_scope() as s:
        persisted = s.query(Score).filter(Score.as_of == date.today()).count()
    assert persisted > 0, "rank_all must persist Score rows for today"


def test_coverage_counts_covering_analysts_not_just_named_changers():
    """A ticker with consensus but NO rating-change history is still covered.

    This is the cold-database failure: `total_sources_count` counted only
    firms appearing in the 90-day upgrade/downgrade feed, so a database
    restored from empty reported 0 sources for all 301 tickers even though
    consensus showed 30-50 analysts covering them. The coverage gate then
    rejected the entire universe and `rank` produced nothing.

    A stock followed by 25 analysts is well covered whether or not any of
    them happened to change their rating this quarter.
    """
    from invest.pipeline.features import build_features

    price = 100.0
    with session_scope() as s:
        s.add(Stock(ticker="COLD", name="Cold Start Inc", sector="Technology",
                    in_universe=True))
        for i in range(120):
            s.add(Price(ticker="COLD", date=date.today() - timedelta(days=120 - i),
                        close=price, adj_close=price, volume=5_000_000))
        s.add(Consensus(ticker="COLD", as_of_date=date.today(), source="yfinance",
                        strong_buy=15, buy=6, hold=4, sell=0, strong_sell=0,
                        mean_target=price * 1.2, high_target=price * 1.5,
                        low_target=price, num_analysts=25))
    # Deliberately NO AnalystAction rows — this is a freshly-seeded database.

    df = build_features(["COLD"]).set_index("ticker")
    assert df.loc["COLD", "named_firm_sources"] == 0
    assert df.loc["COLD", "total_sources_count"] == 25, (
        "25 covering analysts must count as 25 sources even with no rating "
        "changes on file"
    )
    assert df.loc["COLD", "total_sources_count"] >= get_settings().min_total_sources


def test_sell_side_sources_are_not_double_counted():
    """Named rating-changers are a SUBSET of covering analysts, so the
    sell-side bucket takes their max — never their sum. Summing would inflate
    a 25-analyst name to 40 sources and let thin coverage look deep."""
    from invest.pipeline.features import build_features

    _seed("DEDUP", analysts=25)  # 25 covering analysts + min_total_sources+4 named firms
    df = build_features(["DEDUP"]).set_index("ticker")
    named = int(df.loc["DEDUP", "named_firm_sources"])
    assert named > 0, "fixture should have seeded named firms"
    assert df.loc["DEDUP", "sell_side_sources"] == max(25, named)
    assert df.loc["DEDUP", "total_sources_count"] == max(25, named), (
        "no 13F/insider rows seeded, so total must equal the sell-side bucket"
    )


def _load_report_module():
    """Import scripts/generate_report.py, which is a script, not a package."""
    import importlib.util
    from pathlib import Path

    path = Path(__file__).resolve().parent.parent / "scripts" / "generate_report.py"
    spec = importlib.util.spec_from_file_location("generate_report", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_report_source_count_matches_the_gate():
    """The Sources column must be computed the same way as the gate.

    They diverged once: the report counted only named rating-changers while
    ranking used a different definition, so picks that had supposedly cleared
    a 12-source floor were displayed with `Sources = 0`. Any reader comparing
    the two sees a contradiction, and there is no way to tell which number is
    lying without reading the code.
    """
    from invest.pipeline.features import build_features

    _seed("MATCH", analysts=25)
    # A ticker with consensus only — no named firms at all.
    price = 100.0
    with session_scope() as s:
        s.add(Stock(ticker="BARE", name="Bare Inc", sector="Technology", in_universe=True))
        for i in range(120):
            s.add(Price(ticker="BARE", date=date.today() - timedelta(days=120 - i),
                        close=price, adj_close=price, volume=5_000_000))
        s.add(Consensus(ticker="BARE", as_of_date=date.today(), source="yfinance",
                        strong_buy=12, buy=5, hold=3, sell=0, strong_sell=0,
                        mean_target=price * 1.2, high_target=price * 1.4,
                        low_target=price, num_analysts=20))

    tickers = ["MATCH", "BARE"]
    feats = build_features(tickers).set_index("ticker")
    report_counts = _load_report_module()._total_sources_per_ticker(tickers)
    for t in tickers:
        assert report_counts[t] == int(feats.loc[t, "total_sources_count"]), (
            f"{t}: report shows {report_counts[t]} sources but the gate used "
            f"{int(feats.loc[t, 'total_sources_count'])}"
        )
    assert report_counts["BARE"] == 20, "consensus-only coverage must still count"


def test_report_enrichment_skips_null_close_rows():
    """Live-observed: PRX.AS's most recent Price row had a real date but a
    NULL close (a yfinance data gap on a European ADR). The report's "latest
    price" lookup had no filter for this, so it displayed "—" for Price and
    Upside on a stock that had a perfectly good score, target and gate-
    passing history — just because its single most recent price row
    happened to be a data gap."""
    with session_scope() as s:
        s.add(Stock(ticker="GAPPY", name="Gappy Inc", sector="Technology", in_universe=True))
        s.add(Price(ticker="GAPPY", date=date.today() - timedelta(days=1),
                    close=50.0, adj_close=50.0, volume=1_000_000))
        # Most recent row: real date, no close.
        s.add(Price(ticker="GAPPY", date=date.today(), close=None, adj_close=None,
                    volume=None))
        s.add(Consensus(ticker="GAPPY", as_of_date=date.today(), source="yfinance",
                        strong_buy=10, buy=5, hold=2, sell=0, strong_sell=0,
                        mean_target=60.0, high_target=70.0, low_target=55.0,
                        num_analysts=17))

    extras = _load_report_module()._enrichment_for(["GAPPY"])
    assert extras["GAPPY"].get("last_close") == 50.0, (
        "must fall back to the last GOOD close, not None/NaN from the gap row"
    )
    assert extras["GAPPY"].get("upside_pct") is not None


def test_coverage_sweep_is_not_capped_below_the_universe():
    """The hourly sweep must be able to reach every ticker.

    A fixed 60-ticker cap left a restored-from-empty database with analyst
    coverage for only 20 % of a 301-name universe — far too thin for anything
    to clear the coverage gate. The wall-clock budget is the safety valve now,
    not an arbitrary count.
    """
    from invest.pipeline.ingest import stalest_tickers

    settings = get_settings()
    assert settings.coverage_sweep_max == 0, "0 means no cap — sweep the whole universe"
    assert settings.coverage_budget_seconds > 0, "an unbounded sweep can blow the job timeout"

    universe = [f"U{i:03d}" for i in range(301)]
    with session_scope() as s:
        for t in universe:
            s.add(Stock(ticker=t, name=t, sector="Technology", in_universe=True))
    picked = stalest_tickers(universe, settings.coverage_sweep_max or len(universe))
    assert len(picked) == len(universe)


def test_last_close_survives_feature_merge():
    """`price_df` and `cons` both carry last_close; an unsuffixed merge used to
    yield last_close_x/_y and leave last_close as NaN for EVERY ticker,
    poisoning the persisted snapshots and the ML training set."""
    from invest.pipeline.features import build_features

    _seed("LCLOSE")
    df = build_features(["LCLOSE"]).set_index("ticker")
    assert "last_close" in df.columns
    assert pd.notna(df.loc["LCLOSE", "last_close"]), "last_close must not be NaN"
    assert df.loc["LCLOSE", "last_close"] > 0
    assert not [c for c in df.columns if c.endswith(("_x", "_y"))], "merge collision"


def test_13f_ingest_is_idempotent():
    """`session.merge()` on an autoincrement PK INSERTs rather than updates,
    so the second deep run each quarter raised IntegrityError and aborted
    BOTH 13F and insider ingest — the main reason Insts was 0 everywhere."""
    from invest.models import Holding13F
    from invest.sources.edgar_src import EdgarSource

    batch = [
        {
            "filer_cik": "0001067983", "filer_name": "Berkshire Hathaway",
            "ticker": "AAPL", "shares": 1000.0, "value_usd": 1e6,
            "quarter": "2026Q3", "filing_date": date.today(),
        }
    ]
    with session_scope() as s:
        s.add(Stock(ticker="AAPL", name="Apple Inc.", sector="Technology", in_universe=True))

    EdgarSource._upsert_holdings(batch)
    # Same quarter, refreshed numbers — must UPDATE, never duplicate or raise.
    batch[0]["shares"] = 2000.0
    EdgarSource._upsert_holdings(batch)

    with session_scope() as s:
        rows = s.query(Holding13F).filter(Holding13F.ticker == "AAPL").all()
    assert len(rows) == 1, "re-ingesting the same quarter must not duplicate"
    assert rows[0].shares == 2000.0, "re-ingest must refresh the position"


def test_cusip_matching_beats_name_matching():
    """AMZN could NEVER match by name ("Amazon.com, Inc." normalises to
    'amazoncom' but the 13F name "AMAZON COM INC" gives 'amazon com'), so
    holdings were silently dropped. CUSIP is the authoritative key."""
    from invest.sources.edgar_src import EdgarSource

    with session_scope() as s:
        s.add(Stock(ticker="AMZN", name="Amazon.com, Inc.", sector="Consumer Cyclical",
                    cusip="023135106", in_universe=True))

    src = EdgarSource()
    name_lookup = src._build_name_to_ticker(["AMZN"])
    cusip_lookup = src._build_cusip_to_ticker(["AMZN"])

    # The historical failure: the 13F spelling does not match by name.
    assert src._issuer_to_ticker("AMAZON COM INC", name_lookup) is None
    # CUSIP resolves it, both full and issuer-prefix forms.
    assert src._cusip_to_ticker("023135106", cusip_lookup) == "AMZN"
    assert src._cusip_to_ticker("023135", cusip_lookup) == "AMZN"


def test_stalest_tickers_orders_by_consensus_age():
    """The hourly rolling refresh must pick the STALEST tickers so the whole
    universe cycles instead of re-fetching the same names forever."""
    from invest.pipeline.ingest import stalest_tickers

    today = date.today()
    with session_scope() as s:
        for t, age in (("FRESH", 0), ("MID", 5), ("OLD", 30)):
            s.add(Stock(ticker=t, name=t, sector="Technology", in_universe=True))
            s.add(Consensus(ticker=t, as_of_date=today - timedelta(days=age),
                            source="yfinance", strong_buy=10, buy=5, hold=1,
                            sell=0, strong_sell=0, mean_target=120.0,
                            high_target=130.0, low_target=110.0, num_analysts=16))
        s.add(Stock(ticker="NEVER", name="NEVER", sector="Technology", in_universe=True))

    picks = stalest_tickers(["FRESH", "MID", "OLD", "NEVER"], limit=3)
    # Never-fetched first, then oldest-first. FRESH must be last to be picked.
    assert picks[0] == "NEVER"
    assert picks[1] == "OLD"
    assert "FRESH" not in picks


def test_main_table_capped_to_configured_size():
    """The merged main table unions each horizon's own top-N diversified
    picks, so its row count is however many DISTINCT tickers that union
    happens to produce — observed 27 on one live run, not a fixed number.
    `main_table_size` caps the FINAL table regardless of how much the four
    horizon lists overlap."""
    from invest.pipeline.rank import HORIZONS

    report = _load_report_module()
    settings = get_settings()
    # 30 distinct tickers per horizon, all identical across horizons, so the
    # union is exactly 30 — comfortably above main_table_size (25).
    by_h = {
        h: [
            {
                "ticker": f"T{i:02d}", "name": f"T{i:02d} Inc", "sector": "Technology",
                "upside_pct": 0.10, "last_close": 100.0, "mean_target": 110.0,
                "analysts": 20, "percentile": 1.0 - i / 30, "rank": i + 1,
            }
            for i in range(30)
        ]
        for h in HORIZONS
    }
    rows = report.main_table_rows(by_h)
    assert len(rows) == settings.main_table_size == 25
    # Best-scoring tickers (lowest i, highest percentile) must survive the cap.
    assert {r["ticker"] for r in rows} == {f"T{i:02d}" for i in range(25)}
