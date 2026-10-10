"""Shared plumbing for every data source: rate-limiting, retries, run-logging."""
from __future__ import annotations

import logging
import threading
import time
from abc import ABC, abstractmethod
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from ..db import session_scope
from ..models import AnalystAction, InsiderTrade, RunLog

logger = logging.getLogger(__name__)


class TokenBucket:
    """Simple token bucket for per-source rate limiting. Thread-safe."""

    def __init__(self, rate_per_minute: float, burst: int | None = None) -> None:
        self.rate = rate_per_minute / 60.0  # tokens per second
        self.capacity = float(burst if burst is not None else max(1, int(rate_per_minute)))
        self.tokens = self.capacity
        self.last = time.monotonic()
        self._lock = threading.Lock()

    def take(self, n: float = 1.0) -> None:
        """Block until `n` tokens are available.

        The lock is held only while checking/updating the bucket, then
        released before sleeping. Previously `time.sleep` sat after an
        unbroken `while True:` still inside the `with self._lock:` block, so
        it was unreachable dead code — the loop busy-spun at 100 % CPU,
        holding the lock the entire time (blocking every other thread that
        shares this bucket) until enough wall-clock time passed for tokens to
        refill on their own.
        """
        while True:
            with self._lock:
                now = time.monotonic()
                self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
                self.last = now
                if self.tokens >= n:
                    self.tokens -= n
                    return
                needed = (n - self.tokens) / self.rate
            time.sleep(needed)


class TransientSourceError(Exception):
    """Raised for retryable errors (rate-limit, 5xx, timeout)."""


class RateLimitedError(TransientSourceError):
    """The provider answered HTTP 429 / "Too Many Requests"."""


class CrawlAborted(Exception):
    """Raised by RateGovernor once a provider keeps rate-limiting us."""


class RateGovernor:
    """Shared, thread-safe back-off for one provider across worker threads.

    Per-request retries (``with_retries``) absorb an isolated 429. What they
    cannot handle is a provider-wide block: every worker would keep burning
    its own retry budget against a wall. After ``threshold`` consecutive
    rate-limited tickers the governor pauses ALL workers for ``cooldown``
    seconds; after ``max_cooldowns`` pauses it aborts the stage so the run
    moves on (the stalest-first ordering means skipped names go first next
    run) instead of timing out the whole workflow.
    """

    def __init__(self, threshold: int = 6, cooldown: float = 45.0, max_cooldowns: int = 3) -> None:
        self.threshold = threshold
        self.cooldown = cooldown
        self.max_cooldowns = max_cooldowns
        self._lock = threading.Lock()
        self._consecutive = 0
        self._cooldowns = 0
        self._resume_at = 0.0
        self.aborted = False
        self.rate_limited = 0

    def before_request(self) -> None:
        with self._lock:
            if self.aborted:
                raise CrawlAborted("provider rate-limit abort")
            wait = self._resume_at - time.monotonic()
        if wait > 0:
            time.sleep(wait)

    def on_success(self) -> None:
        with self._lock:
            self._consecutive = 0

    def on_rate_limit(self) -> None:
        with self._lock:
            self.rate_limited += 1
            self._consecutive += 1
            if self._consecutive < self.threshold:
                return
            self._consecutive = 0
            self._cooldowns += 1
            if self._cooldowns > self.max_cooldowns:
                self.aborted = True
                logger.error("rate governor: provider still throttling after %d cool-downs; aborting stage",
                             self.max_cooldowns)
                return
            self._resume_at = time.monotonic() + self.cooldown
            logger.warning("rate governor: %d consecutive 429s — pausing all workers %.0fs (cool-down %d/%d)",
                           self.threshold, self.cooldown, self._cooldowns, self.max_cooldowns)


def with_retries(fn):
    """Decorator: retry transient errors with jittered exponential backoff."""
    return retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential_jitter(initial=1.0, max=30.0),
        retry=retry_if_exception_type(TransientSourceError),
        reraise=True,
    )(fn)


