"""Orchestrate all data sources, tolerating individual source failures."""
from __future__ import annotations

import logging
from collections.abc import Callable

from ..config import get_settings
from ..sources.base import log_run
from ..universe import current_universe

logger = logging.getLogger(__name__)


def _available_sources() -> list[Callable[[list[str]], int]]:
    """Return each source's `run` method. Imports are lazy so one missing dep
    doesn't break the others."""
    runners: list[Callable[[list[str]], int]] = []
    settings = get_settings()

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

    if settings.finnhub_api_key:
        try:
            from ..sources.finnhub_src import FinnhubSource

            runners.append(FinnhubSource().run)
        except Exception as e:  # noqa: BLE001
            logger.warning("finnhub source unavailable: %s", e)

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


def ingest_fast(tickers: list[str] | None = None) -> int:
    """Fast path for the every-20-min loop.

    Runs yfinance prices + consensus, then uses stooq to backfill any tickers
    yfinance missed. Skips fundamentals (slow .info calls), Finnhub, and EDGAR
    so the cycle comfortably fits in 20 minutes.
    """
    tickers = tickers or current_universe()
    from ..sources.yfinance_src import YFinanceSource

    src = YFinanceSource()
    total = 0
    with log_run("yfinance.prices_fast") as c:
        c["rows"] = src.ingest_prices(tickers)
        total += c["rows"]
    with log_run("yfinance.consensus_fast") as c:
        c["rows"] = src.ingest_consensus(tickers)
        total += c["rows"]
    # stooq backfill for anything yfinance missed.
    try:
        total += _run_stooq_backfill(tickers)
    except Exception:  # noqa: BLE001
        logger.exception("stooq backfill failed")
    return total
