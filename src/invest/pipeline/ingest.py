"""Orchestrate all data sources, tolerating individual source failures."""
from __future__ import annotations

import logging
from collections.abc import Callable
from datetime import date

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

    # Finnhub + FMP both self-skip when their API keys are unset; we always
    # register them so the dashboard's Sources & freshness page lists every
    # source we'd be using if keys were configured, and adding a key later
    # "just works" without code changes.
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


def _tickers_missing_recent_prices(tickers: list[str], lookback_days: int = 7) -> list[str]:
    """Return tickers with no Price rows in the last `lookback_days`. Used to
    decide which symbols to backfill from stooq after yfinance."""
    from datetime import date, timedelta

    from sqlalchemy import select

    from ..db import session_scope
    from ..models import Price

    cutoff = date.today() - timedelta(days=lookback_days)
    with session_scope() as s:
        rows = s.execute(
            select(Price.ticker)
            .where(Price.date >= cutoff, Price.ticker.in_(tickers))
            .distinct()
        ).all()
    have = {r[0] for r in rows}
    return [t for t in tickers if t not in have]


def _run_stooq_backfill(tickers: list[str]) -> int:
    """Only hit stooq for tickers yfinance didn't deliver recent prices for.

    Keeps stooq traffic low while ensuring the rank output is never empty due
    to a bad yfinance run.
    """
    from ..sources.stooq_src import StooqSource

    missing = _tickers_missing_recent_prices(tickers)
    if not missing:
        return 0
    logger.info("stooq backfill: %d tickers yfinance missed", len(missing))
    return StooqSource().run(missing)


def _validate_consensus_agreement(tickers: list[str], max_pct_diff: float = 0.25) -> int:
    """Compare mean_target across sources on the same as_of_date. Logs (and
    writes a `run_log` row via log_run) when two sources disagree by more
    than ``max_pct_diff``. Returns the number of flagged tickers."""
    from datetime import date

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
    # After all sources have written, sanity-check that the consensus snapshots
    # agree where we have multiple opinions. Disagreements are logged but never
    # abort the ingest.
    try:
        _validate_consensus_agreement(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("consensus validation failed")
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
    """The `limit` tickers whose consensus snapshot is oldest (never-fetched
    tickers first).

    Drives the rolling refresh: each hourly run tops up a slice of the
    universe, so over a day everything cycles without any single run
    blowing its timeout.
    """
    from sqlalchemy import func, select

    from ..db import session_scope
    from ..models import Consensus

    if limit <= 0 or not tickers:
        return []
    with session_scope() as s:
        rows = s.execute(
            select(Consensus.ticker, func.max(Consensus.as_of_date))
            .where(Consensus.ticker.in_(tickers))
            .group_by(Consensus.ticker)
        ).all()
    newest = {t: d for t, d in rows}
    # Tickers with no consensus at all sort first (date.min), then oldest-first.
    ordered = sorted(tickers, key=lambda t: (newest.get(t) or date.min, t))
    return ordered[:limit]


def ingest_fast(tickers: list[str] | None = None) -> int:
    """Fast path for the hourly loop: prices + a full coverage sweep.

    Upside = target / last_close − 1, so refreshing prices moves the
    denominator every hour and refreshing consensus moves the numerator.
    Both have to happen for predictions to genuinely change hourly.

    The sweep walks the WHOLE universe (stalest first) gathering consensus,
    price targets and named rating actions in a single pass per symbol, under
    a wall-clock budget. Earlier versions capped this at a fixed 60-ticker
    slice, which meant a restored-from-empty database had analyst coverage for
    only 20 % of the universe — not enough for anything to clear the coverage
    gate. Stalest-first ordering means a budget-truncated sweep still cycles
    the full universe across consecutive runs.
    """
    tickers = tickers or current_universe()
    from ..config import get_settings
    from ..sources.yfinance_src import YFinanceSource

    settings = get_settings()
    src = YFinanceSource()
    total = 0
    with log_run("yfinance.prices_fast") as c:
        c["rows"] = src.ingest_prices(tickers)
        total += c["rows"]
    try:
        total += _run_stooq_backfill(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("stooq backfill failed")

    batch = stalest_tickers(tickers, settings.coverage_sweep_max or len(tickers))
    if batch:
        logger.info(
            "coverage sweep: %d of %d tickers (stalest first, %.0fs budget)",
            len(batch), len(tickers), settings.coverage_budget_seconds,
        )
        try:
            with log_run("yfinance.coverage_sweep") as c:
                rows, processed = src.ingest_coverage(
                    batch, budget_seconds=settings.coverage_budget_seconds
                )
                c["rows"] = rows
                total += rows
                logger.info(
                    "coverage sweep wrote %d rows across %d/%d tickers",
                    rows, processed, len(batch),
                )
        except Exception:  # noqa: BLE001
            logger.exception("coverage sweep failed")
    return total
