"""Turn a per-ticker feature frame into a composite score per horizon."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import FEATURE_NAMES, HORIZONS, WEIGHTS, Horizon, get_settings


def _zscore(s: pd.Series) -> pd.Series:
    """Standard z-score, hardened against float drift on constant inputs.

    `pd.Series([0.1]*6).std()` is not exactly 0 — it's ~1.5e-17 — so a
    naive `(x - mean) / std` divides comparable garbage by comparable
    garbage and returns spurious ±0.91. We treat any column with fewer
    than two distinct values, or whose std falls below a tiny epsilon,
    as zero-variance and return all-zero contributions.
    """
    x = pd.to_numeric(s, errors="coerce")
    if x.nunique(dropna=True) < 2:
        return pd.Series(np.zeros(len(s)), index=s.index)
    mu = x.mean(skipna=True)
    sd = x.std(skipna=True)
    if not sd or np.isnan(sd) or sd < 1e-12:
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (x - mu) / sd


def liquidity_mask(features: pd.DataFrame) -> pd.Series:
    """True for tickers that pass the liquidity gate."""
    settings = get_settings()
    if "dollar_volume_20d" not in features.columns:
        return pd.Series(True, index=features.index)
    return features["dollar_volume_20d"] >= settings.liquidity_min_dollar_volume


def outlook_mask(features: pd.DataFrame) -> pd.Series:
    """Drop tickers with explicitly negative or insufficiently bullish outlook.

    A stock is excluded from the ranking if ANY of:
      - consensus is not strictly net-bullish  (consensus_z <= min_consensus_z)
      - upside to consensus mean target is below the floor  (upside_z < min_upside)
      - too few analyst firms cover it       (num_analysts < min_firms)

    With the default thresholds (``min_consensus_z = 0`` and
    ``min_upside = 0.04``), stocks with no analyst coverage have
    ``consensus_z = 0`` and ``upside_z = 0`` and so are excluded by design —
    only names that are *demonstrably* positive (covered + bullish + ≥ 4 %
    upside) survive.
    """
    settings = get_settings()
    mask = pd.Series(True, index=features.index)
    if "consensus_z" in features.columns:
        cz = pd.to_numeric(features["consensus_z"], errors="coerce").fillna(0.0)
        # Strict: require net-bullish (> 0), not just non-negative.
        mask &= cz > settings.min_consensus_z
    if "upside_z" in features.columns:
        up = pd.to_numeric(features["upside_z"], errors="coerce").fillna(0.0)
        mask &= up >= settings.min_upside
    if "num_analysts" in features.columns:
        # Require at least `min_firms` covering firms. The strict consensus
        # gate above already removes thinly-covered names; this is a hard
        # backstop for cases where we have stale or partial consensus rows.
        na = pd.to_numeric(features["num_analysts"], errors="coerce").fillna(0.0)
        mask &= na >= settings.min_firms
    if "total_sources_count" in features.columns:
        # Headline coverage floor: every top stock must have at least
        # `min_total_sources` distinct named contributors backing it
        # (sell-side firms in last 90 d + tracked 13F filers + insider
        # filers in last 90 d). Default 50.
        ts = pd.to_numeric(features["total_sources_count"], errors="coerce").fillna(0.0)
        mask &= ts >= settings.min_total_sources
    return mask


def quality_mask(features: pd.DataFrame) -> pd.Series:
    """Combined gate: liquidity + outlook."""
    return liquidity_mask(features) & outlook_mask(features)


def composite_scores(features: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame[ticker, horizon, composite_score] covering all horizons."""
    z = pd.DataFrame({"ticker": features["ticker"]})
    for col in FEATURE_NAMES:
        if col in features.columns:
            z[col] = _zscore(features[col]).clip(-5, 5)
        else:
            z[col] = 0.0

    mask = quality_mask(features).reset_index(drop=True)
    out_rows: list[dict] = []
    for h in HORIZONS:
        w = WEIGHTS[h]
        score = np.zeros(len(z))
        for col, coef in w.items():
            score = score + coef * z[col].to_numpy()
        for i, ticker in enumerate(z["ticker"]):
            if not bool(mask.iloc[i]):
                continue
            out_rows.append(
                {"ticker": ticker, "horizon": h, "composite_score": float(score[i])}
            )
    return pd.DataFrame(out_rows)


def per_feature_contributions(features: pd.DataFrame, horizon: Horizon) -> pd.DataFrame:
    """Return DataFrame[ticker, feature, z, weight, contribution] for explainability."""
    w = WEIGHTS[horizon]
    out: list[dict] = []
    for col in FEATURE_NAMES:
        zs = _zscore(features[col]).clip(-5, 5) if col in features.columns else pd.Series(0.0, index=features.index)
        for ticker, z in zip(features["ticker"], zs):
            out.append(
                {
                    "ticker": ticker,
                    "feature": col,
                    "z": float(z),
                    "weight": w[col],
                    "contribution": float(z * w[col]),
                }
            )
    return pd.DataFrame(out)
