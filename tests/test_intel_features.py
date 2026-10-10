"""Features derived from the new company intel + data-sanity filters."""
from __future__ import annotations

import json
from datetime import UTC, date, datetime, timedelta

import numpy as np
import pandas as pd
import pytest

from invest.config import FEATURE_NAMES
from invest.db import session_scope
from invest.models import (
    AnalystAction,
    Consensus,
    Holding13F,
    IntelSnapshot,
    NewsItem,
    Price,
    SecFiling,
    Stock,
)
from invest.pipeline.features import (
    SNAPSHOT_SCHEMAS,
    SNAPSHOT_VERSION,
    build_features,
    current_13f_filers,
    decode_snapshot,
    persist_feature_snapshot,
    spike_mask,
)

TODAY = date.today()
NOW = datetime.now(UTC).replace(tzinfo=None)


def _seed(t: str, close: float = 100.0, days: int = 120) -> None:
    with session_scope() as s:
        s.add(Stock(ticker=t, name=f"{t} Corp", sector="Technology", in_universe=True,
                    market_cap=1e10))
        for i in range(days):
            s.add(Price(ticker=t, date=TODAY - timedelta(days=days - i), close=close,
                        adj_close=close, volume=1e6))
        s.add(Consensus(ticker=t, as_of_date=TODAY, source="yfinance", strong_buy=8, buy=10,
                        hold=4, sell=0, strong_sell=0, mean_target=close * 1.2,
                        high_target=close * 1.5, low_target=close * 0.9, num_analysts=22))


def _intel(t: str, **over) -> None:
    payload = {
        "rec_trend": {"0m": [8, 10, 4, 0, 0], "-1m": [5, 10, 7, 0, 0], "-3m": [4, 9, 9, 0, 0]},
        "targets": {"mean": 120.0, "high": 150.0, "low": 90.0, "n": 22, "yahoo_price": 100.0},
        "eps": {"0y": {"cur": 5.5, "d30": 5.0, "up30": 9, "dn30": 1, "n": 20},
                "+1y": {"cur": 6.6, "d30": 6.0, "up30": 7, "dn30": 1, "n": 18}},
        "surprises": [{"q": (TODAY - timedelta(days=45)).isoformat(), "act": 1.2, "est": 1.0}],
        "next_earnings": (TODAY + timedelta(days=30)).isoformat(),
        "stats": {"fpe": 20.0, "short_float": 0.02, "w52_high": 105.0, "roe": 0.2,
                  "op_margin": 0.25, "de": 50.0, "w52_change": 0.3},
    }
    payload.update(over)
    with session_scope() as s:
        s.add(IntelSnapshot(ticker=t, kind="quote", as_of=NOW, payload=json.dumps(payload)))


def test_intel_features_are_computed():
    _seed("INT")
    _intel("INT")
    df = build_features(["INT"]).set_index("ticker")
    r = df.loc["INT"]
    assert r["consensus_delta"] > 0, "more buys this month than last"
    assert r["eps_revision"] == pytest.approx(np.mean([0.5 / 5.5, 0.6 / 6.6]))
    assert r["eps_revision_breadth"] == pytest.approx(np.mean([8 / 20, 6 / 18]))
    assert r["earnings_surprise"] > 0
    assert r["target_dispersion"] == pytest.approx((150 - 90) / 120)
    assert r["value"] == pytest.approx(1 / 20)
    assert r["high_52w"] == pytest.approx(100 / 105)
    assert r["short_interest"] == pytest.approx(0.02)
    assert r["next_earnings_days"] == 30


def test_firm_target_changes_and_rating_counts():
    _seed("TGT")
    with session_scope() as s:
        s.add(AnalystAction(ticker="TGT", firm="Goldman Sachs", firm_key="goldman sachs",
                            action="reiterate", target_price=140.0, prior_target=120.0,
                            target_action="raises", date=TODAY - timedelta(days=3), source="yfinance"))
        s.add(AnalystAction(ticker="TGT", firm="Tiny Shop", firm_key="tiny shop",
                            action="downgrade", target_price=90.0, prior_target=100.0,
                            target_action="lowers", date=TODAY - timedelta(days=4), source="yfinance"))
    r = build_features(["TGT"]).set_index("ticker").loc["TGT"]
    expected = (np.log(140 / 120) * 1.0 + np.log(90 / 100) * 0.25) / 1.25  # tier-weighted
    assert r["firm_target_revision"] == pytest.approx(expected)
    assert r["target_raises_30d"] == 1 and r["target_cuts_30d"] == 1
    assert r["downgrades_30d"] == 1


