"""Financial Modeling Prep free-tier source.

FMP exposes broad analyst coverage (consensus + price targets + grade
history) on its free tier with a ~250 req/day budget. Gated by an
optional ``FMP_API_KEY`` env var: if unset the source is silently
skipped, exactly like the Finnhub adapter.

Writes into the same ``Consensus`` and ``AnalystAction`` tables under
``source='fmp'``, so the cross-source disagreement check in
``pipeline/ingest`` and the firm-tier weighting in
``pipeline/features`` pick it up for free.
"""
from __future__ import annotations

import logging
from datetime import date, datetime, timedelta
from typing import Any

import requests
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..db import session_scope
from ..models import AnalystAction, Consensus
from .base import BaseSource, TransientSourceError, log_run, with_retries

logger = logging.getLogger(__name__)

_BASE = "https://financialmodelingprep.com/api/v3"


def _get_api_key() -> str:
    import os

    return os.environ.get("FMP_API_KEY", "").strip()


class FmpSource(BaseSource):
    name = "fmp"
    # 250 calls/day → keep well below the per-minute limits FMP enforces
    # under the hood. 30/min ≈ 2 calls / ticker × 100 tickers / hour, fine
    # for the daily deep crawl.
    rate_per_minute = 30.0

    def __init__(self) -> None:
        super().__init__()
        self.api_key = _get_api_key()

    @with_retries
    def _get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        if not self.api_key:
            raise TransientSourceError("FMP_API_KEY not set")
        self.throttle()
        params = {**(params or {}), "apikey": self.api_key}
        try:
            resp = requests.get(f"{_BASE}{path}", params=params, timeout=15)
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        if resp.status_code == 429 or resp.status_code >= 500:
            raise TransientSourceError(f"{resp.status_code} {resp.text[:120]}")
        if resp.status_code >= 400:
            logger.warning("fmp %s -> %s %s", path, resp.status_code, resp.text[:120])
            return None
        try:
            return resp.json()
        except ValueError as e:
            raise TransientSourceError(f"bad json: {e}") from e

    # ---------------------- consensus / targets ----------------------

    def _ingest_consensus_one(self, ticker: str) -> int:
        target = self._get(f"/price-target-consensus/{ticker}") or {}
        # FMP returns either a list with one dict or a bare dict depending
        # on endpoint version; normalise.
        if isinstance(target, list):
            target = target[0] if target else {}
        if not target:
            return 0
        today = date.today()
        values = dict(
            ticker=ticker,
            as_of_date=today,
            source="fmp",
            strong_buy=None,
            buy=None,
            hold=None,
            sell=None,
            strong_sell=None,
            mean_target=target.get("targetConsensus"),
            high_target=target.get("targetHigh"),
            low_target=target.get("targetLow"),
            num_analysts=None,
        )
        with session_scope() as s:
            stmt = sqlite_insert(Consensus).values(values)
            stmt = stmt.on_conflict_do_update(
                index_elements=["ticker", "as_of_date", "source"],
                set_={
                    k: stmt.excluded[k]
                    for k in (
                        "mean_target", "high_target", "low_target",
                    )
                },
            )
            s.execute(stmt)
        return 1

    def ingest_consensus(self, tickers: list[str]) -> int:
        n = 0
        for t in tickers:
            try:
                n += self._ingest_consensus_one(t)
            except TransientSourceError as e:
                logger.warning("fmp consensus %s failed: %s", t, e)
        return n

    # -------------------- upgrade / downgrade --------------------

    _ACTION_MAP = {
        "upgrade": "upgrade",
        "downgrade": "downgrade",
        "initiates coverage on": "init",
        "maintains": "reiterate",
        "reiterates": "reiterate",
        "reiterated": "reiterate",
    }

    def _ingest_actions_one(self, ticker: str, cutoff: date) -> int:
        # FMP's grade endpoint returns a list of recent rating changes.
        data = self._get(f"/grade/{ticker}") or []
        if not data:
            return 0
        written = 0
        with session_scope() as s:
            for item in data:
                try:
                    d = datetime.strptime(item.get("date", ""), "%Y-%m-%d").date()
                except (ValueError, TypeError):
                    continue
                if d < cutoff:
                    continue
                action_raw = (item.get("action") or "").lower()
                mapped = self._ACTION_MAP.get(action_raw, action_raw or None)
                s.add(
                    AnalystAction(
                        ticker=ticker,
                        firm=(item.get("gradingCompany") or "")[:128] or None,
                        analyst=None,
                        action=mapped,
                        from_grade=(item.get("previousGrade") or "")[:64] or None,
                        to_grade=(item.get("newGrade") or "")[:64] or None,
                        target_price=None,
                        date=d,
                        source="fmp",
                    )
                )
                written += 1
        return written

    def ingest_actions(self, tickers: list[str], lookback_days: int = 90) -> int:
        cutoff = date.today() - timedelta(days=lookback_days)
        n = 0
        for t in tickers:
            try:
                n += self._ingest_actions_one(t, cutoff)
            except TransientSourceError as e:
                logger.warning("fmp actions %s failed: %s", t, e)
        return n

    # ----------------------------- run -----------------------------

    def run(self, tickers: list[str]) -> int:
        if not self.api_key:
            logger.info("fmp disabled (no api key)")
            return 0
        total = 0
        with log_run("fmp.consensus") as c:
            c["rows"] = self.ingest_consensus(tickers)
            total += c["rows"]
        with log_run("fmp.actions") as c:
            c["rows"] = self.ingest_actions(tickers)
            total += c["rows"]
        return total
