from __future__ import annotations

import time

import pytest
from sqlalchemy import select

from invest.db import session_scope
from invest.models import RunLog
from invest.sources.base import TokenBucket, log_run


def test_token_bucket_rate_limits():
    b = TokenBucket(rate_per_minute=120, burst=2)  # 2/sec
    start = time.monotonic()
    for _ in range(4):
        b.take()
    elapsed = time.monotonic() - start
    # 2 tokens free, 2 more require ~1s of refill
    assert elapsed >= 0.4


def test_token_bucket_actually_sleeps_instead_of_busy_spinning(monkeypatch):
    """`take()` previously had `time.sleep(needed)` sitting after an
    unbroken `while True:` loop, inside the lock — genuinely unreachable
    code. The loop busy-spun at 100% CPU while holding the lock (blocking
    every other thread sharing the bucket) until enough wall-clock time
    passed on its own for tokens to refill. This asserts the sleep path is
    actually reached when a caller needs to wait, by counting real calls to
    time.sleep."""
    calls = []
    real_sleep = time.sleep

    def _fake_sleep(seconds):
        calls.append(seconds)
        real_sleep(min(seconds, 0.05))  # keep the test fast

    monkeypatch.setattr(time, "sleep", _fake_sleep)
    b = TokenBucket(rate_per_minute=120, burst=1)  # 1 token, needs a real wait for more
    b.take()  # drains the only free token
    b.take()  # must actually sleep to get the next one
    assert calls, "take() never called time.sleep — it's still busy-spinning"


def test_log_run_writes_ok_row():
    with log_run("test.ok") as c:
        c["rows"] = 3
    with session_scope() as s:
        row = s.execute(select(RunLog).where(RunLog.job == "test.ok")).scalar_one()
    assert row.status == "ok"
    assert row.rows_written == 3


def test_log_run_captures_error():
    with pytest.raises(ValueError), log_run("test.err"):
        raise ValueError("boom")
    with session_scope() as s:
        row = s.execute(select(RunLog).where(RunLog.job == "test.err")).scalar_one()
    assert row.status == "error"
    assert "boom" in (row.error or "")
