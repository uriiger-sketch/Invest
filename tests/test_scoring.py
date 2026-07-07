from __future__ import annotations

import numpy as np
import pandas as pd

from invest.config import FEATURE_NAMES, HORIZONS
from invest.pipeline.score import composite_scores, liquidity_mask, outlook_mask


def _mk_features(n: int = 10, bullish_outlook: bool = True) -> pd.DataFrame:
    """Build a feature frame.

    When ``bullish_outlook=True`` (default) every ticker has positive
    consensus + ≥ 4 % upside and 12 analysts, so all pass the quality gate.
    """
    rng = np.random.default_rng(42)
    tickers = [f"T{i:02d}" for i in range(n)]
    df = pd.DataFrame({"ticker": tickers, "dollar_volume_20d": 1e9})
    for col in FEATURE_NAMES:
        df[col] = rng.normal(size=n)
    df["last_close"] = 100.0
    df["num_analysts"] = 12
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
    """The headline coverage floor: ≥ 50 distinct named contributors per
    top stock. A name with 49 is excluded; 50 and 100 survive."""
    df = _mk_features(3, bullish_outlook=True)
    df["num_analysts"] = 20
    df["total_sources_count"] = [49, 50, 100]
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [False, True, True]


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
