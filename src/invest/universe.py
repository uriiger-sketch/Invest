"""Universe of tickers to track.

We keep a static fallback list so the system works offline. `refresh_universe()`
pulls the current S&P 500 and NASDAQ-100 membership from Wikipedia when online.
"""
from __future__ import annotations

import logging
from collections.abc import Iterable

import pandas as pd

from .config import get_settings

logger = logging.getLogger(__name__)

# Compact fallback (~120 large-cap names) used when online refresh fails.
# Keeps the pipeline usable in air-gapped / rate-limited environments.
STATIC_UNIVERSE: tuple[str, ...] = (
    "AAPL", "MSFT", "GOOGL", "GOOG", "AMZN", "META", "NVDA", "TSLA", "BRK-B", "JPM",
    "V", "UNH", "XOM", "LLY", "MA", "JNJ", "PG", "HD", "ORCL", "AVGO",
    "COST", "MRK", "ABBV", "CVX", "WMT", "BAC", "KO", "PEP", "ADBE", "CRM",
    "MCD", "TMO", "ACN", "ABT", "LIN", "CSCO", "NFLX", "WFC", "AMD", "DHR",
    "TXN", "DIS", "PM", "VZ", "CAT", "INTU", "IBM", "GE", "NEE", "UNP",
    "AMGN", "COP", "LOW", "SPGI", "QCOM", "HON", "NOW", "BKNG", "RTX", "AMAT",
    "GS", "SBUX", "T", "UPS", "INTC", "PFE", "MS", "BLK", "ISRG", "LMT",
    "AXP", "DE", "PLD", "ELV", "TJX", "GILD", "MDLZ", "SYK", "ADI", "C",
    "VRTX", "MDT", "ADP", "MMC", "CB", "PGR", "REGN", "CI", "LRCX", "SCHW",
    "TMUS", "BDX", "BSX", "ZTS", "SO", "DUK", "PANW", "EOG", "SLB", "FISV",
    "MU", "KLAC", "EQIX", "ETN", "APH", "ITW", "CME", "AON", "WM", "ICE",
    "CSX", "SNPS", "CDNS", "MO", "PYPL", "ABNB", "SHOP", "UBER", "PLTR", "COIN",
    "F", "GM", "DAL", "UAL", "AAL", "NKE", "LULU", "MAR",
)


def static_universe() -> list[str]:
    return list(STATIC_UNIVERSE)


def _fetch_sp500() -> list[str]:
    tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = tables[0]
    return [t.replace(".", "-") for t in df["Symbol"].astype(str).tolist()]


def _fetch_ndx() -> list[str]:
    tables = pd.read_html("https://en.wikipedia.org/wiki/Nasdaq-100")
    for t in tables:
        if "Ticker" in t.columns or "Symbol" in t.columns:
            col = "Ticker" if "Ticker" in t.columns else "Symbol"
            return [s.replace(".", "-") for s in t[col].astype(str).tolist()]
    return []


def refresh_universe() -> list[str]:
    """Return current S&P500 ∪ NDX100 tickers, or the static fallback."""
    try:
        tickers = sorted(set(_fetch_sp500()) | set(_fetch_ndx()))
        if not tickers:
            raise ValueError("empty ticker list")
        logger.info("universe refreshed: %d tickers", len(tickers))
        return tickers
    except Exception as e:  # noqa: BLE001
        logger.warning("universe refresh failed (%s); using static fallback", e)
        return static_universe()


def current_universe() -> list[str]:
    settings = get_settings()
    tickers = refresh_universe()
    if settings.universe_max and settings.universe_max > 0:
        tickers = tickers[: settings.universe_max]
    return tickers


def chunks(xs: Iterable[str], n: int) -> Iterable[list[str]]:
    buf: list[str] = []
    for x in xs:
        buf.append(x)
        if len(buf) >= n:
            yield buf
            buf = []
    if buf:
        yield buf
