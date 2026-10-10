"""Calibration and the integrated final grade.

Pipeline (one run of `rank_all`):

1. **Factor ICs, measured.** For every stored daily feature snapshot, the
   cross-sectional Spearman correlation between each feature and the
   realised forward return over each horizon gives an IC time series. Its
   mean and standard error — with the effective sample size reduced for
   overlapping forward windows (Hansen–Hodrick) and a floor on the IC
   volatility so a short history cannot look precise — update the
   literature prior (config.PRIOR_IC, SD = prior_ic_sd) by precision
   weighting:  IC_post = (μ₀/τ² + m/SE²) / (1/τ² + 1/SE²).

2. **Weights.** w_h = C⁻¹ · IC_post,h with C the cross-sectional correlation
   of today's standardised features, shrunk toward I. Correlated signals
   (consensus level vs target upside vs rating momentum) therefore share
   their weight instead of being counted two or three times.

3. **Composite/ML blend.** The two scores are combined with the same rule
   for two signals, using the ML model's purged out-of-sample IC (a model
   without credible OOS skill gets weight 0, capped at blend_ml_weight).

4. **Horizon IC.** The ex-ante composite IC √(ICᵀC⁻¹IC), haircut for
   estimation error, is the prior for each horizon's skill; the realised IC
   of this pipeline's own past published scores updates it.

5. **Grade.** Each gated ticker has a standardised score S_h per horizon.
   The integrated grade is the optimal linear combination of correlated
   z-scores, weighted by horizon skill a_h = IC_h:
          G = Σ a_h S_h / √(aᵀ R a)       (R = cross-horizon correlation)
   so G ~ N(0, 1) across the gated universe. From the same model:
          α_h = IC_h · σ_h · S_h          (expected excess return, Grinold)
          P(outperform) = Φ(IC_h · S_h)
   and a confidence = share of the model's weight backed by observed data.
"""
from __future__ import annotations

import json
import logging
import math
from dataclasses import dataclass, field
from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy.stats import norm
from sqlalchemy import select

from ..config import FEATURE_NAMES, FORWARD_WINDOW_DAYS, HORIZONS, PRIOR_IC, get_settings
from ..db import session_scope
from ..models import Calibration, Grade, Price, Score
from .score import standardize, stats_pool_mask

logger = logging.getLogger(__name__)

# Floor on the cross-sectional IC volatility used for standard errors. A
# handful of dates can show a spuriously tight IC series; real factor ICs
# swing by ~0.05-0.15 from period to period.
_MIN_IC_SD = 0.06
# Prior SD on each horizon's overall skill (composite IC).
_HORIZON_IC_SD = 0.03
# Prior on the ML model's skill: zero, i.e. skeptical until shown otherwise.
_ML_PRIOR_IC, _ML_PRIOR_SD = 0.0, 0.02

FEATURE_LABELS: dict[str, str] = {
    "consensus_z": "analyst consensus",
    "consensus_delta": "consensus improving",
    "upside_z": "target upside",
    "target_dispersion": "analyst disagreement",
    "target_revision_30d": "consensus target revised",
    "firm_target_revision": "firm target changes",
    "rating_mom_7d": "rating changes (7d)",
    "rating_mom_30d": "rating changes (30d)",
    "eps_revision": "EPS estimate revisions",
    "eps_revision_breadth": "EPS revision breadth",
    "earnings_surprise": "earnings surprise",
    "news_sentiment": "news tone",
    "inst_flow_13f": "13F institutional flow",
    "insider_signal": "insider buying",
    "short_interest": "short interest",
    "activist_13d": "activist 13D stake",
    "sec_red_flags": "SEC red-flag filings",
    "value": "valuation",
    "quality": "profitability",
    "price_mom_5d": "1-week move",
    "price_mom_21d": "1-month move",
    "price_mom_63d": "3-month momentum",
    "mom_12_1": "12-1 momentum",
    "high_52w": "near 52-week high",
    "risk_penalty": "low volatility",
}


def posterior(prior_mean: float, prior_sd: float, est: float | None, se: float | None) -> tuple[float, float]:
    """Normal-normal precision-weighted update; returns (mean, sd)."""
    if est is None or se is None or not math.isfinite(est) or not math.isfinite(se) or se <= 0:
        return prior_mean, prior_sd
    p0, p1 = 1.0 / prior_sd**2, 1.0 / se**2
    return (prior_mean * p0 + est * p1) / (p0 + p1), math.sqrt(1.0 / (p0 + p1))


