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


def composite_scores(features: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame[ticker, horizon, composite_score] covering all three horizons."""
    z = pd.DataFrame({"ticker": features["ticker"]})
    for col in FEATURE_NAMES:
        if col in features.columns:
            z[col] = _zscore(features[col]).clip(-5, 5)
        else:
            z[col] = 0.0

    mask = liquidity_mask(features).reset_index(drop=True)
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
