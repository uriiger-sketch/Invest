"""Minimal rank-vs-return backtest. Not a full event-driven simulator.

For each ticker in the universe, build daily feature snapshots from stored
prices + latest consensus, then measure Spearman rank correlation between
today's composite score and forward returns at the three horizons. Use this as
a sanity check on the weight matrix before trusting the live ranker.
"""
from __future__ import annotations

import logging
from datetime import date

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sqlalchemy import select

from invest.config import FORWARD_WINDOW_DAYS, HORIZONS
from invest.db import session_scope
from invest.models import Price
from invest.pipeline.features import build_features
from invest.pipeline.score import composite_scores
from invest.universe import current_universe

logger = logging.getLogger(__name__)


def _close_frame(tickers: list[str]) -> pd.DataFrame:
    with session_scope() as s:
        rows = s.execute(select(Price).where(Price.ticker.in_(tickers))).scalars().all()
    df = pd.DataFrame([{"ticker": r.ticker, "date": r.date, "close": r.close} for r in rows])
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values(["ticker", "date"])


def run(as_of: date | None = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    _ = as_of  # reserved for historical replay; the current implementation uses today's closes
    tickers = current_universe()

    features = build_features(tickers)
    comp = composite_scores(features)
    closes = _close_frame(tickers)

    # Build a map ticker -> close series
    grp = closes.groupby("ticker")

    for h in HORIZONS:
        w = FORWARD_WINDOW_DAYS[h]
        rows: list[tuple[float, float]] = []
        sub = comp[comp["horizon"] == h][["ticker", "composite_score"]]
        for _, r in sub.iterrows():
            try:
                cls = grp.get_group(r["ticker"]).sort_values("date")["close"].astype(float).values
            except KeyError:
                continue
            if len(cls) < w + 2:
                continue
            fwd = cls[-1] / cls[-(w + 1)] - 1
            rows.append((float(r["composite_score"]), float(fwd)))
        if len(rows) < 10:
            logger.warning("horizon %s: too few rows (%d) for IC", h, len(rows))
            continue
        arr = np.array(rows)
        ic, p = spearmanr(arr[:, 0], arr[:, 1])
        logger.info("horizon=%s n=%d spearman_IC=%.4f p=%.3g", h, len(rows), ic, p)


if __name__ == "__main__":
    run()