def test_news_sentiment_is_recency_weighted_and_shrunk():
    _seed("NEWS")
    _seed("ONE")
    with session_scope() as s:
        for i in range(6):
            s.add(NewsItem(id=f"n{i}", ticker="NEWS", published_at=NOW - timedelta(hours=6 * i),
                           title=f"good headline {i}", source="yahoo", sentiment=0.8, relevance=1.0))
        s.add(NewsItem(id="o1", ticker="ONE", published_at=NOW - timedelta(hours=1),
                       title="one good headline", source="yahoo", sentiment=0.8, relevance=1.0))
    df = build_features(["NEWS", "ONE"]).set_index("ticker")
    # Same tone, but one stray headline is pulled much harder toward neutral.
    assert 0 < df.loc["ONE", "news_sentiment"] < df.loc["NEWS", "news_sentiment"] < 0.8
    assert df.loc["NEWS", "news_count_7d"] == 6


def test_sec_features_distinguish_no_events_from_never_crawled():
    _seed("CLEAN")
    _seed("FLAG")
    _seed("UNSEEN")
    with session_scope() as s:
        for t in ("CLEAN", "FLAG"):
            s.add(IntelSnapshot(ticker=t, kind="sec", as_of=NOW, payload="{}"))
        s.add(SecFiling(ticker="FLAG", accession="0001-26-1", form="8-K",
                        filing_date=TODAY - timedelta(days=10), items="4.02,9.01"))
        s.add(SecFiling(ticker="FLAG", accession="0001-26-2", form="SC 13D",
                        filing_date=TODAY - timedelta(days=20)))
    df = build_features(["CLEAN", "FLAG", "UNSEEN"]).set_index("ticker")
    assert df.loc["CLEAN", "sec_red_flags"] == 0
    assert df.loc["FLAG", "sec_red_flags"] == 1 and df.loc["FLAG", "activist_13d"] == 1
    assert pd.isna(df.loc["UNSEEN", "sec_red_flags"]), "never crawled is NOT the same as clean"


def test_mis_scaled_target_is_discarded_not_ranked():
    """ENLV live: price 0.30, stale target 80 -> '+26,486 % upside'."""
    _seed("ENLV", close=0.30)
    with session_scope() as s:
        c = s.get(Consensus, ("ENLV", TODAY, "yfinance"))
        c.mean_target, c.high_target, c.low_target = 80.0, 80.0, 80.0
    _seed("ADR", close=100.0)
    _intel("ADR", targets={"mean": 120.0, "high": 150.0, "low": 90.0, "n": 5,
                           "yahoo_price": 2500.0})  # Yahoo quote in a different unit
    df = build_features(["ENLV", "ADR"]).set_index("ticker")
    assert bool(df.loc["ENLV", "target_suspect"]) and pd.isna(df.loc["ENLV", "upside_z"])
    assert bool(df.loc["ADR", "target_suspect"]) and pd.isna(df.loc["ADR", "upside_z"])


def test_one_day_price_spike_is_dropped():
    """APH live: 74.3 -> 143.7 -> 74.2 (a stale pre-split print)."""
    closes = np.array([74.0, 74.3, 143.7, 74.2, 74.5])
    assert list(spike_mask(closes)) == [True, True, False, True, True]
    # A genuine move that does not revert is kept.
    assert spike_mask(np.array([10.0, 10.0, 20.0, 21.0])).all()


def test_only_current_13f_filers_count():
    with session_scope() as s:
        s.add(Holding13F(filer_cik="NEW", filer_name="n", ticker="AAA", shares=1, quarter="2026Q2",
                         filing_date=TODAY))
        s.add(Holding13F(filer_cik="PREV", filer_name="p", ticker="AAA", shares=1, quarter="2026Q1",
                         filing_date=TODAY))
        s.add(Holding13F(filer_cik="STALE", filer_name="s", ticker="AAA", shares=1, quarter="2024Q3",
                         filing_date=TODAY))
    assert current_13f_filers(["AAA"]) == {"AAA": {"NEW", "PREV"}}


def test_snapshot_schema_tracks_feature_names():
    """Changing FEATURE_NAMES requires a NEW snapshot schema version, or old
    positional snapshots would be decoded into the wrong features."""
    assert SNAPSHOT_SCHEMAS[SNAPSHOT_VERSION] == (
        *FEATURE_NAMES, "last_close", "dollar_volume_20d", "vol_60d"
    )


def test_snapshot_round_trip_and_legacy_decoding():
    _seed("SNAP")
    df = build_features(["SNAP"])
    persist_feature_snapshot(df)
    from invest.models import FeatureSnapshot

    with session_scope() as s:
        js = s.get(FeatureSnapshot, ("SNAP", TODAY)).feature_json
    assert json.loads(js)["v"] == SNAPSHOT_VERSION
    d = decode_snapshot(js)
    assert d["last_close"] == pytest.approx(100.0)
    assert d["consensus_z"] == pytest.approx(float(df["consensus_z"].iloc[0]), rel=1e-4)
    legacy = decode_snapshot(json.dumps({"consensus_z": 0.4, "insider_net_buy_90d": -5e6}))
    assert legacy == {"consensus_z": 0.4}, "raw-$ legacy insider value is not comparable"
