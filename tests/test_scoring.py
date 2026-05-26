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
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [True, False, False]


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
