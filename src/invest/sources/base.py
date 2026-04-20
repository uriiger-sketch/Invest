"""Shared plumbing for every data source: rate-limiting, retries, run-logging."""
from __future__ import annotations

import logging
import threading
import time
from abc import ABC, abstractmethod
from contextlib import contextmanager
from datetime import datetime
from typing import Iterator

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from ..db import session_scope
from ..models import RunLog

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
        with self._lock:
            while True:
                now = time.monotonic()
                self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
                self.last = now
                if self.tokens >= n:
                    self.tokens -= n
                    return
                needed = (n - self.tokens) / self.rate
            # unreachable
        time.sleep(needed)  # pragma: no cover


class TransientSourceError(Exception):
    """Raised for retryable errors (rate-limit, 5xx, timeout)."""


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
