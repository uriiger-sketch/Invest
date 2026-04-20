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


def test_log_run_writes_ok_row():
    with log_run("test.ok") as c:
        c["rows"] = 3
    with session_scope() as s:
        row = s.execute(select(RunLog).where(RunLog.job == "test.ok")).scalar_one()
    assert row.status == "ok"
    assert row.rows_written == 3


def test_log_run_captures_error():
    with pytest.raises(ValueError):
        with log_run("test.err"):
            raise ValueError("boom")
    with session_scope() as s:
        row = s.execute(select(RunLog).where(RunLog.job == "test.err")).scalar_one()
    assert row.status == "error"
    assert "boom" in (row.error or "")
