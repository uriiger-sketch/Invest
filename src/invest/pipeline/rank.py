"""Blend composite + ML scores and persist the top-N per horizon."""
from __future__ import annotations

import logging
from datetime import date

import numpy as np
import pandas as pd
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..config import HORIZONS, get_settings
from ..db import session_scope
from ..models import Score
from . import ml_rank, score
from .features import build_features

logger = logging.getLogger(__name__)


class RankingProducedNothingError(RuntimeError):
    """Raised when the quality gates reject every single ticker.

    This is always a bug or a mis-calibrated threshold, never a normal
    outcome: if it were normal, the app would have nothing to publish.
    Raising (instead of returning empty) makes the workflow fail loudly and
    leaves the previous good report in place, rather than silently going
    stale for weeks.
    """


class InsufficientAnalystDataError(RuntimeError):
    """Raised when the analyst tables are too empty to rank meaningfully.

    Guards against the case where the database was lost/reset and the
    pipeline would otherwise "rank" everything on no data at all.
    """


def _zscore_group(df: pd.DataFrame, col: str) -> pd.Series:
    g = df.groupby("horizon")[col]
    return (df[col] - g.transform("mean")) / g.transform("std").replace(0, np.nan)


def _assert_analyst_data_present(features: pd.DataFrame, min_covered_pct: float = 0.10) -> None:
    """Refuse to rank when almost nothing has analyst coverage.

    If the DB was wiped (cache eviction, fresh checkout) the consensus table
    is empty, every `num_analysts` is 0, and ranking would be meaningless.
    Better to fail the run and keep the last good report than to publish
    noise.

    The bar is a FRACTION of the universe, not an absolute count: a small
    universe (tests, a focused watchlist) is legitimate, whereas "0 % of
    2,000 tickers have consensus" is always a broken ingest.
    """
    if "num_analysts" not in features.columns:
        raise InsufficientAnalystDataError(
            "features frame has no num_analysts column — consensus ingest never ran"
        )
    total = len(features)
    covered = int((pd.to_numeric(features["num_analysts"], errors="coerce").fillna(0) > 0).sum())
    if covered == 0 or (total and covered / total < min_covered_pct):
        raise InsufficientAnalystDataError(
            f"only {covered} of {total} tickers have any analyst coverage "
            f"(need >= {min_covered_pct:.0%}). The consensus tables look empty — "
            "run a deep ingest before ranking."
        )
    logger.info(
        "analyst coverage check: %d/%d tickers (%.0f%%) have consensus",
        covered, total, 100 * covered / max(total, 1),
    )


def rank_all(tickers: list[str]) -> pd.DataFrame:
    """End-to-end: build features, score (composite + ML), blend, persist, return frame."""
    settings = get_settings()
    features = build_features(tickers)
    if features.empty:
        logger.warning("no features built; nothing to rank")
        return pd.DataFrame()

    _assert_analyst_data_present(features)

    comp = score.composite_scores(features)
    if comp.empty:
        # A gate rejected the ENTIRE universe. This used to be a bland warning
        # that blamed the wrong gate and returned quietly, so the workflow
        # stayed green while nothing was ever persisted again. Now we report
        # exactly which gate is responsible and raise, so the run fails
        # visibly and the last good report is left untouched.
        counts = score.gate_survivors(features)
        detail = ", ".join(f"{k}={v}" for k, v in counts.items())
        logger.error(
            "RANKING PRODUCED NOTHING: every one of %d tickers was rejected. "
            "Per-gate survivors: %s. Check the thresholds in config.py against "
            "these numbers — a gate whose survivor count is 0 is the culprit.",
            counts["universe"], detail,
        )
        raise RankingProducedNothingError(
            f"all {counts['universe']} tickers rejected by quality gates ({detail})"
        )

    ml = ml_rank.score_horizons(features, comp)
    merged = comp.merge(ml, on=["ticker", "horizon"], how="left")
    merged["ml_score"] = merged["ml_score"].fillna(merged["composite_score"])

    merged["composite_z"] = _zscore_group(merged, "composite_score").fillna(0.0)
    merged["ml_z"] = _zscore_group(merged, "ml_score").fillna(0.0)
    merged["blended_score"] = (
        settings.blend_composite_weight * merged["composite_z"]
        + settings.blend_ml_weight * merged["ml_z"]
    )

    merged["percentile"] = merged.groupby("horizon")["blended_score"].rank(pct=True)
    merged["as_of"] = date.today()

    _persist(merged)
    return merged


