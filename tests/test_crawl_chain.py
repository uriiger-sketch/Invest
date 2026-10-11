"""Timing rules of the self-dispatching crawl chain (scripts/crawl_chain.py)."""
from __future__ import annotations

import importlib.util
import subprocess
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "crawl_chain.py"
_spec = importlib.util.spec_from_file_location("crawl_chain", SCRIPT)
chain = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(chain)

MON = datetime(2026, 10, 12, tzinfo=UTC)  # a Monday


def at(day: datetime, hh: int, mm: int) -> datetime:
    return day.replace(hour=hh, minute=mm)


def test_next_crawl_lands_thirty_minutes_after_this_one_started():
    now = at(MON, 14, 7)
    assert chain.next_delay(now, now - timedelta(minutes=7)) == 23 * 60
    assert chain.next_delay(now, None) == 30 * 60
    # A crawl that overran its slot is followed promptly, never instantly.
    assert chain.next_delay(now, now - timedelta(minutes=45)) == chain.MIN_DELAY_S


def test_chain_runs_only_inside_the_weekday_session_window():
    started = timedelta(minutes=7)
    # The first slot after a run ending just before 12:00 is inside -> chain starts.
    assert chain.next_delay(at(MON, 11, 50), at(MON, 11, 50) - started) == 23 * 60
    # The slot after the close falls outside -> chain stops, cron takes over.
    assert chain.next_delay(at(MON, 20, 57), at(MON, 20, 57) - started) is None
    friday_close = at(MON + timedelta(days=4), 20, 50)
    assert chain.next_delay(friday_close, friday_close - started) is None
    saturday = at(MON + timedelta(days=5), 15, 0)
    assert chain.next_delay(saturday, saturday - started) is None
    nightly_deep = at(MON, 23, 59)
    assert chain.next_delay(nightly_deep, nightly_deep - timedelta(minutes=27)) is None


def test_a_morning_run_waits_for_the_open_but_never_more_than_four_hours():
    """GitHub's sparse cron ticks mostly land 06:00-11:00 UTC, then not
    until mid-afternoon; without the lead-in the chain would start late."""
    morning = at(MON, 9, 47)
    assert chain.next_delay(morning, morning - timedelta(minutes=7)) == (2 * 60 + 13) * 60
    dawn = at(MON, 6, 9)  # 5 h 51 min before the open: too long to hold a runner
    assert chain.next_delay(dawn, dawn - timedelta(minutes=7)) is None
    edge = at(MON, 8, 0)
    assert chain.next_delay(edge, edge - timedelta(minutes=7)) == chain.MAX_LEAD_S
    saturday_morning = at(MON + timedelta(days=5), 10, 0)
    assert chain.next_delay(saturday_morning, saturday_morning) is None
    sunday_night = at(MON + timedelta(days=6), 23, 0)  # next open is Monday 12:00, 13 h away
    assert chain.next_delay(sunday_night, sunday_night) is None


def test_cli_prints_delay_or_nothing_and_tolerates_a_missing_start():
    def run(*args: str) -> str:
        return subprocess.run([sys.executable, str(SCRIPT), *args],
                              capture_output=True, text=True, check=True).stdout.strip()

    now = int(at(MON, 14, 7).timestamp())
    assert run("--now", str(now), "--started", str(now - 420)) == "1380"
    assert run("--now", str(now), "--started", "") == "1800"
    assert run("--now", str(now), "--started", "garbage") == "1800"
    assert run("--now", str(int(at(MON, 22, 0).timestamp()))) == ""
