"""Turn a per-ticker feature frame into a composite score per horizon."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import FEATURE_NAMES, HORIZONS, WEIGHTS, Horizon, get_settings


def _zscore(s: pd.Series) -> pd.Series:
    """Robust z-score using median / MAD instead of mean / std.

    Mean/std z-scores are hostage to outliers: one ticker with a broken
    +900 % "upside" inflates the std and squashes every legitimate value
    toward zero. Median/MAD ignores tails entirely — 1.4826 · MAD equals
    the std for normal data, so scale is comparable to a classic z.

    Also hardened against float drift on constant inputs (a constant
    column's std is ~1e-17, not exactly 0) and falls back to mean/std
    when MAD is 0 but the column still varies (e.g. >50 % identical
    values with a few distinct ones).
    """
    x = pd.to_numeric(s, errors="coerce")
    if x.nunique(dropna=True) < 2:
        return pd.Series(np.zeros(len(s)), index=s.index)
    med = x.median(skipna=True)
    mad = (x - med).abs().median(skipna=True)
    if mad and not np.isnan(mad) and mad > 1e-12:
        return (x - med) / (1.4826 * mad)
    # MAD == 0 but the column varies: fall back to classic z-score.
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


def data_quality_mask(features: pd.DataFrame) -> pd.Series:
    """Exclude tickers whose underlying market data can't be trusted.

    Independent of how bullish the analyst signal looks:
      - stale price: last close older than ``stale_price_max_days``
        (a wrong denominator makes "upside" meaningless)
      - short history: fewer than ``min_price_history_days`` closes
        (volatility / momentum on 10 data points is noise)
      - absurd upside: > ``max_upside_sane`` (200 %) almost always means
        stale or mis-scaled target data, not a real opportunity
    Each check only applies when its column is present, so unit tests and
    partial frames aren't forced to fabricate every column.
    """
    settings = get_settings()
    mask = pd.Series(True, index=features.index)
    if "last_price_age_days" in features.columns:
        age = pd.to_numeric(features["last_price_age_days"], errors="coerce").fillna(999)
        mask &= age <= settings.stale_price_max_days
    if "price_history_days" in features.columns:
        hist = pd.to_numeric(features["price_history_days"], errors="coerce").fillna(0)
        mask &= hist >= settings.min_price_history_days
    if "upside_z" in features.columns:
        up = pd.to_numeric(features["upside_z"], errors="coerce").fillna(0.0)
        mask &= up <= settings.max_upside_sane
    return mask


def quality_mask(features: pd.DataFrame) -> pd.Series:
    """Combined gate: liquidity + outlook + data quality."""
    return liquidity_mask(features) & outlook_mask(features) & data_quality_mask(features)


def composite_scores(features: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame[ticker, horizon, composite_score] covering all horizons."""
    settings = get_settings()
    z = pd.DataFrame({"ticker": features["ticker"]})
    for col in FEATURE_NAMES:
        if col in features.columns:
            raw = features[col]
            if col == "upside_z":
                # Cap the raw upside used for scoring so one 90 % outlier
                # (often stale target data) can't dominate the whole rank.
                raw = pd.to_numeric(raw, errors="coerce").clip(upper=settings.upside_cap)
            z[col] = _zscore(raw).clip(-5, 5)
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
