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
    """Fast path for the every-20-min loop: yfinance prices + consensus.

    Skips fundamentals (slow per-ticker .info calls), Finnhub, and EDGAR so
    the whole cycle comfortably fits under the 20-minute budget.
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
    return total
