from __future__ import annotations

import numpy as np
import pandas as pd

from invest.config import FEATURE_NAMES, HORIZONS
from invest.pipeline.score import composite_scores, liquidity_mask, outlook_mask


def _mk_features(n: int = 10, neutral_outlook: bool = True) -> pd.DataFrame:
    """Build a feature frame.

    When `neutral_outlook=True` (default) all outlook-gate inputs are set to 0
    so every ticker passes the quality gate — useful for tests that only care
    about scoring shape / liquidity.
    """
    rng = np.random.default_rng(42)
    tickers = [f"T{i:02d}" for i in range(n)]
    df = pd.DataFrame({"ticker": tickers, "dollar_volume_20d": 1e9})
    for col in FEATURE_NAMES:
        df[col] = rng.normal(size=n)
    df["last_close"] = 100.0
    df["firm_count_90d"] = 10
    if neutral_outlook:
        df["consensus_z"] = 0.0
        df["upside_z"] = 0.0
    return df


def test_composite_scores_return_row_per_ticker_per_horizon():
    df = _mk_features(8)
    out = composite_scores(df)
    assert not out.empty
    # 8 tickers × len(HORIZONS) rows (everyone passes the quality gate).
    assert len(out) == 8 * len(HORIZONS)
    assert set(out["horizon"].unique()) == set(HORIZONS)


def test_outlook_mask_drops_negative_consensus_or_upside():
    df = _mk_features(4, neutral_outlook=False)
    df["consensus_z"] = [0.5, -0.5, 0.0, 0.5]
    df["upside_z"] = [0.10, 0.10, 0.10, -0.20]
    df["firm_count_90d"] = 10
    mask = outlook_mask(df).reset_index(drop=True)
    assert list(mask) == [True, False, True, False]


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
    out = composite_scores(df)
    # All z-scores are zero, so every composite score should be zero.
    assert np.allclose(out["composite_score"], 0.0)


def test_liquidity_below_threshold_drops_ticker_from_all_horizons():
    df = _mk_features(4)
    df.loc[0, "dollar_volume_20d"] = 100.0
    out = composite_scores(df)
    assert "T00" not in set(out["ticker"])