def ic_summary(ics: list[float], horizon_days: int) -> tuple[float | None, float | None, int]:
    """(mean, SE, n_dates) of a daily IC series with overlapping windows."""
    vals = [v for v in ics if v is not None and math.isfinite(v)]
    n = len(vals)
    if n == 0:
        return None, None, 0
    m = float(np.mean(vals))
    sd = max(float(np.std(vals, ddof=1)) if n > 1 else _MIN_IC_SD, _MIN_IC_SD)
    n_eff = max(1.0, n / max(1, min(horizon_days, n)))
    return m, sd / math.sqrt(n_eff), n


# ------------------------------------------------------------ forward returns


def forward_returns(tickers: list[str], horizon_days: int, since: date) -> pd.DataFrame:
    """[ticker, date, fwd] — close-to-close return over the next
    `horizon_days` trading sessions of THAT ticker's own calendar (TASE
    trades Sun–Thu), after dropping one-day reverting spikes."""
    from .features import spike_mask

    with session_scope() as s:
        rows = s.execute(
            select(Price.ticker, Price.date, Price.close).where(
                Price.ticker.in_(tickers), Price.date >= since, Price.close.isnot(None)
            )
        ).all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "date", "fwd"])
    df = pd.DataFrame(rows, columns=["ticker", "date", "close"]).sort_values(["ticker", "date"])
    parts = []
    for t, g in df.groupby("ticker"):
        c = g["close"].astype(float).to_numpy()
        keep = spike_mask(c)
        g = g[keep]
        c = g["close"].astype(float)
        fwd = c.shift(-horizon_days) / c - 1
        parts.append(pd.DataFrame({"ticker": t, "date": g["date"].to_numpy(), "fwd": fwd.to_numpy()}))
    out = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=["ticker", "date", "fwd"])
    return out.dropna(subset=["fwd"])


def _attach_returns(panel: pd.DataFrame, fwd: pd.DataFrame) -> pd.DataFrame:
    """Join snapshot rows (ticker, as_of) to the forward return measured from
    the last trading close on or before as_of (weekend snapshots map to
    Friday; duplicates keep the latest snapshot)."""
    if panel.empty or fwd.empty:
        return pd.DataFrame()
    p = panel.copy()
    p["as_of"] = pd.to_datetime(p["as_of"])
    f = fwd.copy()
    f["date"] = pd.to_datetime(f["date"])
    p = p.sort_values("as_of")
    f = f.sort_values("date")
    merged = pd.merge_asof(
        p, f, left_on="as_of", right_on="date", by="ticker", direction="backward",
        tolerance=pd.Timedelta(days=4),
    )
    merged = merged.dropna(subset=["fwd"])
    merged = merged.sort_values("as_of").drop_duplicates(["ticker", "date"], keep="last")
    return merged


def _daily_spearman(df: pd.DataFrame, cols: list[str], min_n: int = 20) -> dict[str, list[float]]:
    out: dict[str, list[float]] = {c: [] for c in cols}
    for _, g in df.groupby("date"):
        r_ret = g["fwd"].rank()
        for c in cols:
            x = pd.to_numeric(g[c], errors="coerce")
            ok = x.notna() & g["fwd"].notna()
            if ok.sum() < min_n or x[ok].nunique() < 3:
                continue
            rho = np.corrcoef(x[ok].rank(), r_ret[ok].rank())[0, 1]
            if math.isfinite(rho):
                out[c].append(float(rho))
    return out


def measure_factor_ics(lookback_days: int = 200) -> dict[str, dict[str, tuple]]:
    """{horizon: {feature: (mean IC, SE, n_dates)}} from stored snapshots."""
    from .features import load_feature_snapshots

    since = date.today() - timedelta(days=lookback_days)
    snaps = load_feature_snapshots(min_as_of=since)
    result: dict[str, dict[str, tuple]] = {h: {} for h in HORIZONS}
    if snaps.empty:
        return result
    tickers = snaps["ticker"].unique().tolist()
    for h in HORIZONS:
        hd = FORWARD_WINDOW_DAYS[h]
        fwd = forward_returns(tickers, hd, since)
        panel = _attach_returns(snaps[["ticker", "as_of", *FEATURE_NAMES]], fwd)
        if panel.empty:
            continue
        series = _daily_spearman(panel, list(FEATURE_NAMES))
        for f, ics in series.items():
            result[h][f] = ic_summary(ics, hd)
    return result


