"""Orchestrate all data sources, tolerating individual source failures.

Every crawl stage is bounded (wall-clock budget, rate governor, circuit
breakers) and ordered so that a truncated stage still makes progress:
  * dormant tickers (no price for `dormant_after_days`) are skipped by every
    per-ticker stage — they used to cost retries on every run, and through
    the stooq fallback they killed whole runs;
  * the "focus list" — names currently on, or just below, the published
    table — gets the expensive per-company intel (Google News, SEC filing
    stream) on EVERY run;
  * the Yahoo sweep walks the universe stalest-first by last-crawl
    TIMESTAMP (date resolution let the same alphabetical tail starve when
    several runs happen per day).
"""
from __future__ import annotations

import logging
from collections.abc import Callable
from datetime import date, datetime, timedelta

from ..sources.base import log_run
from ..universe import current_universe

logger = logging.getLogger(__name__)


def _available_sources() -> list[Callable[[list[str]], int]]:
    """Return each source's `run` method. Imports are lazy so one missing dep
    doesn't break the others."""
    runners: list[Callable[[list[str]], int]] = []

    try:
        from ..sources.yfinance_src import YFinanceSource

        runners.append(YFinanceSource().run)
    except Exception as e:  # noqa: BLE001
        logger.warning("yfinance source unavailable: %s", e)

    # Stooq runs after yfinance and only backfills prices for tickers yfinance
    # missed. See `_run_stooq_backfill` below.
    try:
        from ..sources.stooq_src import StooqSource  # noqa: F401

        runners.append(_run_stooq_backfill)
    except Exception as e:  # noqa: BLE001
        logger.warning("stooq source unavailable: %s", e)

    runners.append(_run_focus_news)

    # Finnhub + FMP both self-skip when their API keys are unset; we always
    # register them so adding a key later "just works" without code changes.
    try:
        from ..sources.finnhub_src import FinnhubSource

        runners.append(FinnhubSource().run)
    except Exception as e:  # noqa: BLE001
        logger.warning("finnhub source unavailable: %s", e)
    try:
        from ..sources.fmp_src import FmpSource

        runners.append(FmpSource().run)
    except Exception as e:  # noqa: BLE001
        logger.warning("fmp source unavailable: %s", e)

    try:
        from ..sources.edgar_src import EdgarSource

        runners.append(EdgarSource().run)
    except Exception as e:  # noqa: BLE001
        logger.warning("edgar source unavailable: %s", e)

    return runners


# ------------------------------ ticker sets ------------------------------


def _newest_price_dates(tickers: list[str]) -> dict[str, date]:
    from sqlalchemy import func, select

    from ..db import session_scope
    from ..models import Price

    with session_scope() as s:
        rows = s.execute(
            select(Price.ticker, func.max(Price.date))
            .where(Price.ticker.in_(tickers), Price.close.isnot(None))
            .group_by(Price.ticker)
        ).all()
    return {t: d for t, d in rows if d is not None}


def dormant_tickers(tickers: list[str]) -> list[str]:
    """Tickers with no price for `dormant_after_days` (delisted / renamed /
    acquired), or never priced at all.

    Evaluated relative to the freshest price in the set rather than to
    today, so a weekend or an exchange holiday never marks the whole
    universe dormant.
    """
    from ..config import get_settings

    newest = _newest_price_dates(tickers)
    if not newest:
        return []  # empty database: nothing is known to be dead yet
    reference = max(newest.values())
    limit = reference - timedelta(days=get_settings().dormant_after_days)
    return [t for t in tickers if newest.get(t) is None or newest[t] < limit]


def active_tickers(tickers: list[str]) -> list[str]:
    dead = set(dormant_tickers(tickers))
    if dead:
        logger.info("skipping %d dormant tickers (no price in %d d): %s",
                    len(dead), _dormant_days(), ", ".join(sorted(dead)[:40]))
    return [t for t in tickers if t not in dead]


def _dormant_days() -> int:
    from ..config import get_settings

    return get_settings().dormant_after_days


