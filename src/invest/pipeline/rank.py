"""Blend composite + ML scores and persist the top-N per horizon."""
from __future__ import annotations

import logging
from datetime import date

import pandas as pd
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..config import HORIZONS, get_settings
from ..db import session_scope
from ..models import Score
from . import ml_rank, score
from .features import build_features, persist_feature_snapshot

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
    """Per-horizon z-score, robust median/MAD (via score._zscore) rather than
    mean/std. `score.py` deliberately avoids mean/std because a single
    outlier inflates the std and squashes every legitimate value toward
    zero — the same argument applies here, since `composite_score` and
    `ml_score` both inherit whatever tails survive the upstream feature
    clipping. Every row in `df` has already passed the quality gates (it
    only exists here because `composite_scores` emitted it), so no
    stats-pool restriction is needed — unlike `score._zscore`'s callers.
    """
    return df.groupby("horizon")[col].transform(lambda s: score._zscore(s))


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


def _theme_tilts(tickers: list[str]) -> dict[str, float]:
    """{ticker: additive tilt} — a small bias toward technology.

    Frontier deep-tech (quantum / AI-infrastructure pure plays) gets the
    larger tilt; any other Technology-sector name gets the smaller one. The
    two never compound: a frontier name gets `theme_tilt_frontier`, not
    frontier + tech.

    Sector comes from the `stocks` table, which `seed_stocks_table()`
    populates from the static universe on every run, so this works even
    before yfinance fundamentals have landed.
    """
    from ..models import Stock
    from ..universe import FRONTIER_TECH

    settings = get_settings()
    if not settings.theme_tilt_tech and not settings.theme_tilt_frontier:
        return {}
    with session_scope() as s:
        rows = s.query(Stock.ticker, Stock.sector).filter(Stock.ticker.in_(tickers)).all()
    sectors = {t: (sec or "") for t, sec in rows}
    out: dict[str, float] = {}
    for t in tickers:
        if t in FRONTIER_TECH:
            out[t] = settings.theme_tilt_frontier
        elif sectors.get(t, "").strip().lower() == "technology":
            out[t] = settings.theme_tilt_tech
        else:
            out[t] = 0.0
    return out


def rank_all(tickers: list[str]) -> pd.DataFrame:
    """End-to-end: build features, score (composite + ML), blend, persist, return frame."""
    settings = get_settings()
    features = build_features(tickers)
    if features.empty:
        logger.warning("no features built; nothing to rank")
        return pd.DataFrame()

    # Persist today's feature snapshot for future ML training. This was
    # previously dead code (nothing called it), so the `features` table
    # stayed empty forever, `ml_rank.train()` never cleared its cold-start
    # check, and `ml_score` was silently identical to `composite_score` for
    # every row ever persisted — the composite+ML blend was composite-only.
    try:
        persist_feature_snapshot(features)
    except Exception:  # noqa: BLE001
        logger.exception("persist_feature_snapshot failed; ranking continues without it")

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
    # fillna(0.0) is load-bearing: `_theme_tilts` returns {} when the tilt is
    # switched off in config, and `.map({})` yields all-NaN — without the
    # fill, disabling the tilt would silently NaN out every blended_score.
    merged["theme_tilt"] = (
        merged["ticker"].map(_theme_tilts(merged["ticker"].tolist())).fillna(0.0)
    )
    merged["blended_score"] = merged["blended_score"] + merged["theme_tilt"]

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
        # The backfill above appends capped-out names in their ORIGINAL scan
        # order, which is only correct if it happens to land after every
        # diversified pick. It doesn't in general: a capped-out name can
        # score higher than a later diversified pick from a still-open
        # sector, so appending it at the end displayed it at a WORSE rank
        # than its score deserved. Re-sorting by score after backfill fixes
        # display order without touching which names got selected (the cap
        # logic above already decided that).
        picked.sort(key=lambda r: -(r.get("blended_score") or 0.0))
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
