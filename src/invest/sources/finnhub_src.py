"""Finnhub free-tier source (60 req/min): consensus, price targets, upgrades/downgrades."""
from __future__ import annotations

import logging
from datetime import date, datetime, timedelta
from typing import Any

import requests
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..config import get_settings
from ..db import session_scope
from ..firms import canonical_firm_key
from ..models import Consensus
from .base import BaseSource, TransientSourceError, log_run, upsert_analyst_actions, with_retries

logger = logging.getLogger(__name__)

_BASE = "https://finnhub.io/api/v1"


class FinnhubSource(BaseSource):
    name = "finnhub"
    rate_per_minute = 55.0  # leave headroom under the 60/min free-tier cap

    def __init__(self) -> None:
        super().__init__()
        self.api_key = get_settings().finnhub_api_key

    # --------------------------- http helpers ---------------------------

    @with_retries
    def _get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        if not self.api_key:
            raise TransientSourceError("FINNHUB_API_KEY not set")
        self.throttle()
        params = {**(params or {}), "token": self.api_key}
        try:
            resp = requests.get(f"{_BASE}{path}", params=params, timeout=15)
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        if resp.status_code == 429 or resp.status_code >= 500:
            raise TransientSourceError(f"{resp.status_code} {resp.text[:120]}")
        if resp.status_code >= 400:
            # 4xx other than 429: don't retry — surface as empty result.
            logger.warning("finnhub %s -> %s %s", path, resp.status_code, resp.text[:120])
            return None
        try:
            return resp.json()
        except ValueError as e:
            raise TransientSourceError(f"bad json: {e}") from e

    # --------------------------- consensus ---------------------------

    def _ingest_consensus_one(self, ticker: str) -> int:
        recs = self._get("/stock/recommendation", {"symbol": ticker}) or []
        target = self._get("/stock/price-target", {"symbol": ticker}) or {}
        if not recs and not target:
            return 0
        today = date.today()
        latest = recs[0] if recs else {}
        values = dict(
            ticker=ticker,
            as_of_date=today,
            source="finnhub",
            strong_buy=latest.get("strongBuy"),
            buy=latest.get("buy"),
            hold=latest.get("hold"),
            sell=latest.get("sell"),
            strong_sell=latest.get("strongSell"),
            mean_target=target.get("targetMean"),
            high_target=target.get("targetHigh"),
            low_target=target.get("targetLow"),
            num_analysts=target.get("numberOfAnalysts"),
        )
        with session_scope() as s:
            stmt = sqlite_insert(Consensus).values(values)
            stmt = stmt.on_conflict_do_update(
                index_elements=["ticker", "as_of_date", "source"],
                set_={
                    k: stmt.excluded[k]
                    for k in (
                        "strong_buy", "buy", "hold", "sell", "strong_sell",
                        "mean_target", "high_target", "low_target", "num_analysts",
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
                logger.warning("finnhub consensus %s failed: %s", t, e)
        return n

    # ---------------------- upgrades / downgrades ----------------------

    def _ingest_actions_one(self, ticker: str, cutoff: date) -> list[dict]:
        data = self._get(
            "/stock/upgrade-downgrade",
            {"symbol": ticker, "from": cutoff.isoformat(), "to": date.today().isoformat()},
        ) or []
        if not data:
            return []
        rows: list[dict] = []
        for item in data:
            try:
                d = datetime.utcfromtimestamp(int(item.get("gradeTime", 0))).date()
            except Exception:  # noqa: BLE001
                continue
            if d < cutoff:
                continue
            action = (item.get("action") or "").lower()
            mapped = "upgrade" if "up" in action else "downgrade" if "down" in action else action or None
            firm = (item.get("company") or "")[:128] or None
            rows.append(
                {
                    "ticker": ticker,
                    "firm": firm,
                    "firm_key": canonical_firm_key(firm),
                    "analyst": None,
                    "action": mapped,
                    "from_grade": (item.get("fromGrade") or "")[:64] or None,
                    "to_grade": (item.get("toGrade") or "")[:64] or None,
                    "target_price": None,
                    "date": d,
                    "source": "finnhub",
                }
            )
        return rows

    def ingest_actions(self, tickers: list[str], lookback_days: int = 90) -> int:
        cutoff = date.today() - timedelta(days=lookback_days)
        all_rows: list[dict] = []
        for t in tickers:
            try:
                all_rows.extend(self._ingest_actions_one(t, cutoff))
            except TransientSourceError as e:
                logger.warning("finnhub actions %s failed: %s", t, e)
        # Upsert on (ticker, firm_key, date, action, source): re-crawling the
        # same historical action updates the row instead of duplicating it.
        return upsert_analyst_actions(all_rows)

    # ------------------------------- run -------------------------------

    def run(self, tickers: list[str]) -> int:
        if not self.api_key:
            logger.info("finnhub disabled (no api key)")
            return 0
        total = 0
        with log_run("finnhub.consensus") as c:
            c["rows"] = self.ingest_consensus(tickers)
            total += c["rows"]
        with log_run("finnhub.actions") as c:
            c["rows"] = self.ingest_actions(tickers)
            total += c["rows"]
        return total
