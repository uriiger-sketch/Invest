"""Company news: Yahoo Finance stream (every ticker) + Google News RSS (focus list).

Every headline is normalised to one row shape, scored with the finance
lexicon in `invest.sentiment`, and deduplicated across feeds on
(ticker, normalised title) — the same wire story syndicated by Yahoo and by
Google News must count once in the sentiment average, not twice.
"""
from __future__ import annotations

import hashlib
import logging
import re
import time
from datetime import UTC, datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import Any
from urllib.parse import quote_plus

import requests
from lxml import etree
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..db import session_scope
from ..models import NewsItem
from ..sentiment import company_query_name, headline_relevance, score_headline
from .base import BaseSource, log_run

logger = logging.getLogger(__name__)

_WS = re.compile(r"[^a-z0-9]+")


def _naive_utc(dt: datetime) -> datetime:
    if dt.tzinfo is not None:
        dt = dt.astimezone(UTC).replace(tzinfo=None)
    return dt


def utcnow() -> datetime:
    """Naive UTC now (the DB stores naive UTC datetimes)."""
    return datetime.now(UTC).replace(tzinfo=None)


def news_id(ticker: str, title: str) -> str:
    norm = _WS.sub(" ", (title or "").lower()).strip()
    return hashlib.sha1(f"{ticker}|{norm}".encode()).hexdigest()


def make_news_row(
    ticker: str,
    title: str,
    published_at: datetime,
    publisher: str | None,
    url: str | None,
    source: str,
    company_name: str | None,
) -> dict[str, Any] | None:
    title = (title or "").strip()
    if len(title) < 8:
        return None
    return {
        "id": news_id(ticker, title),
        "ticker": ticker,
        "published_at": _naive_utc(published_at),
        "title": title[:300],
        "publisher": (publisher or "")[:80] or None,
        "url": (url or "")[:400] or None,
        "source": source,
        "sentiment": round(score_headline(title), 4),
        "relevance": headline_relevance(title, ticker, company_name),
    }


def upsert_news(rows: list[dict[str, Any]]) -> int:
    """Insert headlines; an id already stored (same story, any feed) is kept."""
    rows = [r for r in rows if r]
    if not rows:
        return 0
    # De-duplicate within the batch too: SQLite rejects a multi-row VALUES
    # insert that conflicts with itself only via ON CONFLICT, which is fine,
    # but dropping dupes first keeps the statement small.
    uniq = {r["id"]: r for r in rows}
    with session_scope() as s:
        stmt = sqlite_insert(NewsItem).values(list(uniq.values()))
        stmt = stmt.on_conflict_do_nothing(index_elements=["id"])
        s.execute(stmt)
    return len(uniq)


def parse_yahoo_news(
    ticker: str, items: list[dict] | None, company_name: str | None, max_age_days: int = 30
) -> list[dict[str, Any]]:
    """Normalise yfinance `get_news()` items (both the 2025+ nested `content`
    schema and the older flat schema) into news rows."""
    out: list[dict[str, Any]] = []
    cutoff = utcnow() - timedelta(days=max_age_days)
    for it in items or []:
        if not isinstance(it, dict):
            continue
        c = it.get("content") if isinstance(it.get("content"), dict) else it
        kind = str(c.get("contentType") or it.get("type") or "").upper()
        if kind == "VIDEO":
            continue
        title = c.get("title") or ""
        pub = c.get("pubDate") or c.get("displayTime") or it.get("providerPublishTime")
        dt: datetime | None = None
        try:
            if isinstance(pub, (int, float)):
                dt = datetime.fromtimestamp(float(pub), UTC).replace(tzinfo=None)
            elif isinstance(pub, str) and pub:
                dt = _naive_utc(datetime.fromisoformat(pub.replace("Z", "+00:00")))
        except (ValueError, OverflowError, OSError):
            dt = None
        if dt is None or dt < cutoff:
            continue
        provider = c.get("provider")
        publisher = provider.get("displayName") if isinstance(provider, dict) else it.get("publisher")
        url = None
        for key in ("canonicalUrl", "clickThroughUrl"):
            v = c.get(key)
            if isinstance(v, dict) and v.get("url"):
                url = v["url"]
                break
        url = url or it.get("link")
        row = make_news_row(ticker, title, dt, publisher, url, "yahoo", company_name)
        if row:
            related = {str(x).upper() for x in (it.get("relatedTickers") or [])}
            if ticker.upper() in related:
                row["relevance"] = 1.0  # Yahoo tagged the story with this symbol
            out.append(row)
    return out