def measure_score_ics(lookback_days: int = 200) -> dict[str, tuple]:
    """Realised IC of this pipeline's own persisted blended scores."""
    since = date.today() - timedelta(days=lookback_days)
    with session_scope() as s:
        rows = s.execute(
            select(Score.ticker, Score.horizon, Score.as_of, Score.blended_score).where(
                Score.as_of >= since
            )
        ).all()
    out: dict[str, tuple] = {}
    if not rows:
        return out
    df = pd.DataFrame(rows, columns=["ticker", "horizon", "as_of", "score"])
    tickers = df["ticker"].unique().tolist()
    for h in HORIZONS:
        sub = df[df["horizon"] == h]
        if sub.empty:
            continue
        hd = FORWARD_WINDOW_DAYS[h]
        panel = _attach_returns(sub[["ticker", "as_of", "score"]], forward_returns(tickers, hd, since))
        if panel.empty:
            continue
        out[h] = ic_summary(_daily_spearman(panel, ["score"], min_n=15)["score"], hd)
    return out


# ---------------------------------------------------------------- weights


@dataclass
class Calibrated:
    weights: dict[str, dict[str, float]]
    factor_ic: dict[str, dict[str, dict]] = field(default_factory=dict)
    horizon_ic: dict[str, dict] = field(default_factory=dict)
    ml: dict[str, dict] = field(default_factory=dict)


def _shrunk_corr(z: pd.DataFrame, delta: float) -> np.ndarray:
    k = z.shape[1]
    if len(z) < 3:
        return np.eye(k)
    c = np.corrcoef(z.to_numpy(dtype=float), rowvar=False)
    c = np.nan_to_num(c, nan=0.0)
    np.fill_diagonal(c, 1.0)
    return (1 - delta) * c + delta * np.eye(k)


def calibrate(features: pd.DataFrame, measured: dict | None = None,
              score_ics: dict | None = None) -> Calibrated:
    """Posterior factor ICs and correlation-aware weights per horizon."""
    settings = get_settings()
    if measured is None:
        try:
            measured = measure_factor_ics()
        except Exception:  # noqa: BLE001 — calibration must never block ranking
            logger.exception("factor IC measurement failed; using priors only")
            measured = {h: {} for h in HORIZONS}
    if score_ics is None:
        try:
            score_ics = measure_score_ics()
        except Exception:  # noqa: BLE001
            logger.exception("score IC measurement failed; using ex-ante skill only")
            score_ics = {}

    pool = stats_pool_mask(features)
    z = standardize(features, pool).fillna(0.0)
    zp = z.loc[pool.to_numpy(), list(FEATURE_NAMES)] if pool.any() else z[list(FEATURE_NAMES)]
    corr = _shrunk_corr(zp, settings.corr_shrinkage)
    corr_inv = np.linalg.inv(corr)

    weights: dict[str, dict[str, float]] = {}
    factor_ic: dict[str, dict[str, dict]] = {}
    horizon_ic: dict[str, dict] = {}
    for h in HORIZONS:
        post = []
        fic: dict[str, dict] = {}
        for f in FEATURE_NAMES:
            m, se, n = measured.get(h, {}).get(f, (None, None, 0))
            if n < settings.min_ic_dates:
                m, se = None, None
            mu, sd = posterior(PRIOR_IC[h][f], settings.prior_ic_sd, m, se)
            post.append(mu)
            fic[f] = {"prior": PRIOR_IC[h][f], "measured": m, "se": se, "n_dates": n,
                      "posterior": round(mu, 5), "posterior_sd": round(sd, 5)}
        ic_vec = np.array(post)
        w = corr_inv @ ic_vec
        norm1 = float(np.abs(w).sum()) or 1.0
        weights[h] = {f: float(wi / norm1) for f, wi in zip(FEATURE_NAMES, w)}
        for f in FEATURE_NAMES:
            fic[f]["weight"] = round(weights[h][f], 5)
        factor_ic[h] = fic
        exante = float(math.sqrt(max(ic_vec @ corr_inv @ ic_vec, 0.0))) * settings.ic_haircut
        m, se, n = score_ics.get(h, (None, None, 0))
        if n < settings.min_ic_dates:
            m, se = None, None
        mu, sd = posterior(exante, _HORIZON_IC_SD, m, se)
        horizon_ic[h] = {"exante": round(exante, 5), "realised": m, "realised_se": se,
                         "n_dates": n, "posterior": round(max(mu, 0.0), 5),
                         "posterior_sd": round(sd, 5)}
    return Calibrated(weights=weights, factor_ic=factor_ic, horizon_ic=horizon_ic)


