"""LightGBM ranker per horizon, validated out-of-sample before it is trusted.

Changes from the original regressor (each one a methodological fix):

* Target = the CROSS-SECTIONAL rank of the forward return on each date,
  gaussianised (Φ⁻¹ of the mid-rank). Raw returns are dominated by the
  market-wide move of that day, which no stock-level feature can predict,
  and by a few outliers; the ranking task is relative performance.
* Purged walk-forward validation: dates are split chronologically and the
  last `horizon` dates before the validation block are dropped (embargo),
  because a 20-day forward label on the final training date overlaps the
  first validation dates — the old 80/20 row split leaked the answer.
* The validation IC (mean per-date Spearman of prediction vs realised
  return) and its standard error are saved next to the model. The blend in
  `pipeline.grade.ml_blend` gives the model weight only in proportion to
  that out-of-sample evidence; a model with no metadata, or trained on a
  different feature list, is ignored instead of silently mis-predicting.
"""
from __future__ import annotations

import contextlib
import json
import logging
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import norm

from ..config import FEATURE_NAMES, FORWARD_WINDOW_DAYS, HORIZONS, PROJECT_ROOT, Horizon

logger = logging.getLogger(__name__)

# Minimum distinct snapshot dates before training is attempted. Kept below
# `daily_history_days`: maintenance thins older daily snapshots to weekly, so
# a 60-date gate would have kept the ranker off for months (a live deep run
# found 50 dates). Whether the model gets any WEIGHT is decided separately,
# by its purged out-of-sample IC (pipeline.grade.ml_blend).
COLD_START_MIN_DAYS = 30
MIN_LABELLED_ROWS = 500
MIN_VALIDATION_DATES = 5
MODEL_DIR = PROJECT_ROOT / "data" / "models"


def _unique_snapshot_days(snaps: pd.DataFrame) -> int:
    if snaps.empty:
        return 0
    return int(snaps["as_of"].nunique())


def _gauss_rank_by_date(df: pd.DataFrame, col: str) -> pd.Series:
    r = df.groupby("date")[col].rank(method="average")
    n = df.groupby("date")[col].transform("count")
    p = ((r - 0.5) / n).clip(1e-4, 1 - 1e-4)
    return pd.Series(norm.ppf(p), index=df.index)


def _labelled_panel(horizon: Horizon) -> pd.DataFrame:
    from .features import load_feature_snapshots
    from .grade import _attach_returns, forward_returns

    snaps = load_feature_snapshots()
    if snaps.empty or _unique_snapshot_days(snaps) < COLD_START_MIN_DAYS:
        return pd.DataFrame()
    since = pd.to_datetime(snaps["as_of"]).min().date() - timedelta(days=7)
    fwd = forward_returns(snaps["ticker"].unique().tolist(), FORWARD_WINDOW_DAYS[horizon], since)
    panel = _attach_returns(snaps[["ticker", "as_of", *FEATURE_NAMES]], fwd)
    if panel.empty:
        return panel
    counts = panel.groupby("date")["fwd"].transform("count")
    panel = panel[counts >= 20].copy()
    panel["y"] = _gauss_rank_by_date(panel, "fwd")
    return panel.sort_values("date").reset_index(drop=True)


def _daily_ic(df: pd.DataFrame, pred_col: str) -> list[float]:
    out = []
    for _, g in df.groupby("date"):
        if len(g) >= 20 and g[pred_col].nunique() > 2:
            rho = np.corrcoef(g[pred_col].rank(), g["fwd"].rank())[0, 1]
            if np.isfinite(rho):
                out.append(float(rho))
    return out