def parse_google_news_rss(
    ticker: str, xml_bytes: bytes, company_name: str | None, max_age_days: int = 14
) -> list[dict[str, Any]]:
    """Parse a Google News RSS search result. Titles arrive as
    "Headline text - Publisher"; the publisher suffix is split off so it does
    not leak into the sentiment scoring or the cross-feed dedupe key."""
    out: list[dict[str, Any]] = []
    try:
        parser = etree.XMLParser(resolve_entities=False, no_network=True, recover=True)
        root = etree.fromstring(xml_bytes, parser=parser)
    except (etree.XMLSyntaxError, ValueError):
        return out
    if root is None:
        return out
    cutoff = utcnow() - timedelta(days=max_age_days)
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        source_el = item.find("source")
        publisher = source_el.text.strip() if source_el is not None and source_el.text else None
        if publisher and title.endswith(" - " + publisher):
            title = title[: -len(" - " + publisher)].strip()
        elif " - " in title and publisher is None:
            title, _, publisher = title.rpartition(" - ")
        try:
            dt = _naive_utc(parsedate_to_datetime(item.findtext("pubDate") or ""))
        except (TypeError, ValueError, IndexError):
            continue
        if dt < cutoff:
            continue
        row = make_news_row(
            ticker, title, dt, publisher, item.findtext("link"), "gnews", company_name
        )
        if row:
            out.append(row)
    return out


class GoogleNewsSource(BaseSource):
    """Keyless Google News RSS search, used for the focus list only.

    Yahoo's per-ticker stream is thin for many names (often 5-10 items, a
    third of them press releases). Google News aggregates Reuters, Bloomberg,
    WSJ, Barron's, CNBC, trade press and local outlets, which is where most
    "opinion changes" are reported first.
    """

    name = "gnews"
    rate_per_minute = 50.0

    def __init__(self) -> None:
        super().__init__()
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": "Mozilla/5.0 (compatible; InvestResearchBot/0.2)"}
        )

    def _query(self, ticker: str, company_name: str | None) -> str:
        base = ticker.split(".")[0]
        name = company_query_name(company_name)
        if name and name.upper() != base:
            q = f'"{name}" OR "{base} stock"'
        else:
            q = f'"{base} stock"'
        return f"{q} when:7d"

    def fetch(self, ticker: str, company_name: str | None) -> bytes | None:
        self.throttle()
        url = (
            "https://news.google.com/rss/search?q="
            + quote_plus(self._query(ticker, company_name))
            + "&hl=en-US&gl=US&ceid=US:en"
        )
        try:
            r = self.session.get(url, timeout=(6, 12))
        except requests.RequestException as e:
            logger.info("gnews %s failed: %s", ticker, e)
            return None
        if r.status_code != 200:
            logger.info("gnews %s -> HTTP %s", ticker, r.status_code)
            return None
        return r.content

    def ingest(self, tickers: list[str], names: dict[str, str], budget_seconds: float) -> int:
        started = time.monotonic()
        written = 0
        consecutive_fail = 0
        for t in tickers:
            if time.monotonic() - started > budget_seconds:
                logger.info("gnews: budget reached after %d tickers", tickers.index(t))
                break
            xml = self.fetch(t, names.get(t))
            if xml is None:
                consecutive_fail += 1
                if consecutive_fail >= 5:
                    logger.warning("gnews: 5 consecutive failures — skipping the rest this run")
                    break
                continue
            consecutive_fail = 0
            written += upsert_news(parse_google_news_rss(t, xml, names.get(t)))
        return written

    def run(self, tickers: list[str]) -> int:
        from ..config import get_settings
        from ..models import Stock

        with session_scope() as s:
            names = {
                t: n for t, n in s.query(Stock.ticker, Stock.name).filter(Stock.ticker.in_(tickers))
                if n
            }
        with log_run("gnews.headlines") as c:
            c["rows"] = self.ingest(tickers, names, get_settings().news_budget_seconds)
            return c["rows"]
