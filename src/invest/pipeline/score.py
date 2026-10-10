"""Turn a per-ticker feature frame into a composite score per horizon.

Standardisation is a NaN-aware RANK-GAUSSIAN transform: each value's
empirical CDF position inside the reference pool is mapped through the
inverse normal, z = Φ⁻¹(p). This is the conventional cross-sectional
normalisation for combining heterogeneous signals: every feature becomes
N(0, 1) regardless of its units or tails, a single broken value can never
dominate (a +900 % "upside" is just the top rank), and nothing needs ad-hoc
clipping. Unobserved values stay NaN through the transform and contribute
z = 0 — the prior mean — to the composite.

Selected features are then partially sector-neutralised
(`config.SECTOR_NEUTRAL`), because valuation, profitability, short interest
and sell-side optimism are only comparable within an industry.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import norm

from ..config import FEATURE_NAMES, HORIZONS, SECTOR_NEUTRAL, WEIGHTS, Horizon, get_settings


def _zscore(s: pd.Series, pool_mask: pd.Series | None = None) -> pd.Series:
    """Robust z-score using median / MAD instead of mean / std.

    Still used to standardise the per-horizon composite and ML scores
    (rank.py), where magnitudes — not just ranks — carry information.
    `pool_mask` restricts which rows the median/MAD are COMPUTED from while
    the transform applies to every row. Falls back to mean/std when MAD is 0
    but the column still varies.
    """
    x = pd.to_numeric(s, errors="coerce")
    pool = x if pool_mask is None else x[pool_mask.to_numpy()]
    if pool.nunique(dropna=True) < 2:
        return pd.Series(np.zeros(len(s)), index=s.index)
    med = pool.median(skipna=True)
    mad = (pool - med).abs().median(skipna=True)
    if mad and not np.isnan(mad) and mad > 1e-12:
        return (x - med) / (1.4826 * mad)
    mu = pool.mean(skipna=True)
    sd = pool.std(skipna=True)
    if not sd or np.isnan(sd) or sd < 1e-12:
        return pd.Series(np.zeros(len(s)), index=s.index)
    return (x - mu) / sd


def rank_gauss(s: pd.Series, pool_mask: pd.Series | None = None) -> pd.Series:
    """z = Φ⁻¹(mid-rank CDF position within the pool); NaN stays NaN.

    Ties share the mid-rank (so equal raw values get identical z), and the
    CDF is clamped to [0.5/n, 1 − 0.5/n] so extremes stay finite. A column
    with fewer than two distinct observed values carries no cross-sectional
    information and maps to 0.
    """
    x = pd.to_numeric(s, errors="coerce").astype(float)
    pool = x if pool_mask is None else x[pool_mask.to_numpy()]
    pool = pool.dropna().to_numpy()
    out = pd.Series(np.nan, index=s.index, dtype=float)
    obs = x.notna().to_numpy()
    if len(pool) < 2 or np.unique(pool).size < 2:
        out[obs] = 0.0
        return out
    srt = np.sort(pool)
    n = len(srt)
    vals = x.to_numpy()[obs]
    lo = np.searchsorted(srt, vals, side="left")
    hi = np.searchsorted(srt, vals, side="right")
    p = (lo + hi) / 2.0 / n
    p = np.clip(p, 0.5 / n, 1 - 0.5 / n)
    out[obs] = norm.ppf(p)
    return out


def standardize(features: pd.DataFrame, pool_mask: pd.Series | None = None) -> pd.DataFrame:
    """[ticker, <feature z>…] — rank-gaussian, sector-neutralised, NaN kept.

    Upside is capped at `upside_cap` before ranking so stale/outlier
    targets tie at the cap rather than outranking real opportunities.
    """
    settings = get_settings()
    z = pd.DataFrame({"ticker": features["ticker"]}, index=features.index)
    has_sector = "sector" in features.columns
    for col in FEATURE_NAMES:
        if col not in features.columns:
            z[col] = np.nan
            continue
        raw = pd.to_numeric(features[col], errors="coerce")
        if col == "upside_z":
            raw = raw.clip(upper=settings.upside_cap)
        zc = rank_gauss(raw, pool_mask)
        lam = SECTOR_NEUTRAL.get(col, 0.0)
        if lam and has_sector:
            sec = features["sector"].fillna("").astype(str)
            pool = pool_mask if pool_mask is not None else pd.Series(True, index=features.index)
            ref = zc.where(pool.to_numpy())
            means = ref.groupby(sec).mean()
            counts = ref.groupby(sec).count()
            # Only demean within sectors large enough to estimate a mean.
            means = means.where(counts >= 5, 0.0)
            zc = zc - lam * sec.map(means).fillna(0.0).to_numpy()
        z[col] = zc
    return z


def liquidity_mask(features: pd.DataFrame) -> pd.Series:
    """True for tickers that pass the liquidity gate."""
    settings = get_settings()
    if "dollar_volume_20d" not in features.columns:
        return pd.Series(True, index=features.index)
    return features["dollar_volume_20d"] >= settings.liquidity_min_dollar_volume


def outlook_mask(features: pd.DataFrame) -> pd.Series:
    """Drop tickers with explicitly negative or insufficiently bullish outlook.

    Excluded if ANY of: consensus not strictly net-bullish; upside below the
    floor (a discarded/suspect target counts as no upside); fewer than
    `min_firms` covering analysts; fewer than `min_total_sources` distinct
    contributors.
    """
    settings = get_settings()
    mask = pd.Series(True, index=features.index)
    if "consensus_z" in features.columns:
        cz = pd.to_numeric(features["consensus_z"], errors="coerce").fillna(0.0)
        mask &= cz > settings.min_consensus_z
    if "upside_z" in features.columns:
        up = pd.to_numeric(features["upside_z"], errors="coerce").fillna(0.0)
        mask &= up >= settings.min_upside
    if "num_analysts" in features.columns:
        na = pd.to_numeric(features["num_analysts"], errors="coerce").fillna(0.0)
        mask &= na >= settings.min_firms
    if "total_sources_count" in features.columns:
        ts = pd.to_numeric(features["total_sources_count"], errors="coerce").fillna(0.0)
        mask &= ts >= settings.min_total_sources
    return mask


def data_quality_mask(features: pd.DataFrame) -> pd.Series:
    """Exclude tickers whose underlying market data can't be trusted:
    stale last close, too little history, absurd (> max_upside_sane) upside.
    Each check applies only when its column is present."""
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


def gate_survivors(features: pd.DataFrame) -> dict[str, int]:
    """Per-gate survivor counts, for diagnosing a total wipeout."""
    total = len(features)
    liq = liquidity_mask(features)
    out = outlook_mask(features)
    dq = data_quality_mask(features)
    counts = {
        "universe": total,
        "liquidity": int(liq.sum()),
        "outlook": int(out.sum()),
        "data_quality": int(dq.sum()),
        "combined": int((liq & out & dq).sum()),
    }
    settings = get_settings()
    if "consensus_z" in features.columns:
        cz = pd.to_numeric(features["consensus_z"], errors="coerce").fillna(0.0)
        counts["outlook.consensus"] = int((cz > settings.min_consensus_z).sum())
    if "upside_z" in features.columns:
        up = pd.to_numeric(features["upside_z"], errors="coerce").fillna(0.0)
        counts["outlook.upside"] = int((up >= settings.min_upside).sum())
    if "num_analysts" in features.columns:
        na = pd.to_numeric(features["num_analysts"], errors="coerce").fillna(0.0)
        counts["outlook.min_firms"] = int((na >= settings.min_firms).sum())
    if "total_sources_count" in features.columns:
        ts = pd.to_numeric(features["total_sources_count"], errors="coerce").fillna(0.0)
        counts["outlook.total_sources"] = int((ts >= settings.min_total_sources).sum())
    if "target_suspect" in features.columns:
        counts["data_quality.target_suspect"] = int(features["target_suspect"].fillna(False).sum())
    return counts


def quality_mask(features: pd.DataFrame) -> pd.Series:
    """Combined gate: liquidity + outlook + data quality."""
    return liquidity_mask(features) & outlook_mask(features) & data_quality_mask(features)


def stats_pool_mask(features: pd.DataFrame) -> pd.Series:
    """Tickers trustworthy enough to anchor the standardisation: liquidity +
    data-quality survivors (NOT the outlook gate, which is evaluated on these
    same raw columns — excluding on it first would be circular)."""
    return liquidity_mask(features) & data_quality_mask(features)


_stats_pool_mask = stats_pool_mask  # backwards-compatible name


def composite_scores(
    features: pd.DataFrame, weights: dict[str, dict[str, float]] | None = None
) -> pd.DataFrame:
    """DataFrame[ticker, horizon, composite_score] for tickers passing every gate.

    `weights` maps horizon -> {feature: weight}; defaults to the normalised
    literature priors (`config.WEIGHTS`). rank_all passes the calibrated,
    correlation-aware weights from `pipeline.grade.calibrated_weights`.
    """
    weights = weights or WEIGHTS
    z = standardize(features, stats_pool_mask(features)).fillna(0.0)
    mask = quality_mask(features).to_numpy()
    out_rows: list[dict] = []
    for h in HORIZONS:
        w = weights[h]
        score = np.zeros(len(z))
        for col, coef in w.items():
            if col in z.columns and coef:
                score = score + coef * z[col].to_numpy()
        for i, ticker in enumerate(z["ticker"]):
            if mask[i]:
                out_rows.append({"ticker": ticker, "horizon": h, "composite_score": float(score[i])})
    return pd.DataFrame(out_rows, columns=["ticker", "horizon", "composite_score"])


def per_feature_contributions(
    features: pd.DataFrame, horizon: Horizon, weights: dict[str, dict[str, float]] | None = None
) -> pd.DataFrame:
    """DataFrame[ticker, feature, z, weight, contribution] — mirrors
    `composite_scores` exactly, so contributions sum to the composite."""
    weights = weights or WEIGHTS
    z = standardize(features, stats_pool_mask(features))
    w = weights[horizon]
    out: list[dict] = []
    for col in FEATURE_NAMES:
        zs = z[col]
        for ticker, zv in zip(features["ticker"], zs):
            zf = 0.0 if pd.isna(zv) else float(zv)
            out.append({
                "ticker": ticker,
                "feature": col,
                "z": zf,
                "observed": not pd.isna(zv),
                "weight": w.get(col, 0.0),
                "contribution": zf * w.get(col, 0.0),
            })
    return pd.DataFrame(out)
