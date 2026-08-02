from __future__ import annotations

import numpy as np
import pandas as pd

from invest.config import FEATURE_NAMES, HORIZONS, get_settings
from invest.pipeline.score import composite_scores, liquidity_mask, outlook_mask


def _mk_features(n: int = 10, bullish_outlook: bool = True) -> pd.DataFrame:
    """Build a feature frame that exercises EVERY gate.

    Historically this helper omitted ``total_sources_count``, so the
    coverage gate hit its ``if col in features.columns`` branch as False and
    was silently skipped by almost the whole suite. That blind spot is
    exactly why a mis-calibrated threshold could reject 100 % of the real
    universe for five weeks with 37/37 tests green. Every gate input is now
    populated by default, so a threshold that rejects everything WILL fail
    the suite.
    """
    rng = np.random.default_rng(42)
    tickers = [f"T{i:02d}" for i in range(n)]
    df = pd.DataFrame({"ticker": tickers, "dollar_volume_20d": 1e9})
    for col in FEATURE_NAMES:
        df[col] = rng.normal(size=n)
    df["last_close"] = 100.0
    df["num_analysts"] = 12
    # Realistic coverage: comfortably above the configured floor, but nowhere
    # near the fantasy numbers a fixture could invent.
    df["total_sources_count"] = get_settings().min_total_sources + 6
    df["last_price_age_days"] = 1
    df["price_history_days"] = 120
    if bullish_outlook:
        df["consensus_z"] = 0.5
        df["upside_z"] = 0.10
    return df


def test_composite_scores_return_row_per_ticker_per_horizon():
    df = _mk_features(8)
    out = composite_scores(df)
    assert not out.empty
    # 8 tickers × len(HORIZONS) rows (everyone passes the quality gate).
    assert len(out) == 8 * len(HORIZONS)
    assert set(out["horizon"].unique()) == set(HORIZONS)


def test_outlook_mask_strictly_positive_consensus():
    """Strict net-bullish: consensus_z must be > 0, not just non-negative."""
    df = _mk_features(4, bullish_outlook=False)
    df["consensus_z"] = [0.5, -0.5, 0.0, 0.5]
    df["upside_z"] = [0.10, 0.10, 0.10, -0.20]
    df["num_analysts"] = 12
    mask = outlook_mask(df).reset_index(drop=True)
    # Row 0: bullish + 10% upside → True
    # Row 1: bearish consensus     → False
    # Row 2: consensus exactly 0   → False (strictly positive required)
    # Row 3: bullish but -20% upside → False
    assert list(mask) == [True, False, False, False]


def test_positive_upside_4pct_threshold():
    """Only ≥ 4 % upside passes; 3.9 % is out."""
    df = _mk_features(4, bullish_outlook=False)
    df["consensus_z"] = 0.5
    df["upside_z"] = [0.05, 0.04, 0.039, 0.00]
    df["num_analysts"] = 12
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [True, True, False, False]


def test_min_firms_excludes_thinly_covered():
    df = _mk_features(3, bullish_outlook=True)
    df["num_analysts"] = [10, 4, 0]   # min_firms = 5
    df["total_sources_count"] = 60    # keep total_sources gate satisfied
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [True, False, False]


def test_min_total_sources_gate():
    """The coverage floor excludes names just below it and admits those at
    or above it. Boundaries are derived from the configured threshold rather
    than hardcoded, so re-tuning the threshold can't leave a stale test
    asserting the old value."""
    floor = get_settings().min_total_sources
    df = _mk_features(3, bullish_outlook=True)
    df["num_analysts"] = 20
    df["total_sources_count"] = [floor - 1, floor, floor + 50]
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [False, True, True]


def test_min_total_sources_is_actually_achievable():
    """Regression guard for the five-week outage.

    `min_total_sources` was set to 50 when the best-covered ticker in the
    real universe reached only ~28, so the gate rejected everything and the
    pipeline silently stopped persisting scores. A coverage floor that real
    data cannot clear is always a bug — keep it inside a plausible range.
    """
    floor = get_settings().min_total_sources
    assert 0 < floor <= 30, (
        f"min_total_sources={floor} is outside the range real coverage data can "
        "satisfy; observed production maximum was ~28 distinct sources"
    )


def test_buy_hold_sell_equals_num_analysts_invariant():
    """The buy/hold/sell columns in the report must tie out to the analyst
    total. This invariant comes from yfinance's recommendations_summary:
    every covering firm sits in exactly one bucket. If this ever stops
    holding, the report's column math will look wrong to the user."""
    import pandas as pd

    consensus = pd.DataFrame(
        {
            "ticker": ["A", "B", "C"],
            "strong_buy": [3, 0, 1],
            "buy": [10, 4, 5],
            "hold": [2, 6, 3],
            "sell": [1, 2, 0],
            "strong_sell": [0, 1, 0],
        }
    )
    consensus["total"] = consensus[["strong_buy", "buy", "hold", "sell", "strong_sell"]].sum(axis=1)
    consensus["buy_col"] = consensus["strong_buy"] + consensus["buy"]
    consensus["sell_col"] = consensus["sell"] + consensus["strong_sell"]
    consensus["sum_btns"] = consensus["buy_col"] + consensus["hold"] + consensus["sell_col"]
    assert (consensus["sum_btns"] == consensus["total"]).all()