def _persist(df: pd.DataFrame) -> None:
    rows = df[
        ["ticker", "horizon", "as_of", "composite_score", "ml_score", "blended_score", "percentile"]
    ].to_dict("records")
    if not rows:
        return
    with session_scope() as s:
        stmt = sqlite_insert(Score).values(rows)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker", "horizon", "as_of"],
            set_={
                "composite_score": stmt.excluded.composite_score,
                "ml_score": stmt.excluded.ml_score,
                "blended_score": stmt.excluded.blended_score,
                "percentile": stmt.excluded.percentile,
            },
        )
        s.execute(stmt)


def select_diversified(rows: list[dict], n: int, max_per_sector: int | None = None) -> list[dict]:
    """Greedy top-N selection with a per-sector concentration cap.

    `rows` must be sorted best-first and each dict may carry a "sector" key.
    With the cap (default from settings, 0 = disabled) an all-semiconductor
    market can't fill an entire top list — once a sector hits the cap, the
    next-best name from any other sector takes the slot. Unknown/missing
    sectors are treated as their own bucket so they're capped too.
    """
    settings = get_settings()
    cap = settings.max_per_sector if max_per_sector is None else max_per_sector
    if cap <= 0:
        return rows[:n]
    picked: list[dict] = []
    sector_counts: dict[str, int] = {}
    for r in rows:
        if len(picked) >= n:
            break
        sector = (r.get("sector") or "?").strip() or "?"
        if sector_counts.get(sector, 0) >= cap:
            continue
        picked.append(r)
        sector_counts[sector] = sector_counts.get(sector, 0) + 1
    # If the cap left empty slots (tiny candidate pool), backfill by score.
    if len(picked) < n:
        chosen = {r["ticker"] for r in picked}
        for r in rows:
            if len(picked) >= n:
                break
            if r["ticker"] not in chosen:
                picked.append(r)
    return picked


def top_n(as_of: date | None = None, n: int | None = None) -> dict[str, pd.DataFrame]:
    """Return dict[horizon -> top-N DataFrame] from persisted scores.

    Fetches a deep candidate pool (4×n) and applies the per-sector
    diversification cap before final ranking.
    """
    from ..models import Stock

    settings = get_settings()
    n = n or settings.top_n
    as_of = as_of or date.today()
    out: dict[str, pd.DataFrame] = {}
    with session_scope() as s:
        for h in HORIZONS:
            rows = (
                s.query(Score, Stock.sector)
                .outerjoin(Stock, Stock.ticker == Score.ticker)
                .filter(Score.horizon == h, Score.as_of == as_of)
                .order_by(Score.blended_score.desc())
                .limit(n * 4)
                .all()
            )
            candidates = [
                {
                    "ticker": r.Score.ticker,
                    "sector": r.sector,
                    "blended_score": r.Score.blended_score,
                    "composite_score": r.Score.composite_score,
                    "ml_score": r.Score.ml_score,
                    "percentile": r.Score.percentile,
                }
                for r in rows
            ]
            picked = select_diversified(candidates, n)
            out[h] = pd.DataFrame(
                [
                    {
                        "rank": i + 1,
                        "ticker": r["ticker"],
                        "blended_score": r["blended_score"],
                        "composite_score": r["composite_score"],
                        "ml_score": r["ml_score"],
                        "percentile": r["percentile"],
                    }
                    for i, r in enumerate(picked)
                ]
            )
    return out
