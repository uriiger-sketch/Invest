"""Stooq price source — free, no API key, reliable CSV endpoint.

Used as a fallback when yfinance is rate-limited or returns empty frames.
Format: https://stooq.com/q/d/l/?s=aapl.us&i=d returns CSV
    Date,Open,High,Low,Close,Volume
"""
from __future__ import annotations

import csv
import io
import logging
import time
from datetime import date, datetime, timedelta

import requests
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..db import session_scope
from ..models import Price
from .base import BaseSource, TransientSourceError, log_run

logger = logging.getLogger(__name__)


def _to_stooq_symbol(ticker: str) -> str | None:
    """AAPL -> aapl.us, BRK-B -> brk-b.us; None for non-US listings.

    Exchange-suffixed tickers (DELT.TA, PRX.AS) used to be mangled into
    "delt-ta.us" — a symbol stooq has never heard of — so the fallback could
    never succeed for exactly the names it was being asked about.
    """
    if "." in ticker:
        return None
    return ticker.lower() + ".us"


class StooqSource(BaseSource):
    name = "stooq"
    rate_per_minute = 120.0  # stooq is generous but be polite

    def __init__(self) -> None:
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Invest/0.1 (research)"})

    def _fetch_one(self, ticker: str, days: int) -> list[dict]:
        """One attempt, short timeouts, no retries.

        This is a best-effort fallback. It used to retry every failure 4x
        with a 15 s connect timeout; when stooq.com stopped accepting
        connections from GitHub runners, each missing ticker cost ~130 s and
        twelve delisted tickers pushed the fast ingest past its 25-minute
        step limit — killing the whole run (observed on runs 2006, 2015).
        """
        symbol = _to_stooq_symbol(ticker)
        if symbol is None:
            return []
        self.throttle()
        cutoff = date.today() - timedelta(days=days)
        url = f"https://stooq.com/q/d/l/?s={symbol}&i=d"
        try:
            resp = self.session.get(url, timeout=(5, 10))
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        if resp.status_code == 429 or resp.status_code >= 500:
            raise TransientSourceError(f"{resp.status_code}")
        if resp.status_code >= 400:
            return []
        text = resp.text.strip()
        if not text or text.lower().startswith("no data"):
            return []
        rows: list[dict] = []
        reader = csv.DictReader(io.StringIO(text))
        for r in reader:
            try:
                d = datetime.strptime(r["Date"], "%Y-%m-%d").date()
            except (KeyError, ValueError):
                continue
            if d < cutoff:
                continue
            try:
                rows.append(
                    {
                        "ticker": ticker,
                        "date": d,
                        "open": float(r["Open"]) if r.get("Open") else None,
                        "high": float(r["High"]) if r.get("High") else None,
                        "low": float(r["Low"]) if r.get("Low") else None,
                        "close": float(r["Close"]) if r.get("Close") else None,
                        "adj_close": float(r["Close"]) if r.get("Close") else None,
                        "volume": float(r["Volume"]) if r.get("Volume") else None,
                    }
                )
            except ValueError:
                continue
        return rows

    def ingest_prices(
        self, tickers: list[str], days: int = 90, budget_seconds: float = 45.0
    ) -> int:
        written = 0
        started = time.monotonic()
        consecutive_fail = 0
        for t in tickers:
            if time.monotonic() - started > budget_seconds:
                logger.warning("stooq: %.0fs budget exhausted; skipping remaining tickers",
                               budget_seconds)
                break
            try:
                rows = self._fetch_one(t, days)
                consecutive_fail = 0
            except TransientSourceError as e:
                consecutive_fail += 1
                logger.warning("stooq %s failed: %s", t, e)
                if consecutive_fail >= 3:
                    logger.warning("stooq: 3 consecutive failures — host unreachable, giving up this run")
                    break
                continue
            if not rows:
                continue
            with session_scope() as s:
                stmt = sqlite_insert(Price).values(rows)
                stmt = stmt.on_conflict_do_update(
                    index_elements=["ticker", "date"],
                    set_={
                        "open": stmt.excluded.open,
                        "high": stmt.excluded.high,
                        "low": stmt.excluded.low,
                        "close": stmt.excluded.close,
                        "adj_close": stmt.excluded.adj_close,
                        "volume": stmt.excluded.volume,
                    },
                )
                s.execute(stmt)
            written += len(rows)
        return written

    def run(self, tickers: list[str]) -> int:
        from ..config import get_settings

        with log_run("stooq.prices") as c:
            c["rows"] = self.ingest_prices(
                tickers, budget_seconds=get_settings().stooq_budget_seconds
            )
            return c["rows"]