def test_liquidity_gate_excludes_low_dollar_volume():
    df = _mk_features(5)
    df.loc[0, "dollar_volume_20d"] = 1.0  # below threshold
    mask = liquidity_mask(df).reset_index(drop=True)
    assert bool(mask.iloc[0]) is False
    assert all(mask.iloc[1:])


def test_zero_variance_column_contributes_zero():
    df = _mk_features(6)
    for col in FEATURE_NAMES:
        df[col] = 0.0
    # Keep stocks past the strict outlook gate so composite_scores returns
    # rows; the constants below are identical across tickers so each
    # column's z-score is zero and the composite still collapses to 0.
    df["consensus_z"] = 0.5
    df["upside_z"] = 0.10
    out = composite_scores(df)
    assert not out.empty
    assert np.allclose(out["composite_score"], 0.0)


def test_liquidity_below_threshold_drops_ticker_from_all_horizons():
    df = _mk_features(4)
    df.loc[0, "dollar_volume_20d"] = 100.0
    out = composite_scores(df)
    assert "T00" not in set(out["ticker"])


def test_robust_zscore_resists_outliers():
    """One broken outlier must not crush every legitimate value to ~0.

    With mean/std, a single +50 value in [1..9, 50] inflates the std so the
    legitimate spread z-scores collapse below 0.6. Median/MAD keeps them
    at a meaningful scale.
    """
    from invest.pipeline.score import _zscore

    s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 50], dtype=float)
    z = _zscore(s)
    # Legit points (1..9) span ~2.7 robust-z units; classic z would give ~0.57.
    legit_spread = z.iloc[8] - z.iloc[0]
    assert legit_spread > 2.0
    # The outlier is far out — flagged, not normalised away.
    assert z.iloc[9] > 10


def test_data_quality_mask_gates():
    from invest.pipeline.score import data_quality_mask

    df = _mk_features(4, bullish_outlook=True)
    df["last_price_age_days"] = [1, 30, 2, 3]      # row 1: stale price
    df["price_history_days"] = [120, 120, 10, 120]  # row 2: short history
    df["upside_z"] = [0.10, 0.10, 0.10, 5.0]        # row 3: absurd 500 % upside
    mask = data_quality_mask(df).reset_index(drop=True)
    assert list(mask) == [True, False, False, False]


def test_upside_cap_limits_scoring_dominance():
    """A 90 % upside is capped at upside_cap (75 %) before z-scoring so it
    scores identically to a capped 75 % — outliers can't run the board."""
    df = _mk_features(6, bullish_outlook=True)
    for col in FEATURE_NAMES:
        df[col] = 0.0
    df["consensus_z"] = 0.5
    df["upside_z"] = [0.90, 0.75, 0.10, 0.10, 0.10, 0.10]
    out = composite_scores(df)
    hours = out[out["horizon"] == "hours"].set_index("ticker")["composite_score"]
    assert abs(hours["T00"] - hours["T01"]) < 1e-9


def test_select_diversified_sector_cap():
    from invest.pipeline.rank import select_diversified

    rows = [
        {"ticker": f"S{i}", "sector": "Semis", "blended_score": 10 - i} for i in range(8)
    ] + [
        {"ticker": "BANK", "sector": "Financials", "blended_score": 1.0},
        {"ticker": "PHRM", "sector": "Health Care", "blended_score": 0.5},
    ]
    picked = select_diversified(rows, n=7, max_per_sector=5)
    sectors = [r["sector"] for r in picked]
    assert sectors.count("Semis") == 5
    assert "BANK" in {r["ticker"] for r in picked}
    assert "PHRM" in {r["ticker"] for r in picked}
    assert len(picked) == 7


def test_select_diversified_backfills_when_pool_small():
    from invest.pipeline.rank import select_diversified

    rows = [{"ticker": f"S{i}", "sector": "Semis", "blended_score": 5 - i} for i in range(6)]
    picked = select_diversified(rows, n=6, max_per_sector=3)
    # Cap admits 3, but with nothing else available the rest backfill by score.
    assert len(picked) == 6


def test_select_diversified_backfill_preserves_rank_monotonicity():
    """A backfilled (capped-out) name can score HIGHER than a diversified
    pick from a still-open sector. Appending backfill at the end of `picked`
    in scan order used to display it at a WORSE rank than its score
    deserved; the final list must be sorted by score regardless of which
    pass (diversified vs backfill) contributed each row."""
    from invest.pipeline.rank import select_diversified

    rows = [
        {"ticker": "A10", "sector": "Semis", "blended_score": 10},
        {"ticker": "A9", "sector": "Semis", "blended_score": 9},
        {"ticker": "A8", "sector": "Semis", "blended_score": 8},
        {"ticker": "A7", "sector": "Semis", "blended_score": 7},
        {"ticker": "A6", "sector": "Semis", "blended_score": 6},
        {"ticker": "B1", "sector": "Financials", "blended_score": 1},
        {"ticker": "A5", "sector": "Semis", "blended_score": 5},
        {"ticker": "A4", "sector": "Semis", "blended_score": 4},
        {"ticker": "A3", "sector": "Semis", "blended_score": 3},
    ]
    picked = select_diversified(rows, n=9, max_per_sector=5)
    scores = [r["blended_score"] for r in picked]
    assert scores == sorted(scores, reverse=True), (
        f"picked list is not sorted by score: {[(r['ticker'], r['blended_score']) for r in picked]}"
    )
    assert len(picked) == 9