def train(horizon: Horizon) -> Path | None:
    """Train one horizon. Returns the saved model path, or None if skipped."""
    panel = _labelled_panel(horizon)
    if panel.empty or len(panel) < MIN_LABELLED_ROWS:
        logger.info("ml_rank[%s]: cold start (%d labelled rows)", horizon, len(panel))
        return None
    try:
        import lightgbm as lgb
    except ImportError:
        logger.warning("lightgbm not installed; skipping training")
        return None

    dates = np.sort(panel["date"].unique())
    h = FORWARD_WINDOW_DAYS[horizon]
    cut = int(len(dates) * 0.75)
    train_dates = dates[: max(cut - h, 0)]   # embargo: drop h dates before validation
    val_dates = dates[cut:]
    if len(train_dates) < 10 or len(val_dates) < MIN_VALIDATION_DATES:
        logger.info("ml_rank[%s]: not enough dates for a purged split (%d train / %d val)",
                    horizon, len(train_dates), len(val_dates))
        return None
    tr = panel[panel["date"].isin(train_dates)]
    va = panel[panel["date"].isin(val_dates)]
    params = {
        "objective": "regression",
        "metric": "l2",
        "learning_rate": 0.03,
        "num_leaves": 15,
        "min_data_in_leaf": 50,
        "feature_fraction": 0.8,
        "bagging_fraction": 0.8,
        "bagging_freq": 5,
        "lambda_l2": 5.0,
        "verbose": -1,
    }
    X_tr = tr[list(FEATURE_NAMES)].astype(float)
    X_va = va[list(FEATURE_NAMES)].astype(float)
    model = lgb.train(
        params,
        lgb.Dataset(X_tr, label=tr["y"]),
        num_boost_round=300,
        valid_sets=[lgb.Dataset(X_va, label=va["y"])],
        callbacks=[lgb.early_stopping(30, verbose=False), lgb.log_evaluation(0)],
    )
    va = va.assign(pred=model.predict(X_va.to_numpy()))
    from .grade import ic_summary

    ic_mean, ic_se, n_dates = ic_summary(_daily_ic(va, "pred"), h)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    path = MODEL_DIR / f"lgb_{horizon}.txt"
    model.save_model(str(path))
    meta = {
        "features": list(FEATURE_NAMES),
        "val_ic": ic_mean,
        "val_ic_se": ic_se,
        "val_dates": n_dates,
        "train_rows": int(len(tr)),
        "embargo_dates": int(h),
        "trained_at": datetime.now(UTC).replace(tzinfo=None).isoformat(timespec="seconds"),
        "target": "gaussian cross-sectional rank of forward return",
    }
    path.with_suffix(".json").write_text(json.dumps(meta, indent=1))
    logger.info("ml_rank[%s]: saved %s (val IC %.4f ± %.4f over %d dates)",
                horizon, path, ic_mean or float("nan"), ic_se or float("nan"), n_dates)
    return path


def train_all() -> dict[Horizon, Path | None]:
    return {h: train(h) for h in HORIZONS}


def model_meta(horizon: Horizon) -> dict | None:
    """Saved validation metadata, or None when the model must not be used."""
    path = MODEL_DIR / f"lgb_{horizon}.json"
    if not path.exists():
        return None
    try:
        meta = json.loads(path.read_text())
    except (OSError, ValueError):
        return None
    if meta.get("features") != list(FEATURE_NAMES):
        return None
    return meta


def _load_model(horizon: Horizon):
    path = MODEL_DIR / f"lgb_{horizon}.txt"
    if not path.exists() or model_meta(horizon) is None:
        return None
    try:
        import lightgbm as lgb

        return lgb.Booster(model_file=str(path))
    except Exception as e:  # noqa: BLE001
        logger.warning("failed to load ml model %s: %s", path, e)
        return None


def score_horizons(features: pd.DataFrame, composite: pd.DataFrame) -> pd.DataFrame:
    """DataFrame[ticker, horizon, ml_score]; cold start / unusable model =
    the composite score (which the blend then weights at zero)."""
    out_rows: list[dict] = []
    for h in HORIZONS:
        sub = composite[composite["horizon"] == h][["ticker", "composite_score"]]
        model = _load_model(h)
        if model is None:
            out_rows.extend(
                {"ticker": r.ticker, "horizon": h, "ml_score": float(r.composite_score)}
                for r in sub.itertuples(index=False)
            )
            continue
        X = features.set_index("ticker").reindex(sub["ticker"])[list(FEATURE_NAMES)].astype(float)
        preds = model.predict(X.to_numpy())
        out_rows.extend(
            {"ticker": t, "horizon": h, "ml_score": float(p)} for t, p in zip(sub["ticker"], preds)
        )
    return pd.DataFrame(out_rows, columns=["ticker", "horizon", "ml_score"])


def last_trained() -> date | None:
    stamps = []
    for h in HORIZONS:
        meta = model_meta(h)
        if meta and meta.get("trained_at"):
            with contextlib.suppress(ValueError):
                stamps.append(datetime.fromisoformat(meta["trained_at"]).date())
    return max(stamps) if stamps else None