def focus_tickers(limit: int) -> list[str]:
    """Names on (or near) the published table: the latest grades first, then
    the top of each horizon's latest scores. Empty on a fresh database."""
    from sqlalchemy import desc, select

    from ..config import HORIZONS
    from ..db import session_scope
    from ..models import Grade, Score

    out: list[str] = []
    seen: set[str] = set()

    def add(t: str) -> None:
        if t not in seen and len(out) < limit:
            seen.add(t)
            out.append(t)

    with session_scope() as s:
        latest_g = s.execute(select(Grade.as_of).order_by(desc(Grade.as_of)).limit(1)).scalar()
        if latest_g is not None:
            for (t,) in s.execute(
                select(Grade.ticker).where(Grade.as_of == latest_g)
                .order_by(desc(Grade.grade_score)).limit(limit)
            ).all():
                add(t)
        latest_s = s.execute(select(Score.as_of).order_by(desc(Score.as_of)).limit(1)).scalar()
        if latest_s is not None:
            per_h = max(1, limit // max(1, len(HORIZONS)))
            for h in HORIZONS:
                for (t,) in s.execute(
                    select(Score.ticker).where(Score.as_of == latest_s, Score.horizon == h)
                    .order_by(desc(Score.blended_score)).limit(per_h)
                ).all():
                    add(t)
    return out


def _tickers_missing_recent_prices(tickers: list[str], lookback_days: int = 7) -> list[str]:
    """Tickers with no Price rows in the last `lookback_days`."""
    newest = _newest_price_dates(tickers)
    cutoff = date.today() - timedelta(days=lookback_days)
    return [t for t in tickers if newest.get(t) is None or newest[t] < cutoff]


def stooq_candidates(tickers: list[str]) -> list[str]:
    """Recently-live US tickers whose price is now missing.

    Only names priced within the last 30 days but not in the last 3 are
    worth a fallback request: anything older is dormant (no fallback will
    revive a delisted symbol), anything newer is fine.
    """
    newest = _newest_price_dates(tickers)
    today = date.today()
    out = []
    for t in tickers:
        d = newest.get(t)
        if "." in t or d is None:
            continue
        if timedelta(days=3) < (today - d) <= timedelta(days=30):
            out.append(t)
    return out


def _run_stooq_backfill(tickers: list[str]) -> int:
    """Hit stooq only for recently-live tickers yfinance missed this run."""
    from ..sources.stooq_src import StooqSource

    missing = stooq_candidates(tickers)
    if not missing:
        return 0
    logger.info("stooq backfill: %d recently-live tickers yfinance missed", len(missing))
    return StooqSource().run(missing)


def _run_focus_news(tickers: list[str]) -> int:
    """Google News for the focus list (falls back to the first slice of the
    active universe on a fresh database)."""
    from ..config import get_settings
    from ..sources.news_src import GoogleNewsSource

    settings = get_settings()
    focus = [t for t in focus_tickers(settings.focus_size) if t in set(tickers)]
    if not focus:
        focus = active_tickers(tickers)[: settings.focus_size]
    return GoogleNewsSource().run(focus)


def _run_focus_filings(tickers: list[str]) -> int:
    from ..config import get_settings
    from ..sources.edgar_src import EdgarSource

    settings = get_settings()
    focus = [t for t in focus_tickers(settings.focus_size) if t in set(tickers)]
    if not focus:
        return 0
    with log_run("edgar.filings_focus") as c:
        c["rows"] = EdgarSource().ingest_filings(focus, budget_seconds=settings.sec_budget_seconds)
        return c["rows"]


def _validate_consensus_agreement(tickers: list[str], max_pct_diff: float = 0.25) -> int:
    """Compare mean_target across sources on the same as_of_date. Logs (and
    writes a `run_log` row via log_run) when two sources disagree by more
    than ``max_pct_diff``. Returns the number of flagged tickers."""
    from sqlalchemy import select

    from ..db import session_scope
    from ..models import Consensus

    today = date.today()
    flagged = 0
    with log_run("validate.consensus_agreement") as c:
        with session_scope() as s:
            rows = s.execute(
                select(
                    Consensus.ticker, Consensus.source, Consensus.mean_target
                ).where(
                    Consensus.ticker.in_(tickers),
                    Consensus.as_of_date == today,
                    Consensus.mean_target.isnot(None),
                )
            ).all()
        by_ticker: dict[str, dict[str, float]] = {}
        for ticker, source, mt in rows:
            by_ticker.setdefault(ticker, {})[source] = float(mt)
        for ticker, by_src in by_ticker.items():
            if len(by_src) < 2:
                continue
            targets = list(by_src.values())
            lo, hi = min(targets), max(targets)
            if lo > 0 and (hi - lo) / lo > max_pct_diff:
                logger.warning(
                    "consensus disagreement on %s: sources=%s targets=%s",
                    ticker, list(by_src.keys()), targets,
                )
                flagged += 1
        c["rows"] = flagged
    return flagged


def _record_dormant(tickers: list[str]) -> None:
    """Persist the dormant list in run_log so the report's data-health
    section can name the symbols that need replacing."""
    dead = dormant_tickers(tickers)
    with log_run("universe.dormant") as c:
        c["rows"] = len(dead)
    if dead:
        from ..db import session_scope
        from ..models import RunLog

        with session_scope() as s:
            row = s.query(RunLog).filter(RunLog.job == "universe.dormant").order_by(
                RunLog.id.desc()
            ).first()
            if row is not None:
                row.error = "dormant: " + ", ".join(sorted(dead))


def ingest_all(tickers: list[str] | None = None) -> int:
    tickers = tickers or current_universe()
    logger.info("ingest starting for %d tickers", len(tickers))
    total = 0
    for runner in _available_sources():
        try:
            total += runner(tickers)
        except Exception:  # noqa: BLE001
            logger.exception("source runner failed")
            continue
    try:
        _validate_consensus_agreement(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("consensus validation failed")
    try:
        _record_dormant(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("dormant bookkeeping failed")
    logger.info("ingest finished, total rows written: %d", total)
    return total


def ingest_prices_only(tickers: list[str] | None = None) -> int:
    """Faster intraday loop used by the scheduler during market hours."""
    tickers = tickers or current_universe()
    from ..sources.yfinance_src import YFinanceSource

    src = YFinanceSource()
    with log_run("yfinance.prices_intraday") as c:
        c["rows"] = src.ingest_prices(tickers)
        return c["rows"]


def stalest_tickers(tickers: list[str], limit: int) -> list[str]:
    """The `limit` tickers whose intel was crawled longest ago (never-crawled
    first). Uses the intel snapshot TIMESTAMP when present, falling back to
    the consensus date for databases that predate it."""
    from sqlalchemy import func, select

    from ..db import session_scope
    from ..models import Consensus, IntelSnapshot

    if limit <= 0 or not tickers:
        return []
    with session_scope() as s:
        cons = s.execute(
            select(Consensus.ticker, func.max(Consensus.as_of_date))
            .where(Consensus.ticker.in_(tickers))
            .group_by(Consensus.ticker)
        ).all()
        intel = s.execute(
            select(IntelSnapshot.ticker, IntelSnapshot.as_of).where(
                IntelSnapshot.ticker.in_(tickers), IntelSnapshot.kind == "quote"
            )
        ).all()
    newest: dict[str, datetime] = {
        t: datetime.combine(d, datetime.min.time()) for t, d in cons if d is not None
    }
    for t, ts in intel:
        if ts is not None and (t not in newest or ts > newest[t]):
            newest[t] = ts
    ordered = sorted(tickers, key=lambda t: (newest.get(t) or datetime.min, t))
    return ordered[:limit]


def ingest_fast(tickers: list[str] | None = None) -> int:
    """Fast path for the scheduled loop.

    1. bulk prices (cheap: 40 symbols per request, every ticker);
    2. stooq backfill for recently-live names yfinance just missed;
    3. the Yahoo intel sweep over every ACTIVE ticker, stalest first, under
       a wall-clock budget — consensus, price targets, per-firm rating AND
       target changes, EPS revisions, earnings surprises, key stats, news;
    4. Google News + the SEC filing stream for the focus list.
    """
    tickers = tickers or current_universe()
    from ..config import get_settings
    from ..sources.yfinance_src import YFinanceSource

    settings = get_settings()
    src = YFinanceSource()
    total = 0
    with log_run("yfinance.prices_fast") as c:
        c["rows"] = src.ingest_prices(tickers, period=settings.fast_price_period)
        total += c["rows"]
    try:
        total += _run_stooq_backfill(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("stooq backfill failed")

    live = active_tickers(tickers)
    batch = stalest_tickers(live, settings.coverage_sweep_max or len(live))
    if batch:
        logger.info(
            "coverage sweep: %d of %d active tickers (stalest first, %.0fs budget, %d workers)",
            len(batch), len(live), settings.coverage_budget_seconds, settings.crawl_workers,
        )
        try:
            with log_run("yfinance.coverage_sweep") as c:
                rows, processed = src.ingest_coverage(
                    batch, budget_seconds=settings.coverage_budget_seconds
                )
                c["rows"] = rows
                total += rows
        except Exception:  # noqa: BLE001
            logger.exception("coverage sweep failed")
    for stage in (_run_focus_news, _run_focus_filings):
        try:
            total += stage(live)
        except Exception:  # noqa: BLE001
            logger.exception("%s failed", stage.__name__)
    try:
        _record_dormant(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("dormant bookkeeping failed")
    return total