@contextmanager
def log_run(job: str) -> Iterator[dict[str, int]]:
    """Record a job in `run_log`. Caller mutates `counter['rows']` for reporting."""
    counter: dict[str, int] = {"rows": 0}
    started = datetime.utcnow()
    entry_id: int | None = None
    with session_scope() as s:
        entry = RunLog(job=job, started_at=started, status="running", rows_written=0)
        s.add(entry)
        s.flush()
        entry_id = entry.id
    try:
        yield counter
    except Exception as e:
        logger.exception("job %s failed", job)
        with session_scope() as s:
            row = s.get(RunLog, entry_id)
            if row is not None:
                row.finished_at = datetime.utcnow()
                row.status = "error"
                row.rows_written = counter["rows"]
                row.error = f"{type(e).__name__}: {e}"[:2000]
        raise
    else:
        with session_scope() as s:
            row = s.get(RunLog, entry_id)
            if row is not None:
                row.finished_at = datetime.utcnow()
                row.status = "ok"
                row.rows_written = counter["rows"]


def upsert_analyst_actions(rows: list[dict]) -> int:
    """Insert AnalystAction rows, upserting on (ticker, firm_key, date,
    action, source) so the SAME real analyst action reported again on a
    later crawl (every feed returns a rolling ~90-day window each call)
    updates the existing row instead of creating a duplicate.

    Every ingester (yfinance, Finnhub, FMP) MUST route through this
    instead of `session.add(AnalystAction(...))` — that was the actual
    root cause of the same firm being counted as multiple sources: a
    single Goldman Sachs upgrade re-inserted on every 2-hour crawl became
    dozens of identical-looking rows within days.

    Each dict in `rows` must already have `firm_key` set via
    `invest.firms.canonical_firm_key(firm)`. Rows without a usable
    `firm_key` (blank firm) are skipped — they can't be deduped and
    aren't real named sources anyway.
    """
    from sqlalchemy.dialects.sqlite import insert as sqlite_insert

    # Every row must carry the same keys for a multi-row VALUES insert;
    # sources that predate the target-change columns simply leave them None.
    usable = [
        {"prior_target": None, "target_action": None, **r} for r in rows if r.get("firm_key")
    ]
    if not usable:
        return 0
    with session_scope() as s:
        stmt = sqlite_insert(AnalystAction).values(usable)
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker", "firm_key", "date", "action", "source"],
            set_={
                "firm": stmt.excluded.firm,
                "analyst": stmt.excluded.analyst,
                "from_grade": stmt.excluded.from_grade,
                "to_grade": stmt.excluded.to_grade,
                "target_price": stmt.excluded.target_price,
                "prior_target": stmt.excluded.prior_target,
                "target_action": stmt.excluded.target_action,
            },
        )
        s.execute(stmt)
    return len(usable)


def upsert_insider_trades(rows: list[dict]) -> int:
    """Insert InsiderTrade rows, upserting on (ticker, filer, date, action,
    shares, price) so re-crawling the SAME historical Form 4 transaction
    (the SEC atom feed is a rolling recent-filings window, not a one-time
    event) doesn't create a duplicate. Rows with no real transaction detail
    (NULL shares/price — a filing we couldn't parse individually) are NOT
    deduplicated by this constraint (SQLite treats NULL as never equal to
    another NULL), but that's fine: they always contribute a net-zero
    signal to `insider_net_buy_90d` regardless of how many accumulate.
    """
    from sqlalchemy.dialects.sqlite import insert as sqlite_insert

    if not rows:
        return 0
    # Placeholder rows ("a filing happened, detail unparsed") must carry
    # 0, not NULL, for shares/price: SQLite never treats two NULLs as equal,
    # so NULL placeholders bypassed the unique index and were re-inserted on
    # every crawl (341k duplicate rows / ~57 MB before migration 0005).
    rows = [
        {**r, "shares": r.get("shares") or 0.0, "price": r.get("price") or 0.0} for r in rows
    ]
    with session_scope() as s:
        stmt = sqlite_insert(InsiderTrade).values(rows)
        stmt = stmt.on_conflict_do_nothing(
            index_elements=["ticker", "filer", "date", "action", "shares", "price"],
        )
        s.execute(stmt)
    return len(rows)


class BaseSource(ABC):
    """Abstract source. Subclasses implement `run(tickers)` and reuse helpers."""

    name: str = "base"
    rate_per_minute: float = 60.0

    def __init__(self) -> None:
        self.bucket = TokenBucket(rate_per_minute=self.rate_per_minute)

    def throttle(self, n: float = 1.0) -> None:
        self.bucket.take(n)

    @abstractmethod
    def run(self, tickers: list[str]) -> int:  # returns rows written
        ...
