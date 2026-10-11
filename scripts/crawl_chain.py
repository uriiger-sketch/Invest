"""Seconds until the next chained crawl, or nothing when the chain should stop.

GitHub delivers only a fraction of this repository's scheduled ticks:
measured on 2026-10-10, ~5 of the 48 daily fast ticks ran, hours late, both
on :00/:30 and after moving to off-peak minutes. So during the US trading
session every crawl dispatches its successor (`next-crawl` in crawl.yml).
Outside the window the chain stops and the cron, which still fires every
few hours, covers nights and weekends without holding a runner, and its
first tick inside the next session restarts the chain.

Usage: crawl_chain.py [--started EPOCH] [--now EPOCH]
Prints the delay in whole seconds, or nothing to stop the chain.
"""
from __future__ import annotations

import argparse
from datetime import UTC, datetime, timedelta

# 12:00-21:00 UTC: pre-market news flow through the 16:00 ET close, under
# both EDT (20:00 UTC) and EST (21:00 UTC).
WINDOW_UTC = (12, 21)
INTERVAL_S = 30 * 60
MIN_DELAY_S = 60


def in_window(t: datetime) -> bool:
    return t.weekday() < 5 and WINDOW_UTC[0] <= t.hour < WINDOW_UTC[1]


def next_delay(now: datetime, started: datetime | None = None) -> int | None:
    """Delay that puts the next crawl INTERVAL_S after this one started,
    or None when that moment falls outside the trading-session window."""
    elapsed = (now - started).total_seconds() if started else 0.0
    delay = max(MIN_DELAY_S, int(INTERVAL_S - elapsed))
    return delay if in_window(now + timedelta(seconds=delay)) else None


def _epoch(s: str | None) -> datetime | None:
    try:
        return datetime.fromtimestamp(int(s), UTC) if s else None
    except (TypeError, ValueError, OverflowError, OSError):
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--started", default=None, help="epoch seconds the crawl started")
    ap.add_argument("--now", default=None, help="epoch seconds (testing)")
    args = ap.parse_args()
    now = _epoch(args.now) or datetime.now(UTC)
    delay = next_delay(now, _epoch(args.started))
    if delay is not None:
        print(delay)


if __name__ == "__main__":
    main()