def ml_blend(comp_z: pd.Series, ml_z: pd.Series, ml_meta: dict | None,
             composite_ic: float) -> tuple[float, float, dict]:
    """(w_composite, w_ml, diagnostics) via the two-signal Σ⁻¹·IC rule."""
    settings = get_settings()
    info: dict = {"available": bool(ml_meta)}
    if not ml_meta:
        return 1.0, 0.0, info
    est, se = ml_meta.get("val_ic"), ml_meta.get("val_ic_se")
    ic_ml, sd = posterior(_ML_PRIOR_IC, _ML_PRIOR_SD, est, se)
    info.update({"val_ic": est, "val_ic_se": se, "posterior": round(ic_ml, 5),
                 "posterior_sd": round(sd, 5)})
    if ic_ml <= 0:
        info["weight"] = 0.0
        return 1.0, 0.0, info
    ok = comp_z.notna() & ml_z.notna()
    rho = float(np.corrcoef(comp_z[ok], ml_z[ok])[0, 1]) if ok.sum() > 2 else 0.0
    rho = float(np.clip(np.nan_to_num(rho), -0.95, 0.95))
    r_inv = np.linalg.inv(np.array([[1.0, rho], [rho, 1.0]]))
    w = r_inv @ np.array([max(composite_ic, 1e-4), ic_ml])
    w = np.clip(w, 0.0, None)
    if w.sum() <= 0:
        return 1.0, 0.0, info
    # The cap applies in every case, so an over-fitted model can never
    # dominate even when the composite's own skill estimate is weak.
    share_ml = min(float(w[1] / w.sum()), settings.blend_ml_weight)
    info.update({"rho": round(rho, 4), "weight": round(share_ml, 4)})
    return 1.0 - share_ml, share_ml, info


# ------------------------------------------------------------------ grading

_LETTERS = ((0.97, "A+"), (0.90, "A"), (0.80, "A-"), (0.70, "B+"), (0.55, "B"),
            (0.40, "B-"), (0.30, "C+"), (0.15, "C"), (0.0, "D"))


def letter_for(pct: float) -> str:
    for cut, letter in _LETTERS:
        if pct >= cut:
            return letter
    return "D"


