"""Light ML ranker: LightGBM regressors per horizon with cold-start fallback.

Training data comes from persisted FeatureSnapshot + Price history. Until we have
enough snapshots (see COLD_START_MIN_DAYS), the ML score falls back to the
composite score so the blended score is well-defined from day one.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

import pandas as pd
from sqlalchemy import select

from ..config import FEATURE_NAMES, FORWARD_WINDOW_DAYS, HORIZONS, PROJECT_ROOT, Horizon
from ..db import session_scope
from ..models import FeatureSnapshot, Price

logger = logging.getLogger(__name__)

COLD_START_MIN_DAYS = 60
# Rooted at PROJECT_ROOT rather than a bare relative path: a relative
# "data/models" resolves against whatever the CURRENT WORKING DIRECTORY
# happens to be when `train()`/`_load_model()` run, which is fragile outside
# the one context (repo root) it was implicitly assumed to always run from.
MODEL_DIR = PROJECT_ROOT / "data" / "models"


def _load_snapshots() -> pd.DataFrame:
    with session_scope() as s:
        rows = s.execute(select(FeatureSnapshot)).scalars().all()
    if not rows:
        return pd.DataFrame()
    records: list[dict] = []
    for r in rows:
        try:
            data = json.loads(r.feature_json)
        except Exception:  # noqa: BLE001
            continue
        rec = {"ticker": r.ticker, "as_of": r.as_of}
        rec.update({k: data.get(k) for k in FEATURE_NAMES})
        records.append(rec)
    return pd.DataFrame(records)


def _load_forward_returns(tickers: list[str], horizon_days: int) -> pd.DataFrame:
    """For each (ticker, date), compute (close_{date+N} / close_date - 1)."""
    with session_scope() as s:
        rows = s.execute(
            select(Price).where(Price.ticker.in_(tickers))
        ).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "as_of", "fwd_ret"])
    df = pd.DataFrame(
        [{"ticker": r.ticker, "date": r.date, "close": r.close} for r in rows]
    )
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(["ticker", "date"])
    df["fwd_close"] = df.groupby("ticker")["close"].shift(-horizon_days)
    df["fwd_ret"] = df["fwd_close"] / df["close"] - 1
    return df[["ticker", "date", "fwd_ret"]].rename(columns={"date": "as_of"})


def _unique_snapshot_days(snaps: pd.DataFrame) -> int:
    if snaps.empty:
        return 0
    return int(snaps["as_of"].nunique())


def train(horizon: Horizon) -> Path | None:
    """Train LightGBM for one horizon. Returns saved model path or None if skipped."""
    snaps = _load_snapshots()
    if _unique_snapshot_days(snaps) < COLD_START_MIN_DAYS:
        logger.info("ml_rank[%s]: cold start (only %d days of snapshots)", horizon, _unique_snapshot_days(snaps))
        return None

    tickers = snaps["ticker"].unique().tolist()
    fwd = _load_forward_returns(tickers, FORWARD_WINDOW_DAYS[horizon])
    snaps["as_of"] = pd.to_datetime(snaps["as_of"])
    data = snaps.merge(fwd, on=["ticker", "as_of"], how="inner").dropna(subset=["fwd_ret"])
    if len(data) < 500:
        logger.info("ml_rank[%s]: insufficient labelled rows (%d)", horizon, len(data))
        return None

    try:
        import lightgbm as lgb
    except ImportError:
        logger.warning("lightgbm not installed; skipping training")
        return None

    # Chronological order is required for the walk-forward split below: rows
    # come back from `_load_snapshots` in DB insertion order (unordered with
    # respect to `as_of`), so slicing 80/20 without sorting first could put
    # NEWER rows in the training set and OLDER rows in validation — silent
    # look-ahead leakage into the metric used for early stopping.
    data = data.sort_values("as_of").reset_index(drop=True)
    X = data[list(FEATURE_NAMES)].astype(float).fillna(0.0)
    y = data["fwd_ret"].astype(float)

    # Simple walk-forward: last 20% (chronologically) is validation.
    cut = int(len(data) * 0.8)
    d_train = lgb.Dataset(X.iloc[:cut], label=y.iloc[:cut])
    d_val = lgb.Dataset(X.iloc[cut:], label=y.iloc[cut:])
    params = {
        "objective": "regression",
        "metric": "rmse",
        "learning_rate": 0.05,
        "num_leaves": 31,
        "min_data_in_leaf": 20,
        "feature_fraction": 0.9,
        "bagging_fraction": 0.9,
        "bagging_freq": 5,
        "verbose": -1,
    }
    model = lgb.train(
        params,
        d_train,
        num_boost_round=400,
        valid_sets=[d_val],
        callbacks=[lgb.early_stopping(20), lgb.log_evaluation(0)],
    )
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    path = MODEL_DIR / f"lgb_{horizon}.txt"
    model.save_model(str(path))
    logger.info("ml_rank[%s]: saved model -> %s", horizon, path)
    return path


def train_all() -> dict[Horizon, Path | None]:
    return {h: train(h) for h in HORIZONS}


def _load_model(horizon: Horizon):
    path = MODEL_DIR / f"lgb_{horizon}.txt"
    if not path.exists():
        return None
    try:
        import lightgbm as lgb

        return lgb.Booster(model_file=str(path))
    except Exception as e:  # noqa: BLE001
        logger.warning("failed to load ml model %s: %s", path, e)
        return None


def score_horizons(features: pd.DataFrame, composite: pd.DataFrame) -> pd.DataFrame:
    """Return DataFrame[ticker, horizon, ml_score]. Cold-start = composite."""
    out_rows: list[dict] = []
    for h in HORIZONS:
        model = _load_model(h)
        if model is None:
            # Cold-start fallback: ml_score := composite_score
            sub = composite[composite["horizon"] == h][["ticker", "composite_score"]]
            for _, r in sub.iterrows():
                out_rows.append(
                    {"ticker": r["ticker"], "horizon": h, "ml_score": float(r["composite_score"])}
                )
            continue
        X = features[list(FEATURE_NAMES)].astype(float).fillna(0.0)
        preds = model.predict(X.values)
        for ticker, p in zip(features["ticker"], preds):
            out_rows.append({"ticker": ticker, "horizon": h, "ml_score": float(p)})
    return pd.DataFrame(out_rows)
