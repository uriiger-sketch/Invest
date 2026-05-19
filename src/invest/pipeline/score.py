"""Turn a per-ticker feature frame into a composite score per horizon."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..config import FEATURE_NAMES, HORIZONS, WEIGHTS, Horizon, get_settings


def _zscore(s: pd.Series) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    mu = x.mean(skipna=True)
    sd = x.std(skipna=True)
    if not sd or np.isnan(sd) or sd == 0:
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (x - mu) / sd


def liquidity_mask(features: pd.DataFrame) -> pd.Series:
    """True for tickers that pass the liquidity gate."""
    settings = get_settings()
    if "dollar_volume_20d" not in features.columns:
        return pd.Series(True, index=features.index)
    return features["dollar_volume_20d"] >= settings.liquidity_min_dollar_volume


def outlook_mask(features: pd.DataFrame) -> pd.Series:
    """Drop tickers with explicitly negative analyst outlook.

    A stock is excluded from the ranking if ANY of:
      - consensus is net-bearish (more sells than buys, raw consensus_z < min)
      - the consensus price target is meaningfully below the last close
      - too few analyst firms cover it for the consensus signal to be reliable
    Stocks with no consensus data (consensus_z == 0) are treated as neutral
    and ALLOWED through, so non-US names without rich coverage aren't
    needlessly excluded.
    """
    settings = get_settings()
    mask = pd.Series(True, index=features.index)
    if "consensus_z" in features.columns:
        cz = pd.to_numeric(features["consensus_z"], errors="coerce").fillna(0.0)
        # Only filter strictly bearish; treat 0/NaN as neutral.
        mask &= cz >= settings.min_consensus_z
    if "upside_z" in features.columns:
        up = pd.to_numeric(features["upside_z"], errors="coerce").fillna(0.0)
        mask &= up >= settings.min_upside
    if "firm_count_90d" in features.columns:
        fc = pd.to_numeric(features["firm_count_90d"], errors="coerce").fillna(0.0)
        # Only enforce min-firms when the ticker has ANY consensus data; this
        # avoids excluding small/foreign names purely for thin sell-side coverage.
        has_consensus = (
            pd.to_numeric(features.get("consensus_z", 0), errors="coerce").fillna(0.0) != 0
        )
        mask &= (~has_consensus) | (fc >= settings.min_firms)
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