def integrated_grades(merged: pd.DataFrame, features: pd.DataFrame, calib: Calibrated) -> pd.DataFrame:
    """One row per gated ticker: grade score G, letter, percentile,
    confidence, expected 1M/3M excess return, P(outperform 1M), drivers."""
    if merged.empty:
        return pd.DataFrame()
    wide = merged.pivot_table(index="ticker", columns="horizon", values="blended_score")
    hs = [h for h in HORIZONS if h in wide.columns]
    wide = wide[hs].dropna()
    if wide.empty:
        return pd.DataFrame()
    a = np.array([max(calib.horizon_ic.get(h, {}).get("posterior", 0.0), 1e-3) for h in hs])
    S = wide.to_numpy(dtype=float)
    if len(wide) >= 3:
        R = np.nan_to_num(np.corrcoef(S, rowvar=False), nan=0.0)
        np.fill_diagonal(R, 1.0)
    else:
        R = np.eye(len(hs))
    denom = math.sqrt(max(float(a @ R @ a), 1e-12))
    G = (S @ a) / denom
    out = pd.DataFrame({"ticker": wide.index, "grade_score": G})
    out["percentile"] = out["grade_score"].rank(pct=True)
    out["letter"] = out["percentile"].map(letter_for)

    feats = features.set_index("ticker")
    pool = stats_pool_mask(features)
    zall = standardize(features, pool).set_index("ticker")
    vol = pd.to_numeric(feats.get("vol_60d"), errors="coerce") if "vol_60d" in feats else None
    vol_med = float(vol.median()) if vol is not None and vol.notna().any() else 0.35
    a_norm = a / a.sum()

    rows = []
    for i, t in enumerate(wide.index):
        zt = zall.loc[t, list(FEATURE_NAMES)] if t in zall.index else pd.Series(np.nan, index=FEATURE_NAMES)
        observed = zt.notna()
        conf_h, contrib = [], np.zeros(len(FEATURE_NAMES))
        for j, h in enumerate(hs):
            w = np.array([calib.weights[h][f] for f in FEATURE_NAMES])
            tot = np.abs(w).sum() or 1.0
            conf_h.append(float(np.abs(w[observed.to_numpy()]).sum() / tot))
            contrib += a_norm[j] * w * zt.fillna(0.0).to_numpy()
        conf = float(np.dot(a_norm, conf_h))
        sig = float(vol.get(t, np.nan)) if vol is not None else np.nan
        sig = sig if math.isfinite(sig) and sig > 0 else vol_med

        def alpha(h: str, t: str = t, sig: float = sig) -> float | None:
            """Grinold: α = IC · σ_h · S_h (expected excess return over h)."""
            if h not in hs:
                return None
            ic = calib.horizon_ic.get(h, {}).get("posterior", 0.0)
            s_h = float(wide.loc[t, h])
            return ic * sig * math.sqrt(FORWARD_WINDOW_DAYS[h] / 252.0) * s_h

        s_w = float(wide.loc[t, "weekly"]) if "weekly" in hs else float(G[i])
        ic_w = calib.horizon_ic.get("weekly", {}).get("posterior", 0.0)
        order = np.argsort(contrib)
        pos = [(FEATURE_NAMES[k], round(float(contrib[k]), 4)) for k in order[::-1][:3] if contrib[k] > 0.01]
        neg = [(FEATURE_NAMES[k], round(float(contrib[k]), 4)) for k in order[:2] if contrib[k] < -0.01]
        rows.append({
            "ticker": t,
            "confidence": conf,
            "alpha_1m": alpha("weekly"),
            "alpha_3m": alpha("monthly"),
            "p_outperform_1m": float(norm.cdf(ic_w * s_w)),
            "detail": {
                "S": {h: round(float(wide.loc[t, h]), 4) for h in hs},
                "drivers_pos": pos,
                "drivers_neg": neg,
                "conf_by_h": {h: round(c, 3) for h, c in zip(hs, conf_h)},
                "vol": round(sig, 4),
            },
        })
    return out.merge(pd.DataFrame(rows), on="ticker", how="left")


def persist_grades(grades: pd.DataFrame, calib: Calibrated, as_of: date | None = None) -> None:
    from sqlalchemy.dialects.sqlite import insert as sqlite_insert

    as_of = as_of or date.today()
    if not grades.empty:
        recs = [
            {
                "ticker": r.ticker,
                "as_of": as_of,
                "grade_score": float(r.grade_score),
                "letter": r.letter,
                "percentile": float(r.percentile),
                "confidence": float(r.confidence),
                "alpha_1m": None if r.alpha_1m is None or pd.isna(r.alpha_1m) else float(r.alpha_1m),
                "p_outperform_1m": float(r.p_outperform_1m),
                "alpha_3m": None if r.alpha_3m is None or pd.isna(r.alpha_3m) else float(r.alpha_3m),
                "detail_json": json.dumps(r.detail, separators=(",", ":")),
            }
            for r in grades.itertuples(index=False)
        ]
        with session_scope() as s:
            # Today's grade set is replaced wholesale: a ticker that dropped
            # out of the gated pool since the previous run must not linger.
            s.query(Grade).filter(Grade.as_of == as_of).delete()
            s.execute(sqlite_insert(Grade).values(recs))
    with session_scope() as s:
        for h in HORIZONS:
            payload = json.dumps({
                "horizon_ic": calib.horizon_ic.get(h, {}),
                "ml": calib.ml.get(h, {}),
                "factors": calib.factor_ic.get(h, {}),
            }, separators=(",", ":"), default=float)
            row = s.get(Calibration, (as_of, h))
            if row is None:
                s.add(Calibration(as_of=as_of, horizon=h, payload=payload))
            else:
                row.payload = payload