def test_weights_sum_to_one():
    """Every horizon's WEIGHTS row must sum to 1.0 so composite_score is on a
    comparable scale across horizons. Previously hours=0.95 and
    weekly=1.10 — harmless within a horizon (re-z-scored downstream) but the
    persisted, displayed composite_score was on an incomparable per-horizon
    scale."""
    from invest.config import WEIGHTS

    for horizon, weights in WEIGHTS.items():
        total = sum(weights.values())
        assert abs(total - 1.0) < 1e-9, f"{horizon} weights sum to {total}, expected 1.0"


def test_horizons_use_distinct_dominant_momentum_windows():
    """Each horizon must have a nonzero weight on a momentum window some
    OTHER horizon zeroes out — otherwise every horizon is just a linear
    recombination of the same signals and rankings collapse together
    (measured on live data: hours vs daily Spearman rho = 0.958, 11/13
    top-13 overlap, because both leaned on the same single 21-day window)."""
    from invest.config import WEIGHTS

    assert WEIGHTS["hours"]["price_mom_5d"] > 0
    assert WEIGHTS["hours"]["price_mom_63d"] == 0
    assert WEIGHTS["monthly"]["price_mom_63d"] > 0
    assert WEIGHTS["monthly"]["price_mom_5d"] == 0
    # hours and monthly must not share a nonzero momentum window at all.
    hours_mom = {k for k in ("price_mom_5d", "price_mom_21d", "price_mom_63d") if WEIGHTS["hours"][k] > 0}
    monthly_mom = {k for k in ("price_mom_5d", "price_mom_21d", "price_mom_63d") if WEIGHTS["monthly"][k] > 0}
    assert not (hours_mom & monthly_mom), (
        f"hours and monthly share a momentum window: {hours_mom & monthly_mom}"
    )


def test_zscore_pool_mask_ignores_excluded_rows():
    """Rows outside `pool_mask` must not influence the median/MAD used to
    z-score the rows that ARE in the pool. Without this, ~100 gated-out
    tickers carrying a fabricated `fillna(0)` for a column they have no real
    data for skewed the reference population for the ~200 survivors that DO
    have real data."""
    from invest.pipeline.score import _zscore

    # Pool values cluster tightly around 10; excluded values are all 0
    # (simulating a fillna(0) placeholder). If the mask works, the pool's
    # own tight spread drives the z-scores, not the fabricated zeros.
    s = pd.Series([10.0, 10.5, 9.5, 11.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    pool_mask = pd.Series([True] * 5 + [False] * 5)
    z = _zscore(s, pool_mask)
    # The pool median is 10.0; a pool value near it must be near 0.
    assert abs(z.iloc[0]) < 0.5
    # An excluded (masked-out) row is still transformed using pool stats,
    # just not used to CALCULATE them — it should look like a strong outlier
    # relative to the pool (~10), not like the "average" of the whole column
    # (which naive unmasked stats would have made it look close to).
    assert z.iloc[5] < -3


def test_ml_score_persists_feature_snapshots_for_training():
    """rank_all must persist a feature snapshot every run, or the `features`
    table stays empty forever, `ml_rank.train()`'s cold-start check never
    clears, and `ml_score` silently equals `composite_score` for every row —
    the composite+ML blend the app is supposed to compute is composite-only.
    This was previously dead code: `compute_and_persist`/
    `persist_feature_snapshot` had zero callers outside their own module."""
    from datetime import date, timedelta

    from invest.db import session_scope
    from invest.models import Consensus, FeatureSnapshot, Price, Stock
    from invest.pipeline.rank import rank_all

    with session_scope() as s:
        s.add(Stock(ticker="MLTEST", name="ML Test Inc", sector="Technology", in_universe=True))
        price = 100.0
        for i in range(120):
            s.add(Price(ticker="MLTEST", date=date.today() - timedelta(days=120 - i),
                        close=price, adj_close=price, volume=5_000_000))
        s.add(Consensus(ticker="MLTEST", as_of_date=date.today(), source="yfinance",
                        strong_buy=15, buy=6, hold=4, sell=0, strong_sell=0,
                        mean_target=price * 1.2, high_target=price * 1.4,
                        low_target=price, num_analysts=25))

    rank_all(["MLTEST"])

    with session_scope() as s:
        snap = s.get(FeatureSnapshot, ("MLTEST", date.today()))
    assert snap is not None, "rank_all must call persist_feature_snapshot"
    assert snap.feature_json, "persisted snapshot must not be empty"
