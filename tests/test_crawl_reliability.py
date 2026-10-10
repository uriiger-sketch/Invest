"""Regression tests for the crawl failures found in the live workflow logs.

Runs 2006 and 2015 were killed at the 25-minute fast-ingest limit: twelve
delisted symbols each burned ~130 s in stooq connect-timeout retries. The
database had also grown to 87 MB (GitHub's hard limit is 100 MB) because
NULL-valued insider placeholder rows bypassed their unique index.
"""
from __future__ import annotations

import sqlite3
from datetime import UTC, date, datetime, timedelta

from invest.db import session_scope
from invest.models import Consensus, Grade, IntelSnapshot, NewsItem, Price, RunLog, Score
from invest.pipeline import ingest
from invest.sources.base import TransientSourceError
from invest.sources.stooq_src import StooqSource, _to_stooq_symbol


def _price(t: str, d: date, close: float = 100.0) -> Price:
    return Price(ticker=t, date=d, close=close, adj_close=close, volume=1e6)


def test_dormant_is_relative_to_the_freshest_price_not_today():
    ref = date.today() - timedelta(days=3)  # e.g. a long weekend
    with session_scope() as s:
        s.add(_price("LIVE", ref))
        s.add(_price("STALE", ref - timedelta(days=30)))
    dead = ingest.dormant_tickers(["LIVE", "STALE", "NEVER"])
    assert set(dead) == {"STALE", "NEVER"}
    assert ingest.active_tickers(["LIVE", "STALE", "NEVER"]) == ["LIVE"]


def test_empty_database_marks_nothing_dormant():
    assert ingest.dormant_tickers(["A", "B"]) == []


def test_stooq_candidates_are_recently_live_us_names_only():
    today = date.today()
    with session_scope() as s:
        s.add(_price("FRESH", today))
        s.add(_price("GAP", today - timedelta(days=6)))         # live, missing lately
        s.add(_price("DEAD", today - timedelta(days=90)))       # delisted
        s.add(_price("DELT.TA", today - timedelta(days=6)))     # stooq can't serve .TA
    assert ingest.stooq_candidates(["FRESH", "GAP", "DEAD", "DELT.TA", "NEVER"]) == ["GAP"]


def test_stooq_symbol_mapping_rejects_exchange_suffixes():
    assert _to_stooq_symbol("AAPL") == "aapl.us"
    assert _to_stooq_symbol("BRK-B") == "brk-b.us"
    assert _to_stooq_symbol("DELT.TA") is None
    assert _to_stooq_symbol("PRX.AS") is None


def test_stooq_circuit_breaker_stops_after_three_failures(monkeypatch):
    calls = []

    def boom(self, ticker, days):
        calls.append(ticker)
        raise TransientSourceError("connect timeout")

    monkeypatch.setattr(StooqSource, "_fetch_one", boom)
    StooqSource().ingest_prices([f"T{i}" for i in range(12)], budget_seconds=60)
    assert len(calls) == 3, "an unreachable host must cost 3 attempts, not 12 x retries"


def test_focus_list_prefers_latest_grades_then_horizon_tops():
    today = date.today()
    with session_scope() as s:
        for i, t in enumerate(["G1", "G2"]):
            s.add(Grade(ticker=t, as_of=today, grade_score=2.0 - i, letter="A"))
        for h in ("hours", "daily", "weekly", "monthly"):
            s.add(Score(ticker=f"S_{h}", horizon=h, as_of=today, blended_score=1.0))
    focus = ingest.focus_tickers(10)
    assert focus[:2] == ["G1", "G2"]
    assert {"S_hours", "S_daily", "S_weekly", "S_monthly"} <= set(focus)


def test_stalest_ordering_uses_intel_timestamps():
    """Several runs a day all write today's consensus date; ordering by date
    alone left the same alphabetical tail last on every truncated sweep."""
    today = date.today()
    now = datetime.now(UTC).replace(tzinfo=None)
    with session_scope() as s:
        for t in ("AAA", "BBB", "CCC"):
            s.add(Consensus(ticker=t, as_of_date=today, source="yfinance"))
        s.add(IntelSnapshot(ticker="AAA", kind="quote", as_of=now, payload="{}"))
        s.add(IntelSnapshot(ticker="BBB", kind="quote", as_of=now - timedelta(hours=5), payload="{}"))
    assert ingest.stalest_tickers(["AAA", "BBB", "CCC"], 3) == ["CCC", "BBB", "AAA"]


def test_dormant_list_is_recorded_for_the_report():
    today = date.today()
    with session_scope() as s:
        s.add(_price("LIVE", today))
        s.add(_price("GONE", today - timedelta(days=40)))
    ingest._record_dormant(["LIVE", "GONE"])
    with session_scope() as s:
        row = s.query(RunLog).filter(RunLog.job == "universe.dormant").one()
    assert row.rows_written == 1 and "GONE" in (row.error or "")


def test_maintenance_prunes_only_expired_history():
    from invest.pipeline.maintenance import prune_and_vacuum

    now = datetime.now(UTC).replace(tzinfo=None)
    with session_scope() as s:
        s.add(NewsItem(id="old", ticker="X", published_at=now - timedelta(days=90), title="old news",
                       source="yahoo"))
        s.add(NewsItem(id="new", ticker="X", published_at=now - timedelta(days=1), title="new news",
                       source="yahoo"))
        s.add(Score(ticker="X", horizon="hours", as_of=date.today() - timedelta(days=400)))
        s.add(Score(ticker="X", horizon="hours", as_of=date.today()))
    deleted = prune_and_vacuum()
    assert deleted["news_items"] == 1 and deleted["scores"] == 1
    with session_scope() as s:
        assert {n.id for n in s.query(NewsItem)} == {"new"}
        assert s.query(Score).count() == 1


def test_migration_0005_repairs_the_live_data_defects(tmp_path, monkeypatch):
    """Run the real Alembic chain on a file DB seeded with the three measured
    defects: duplicate NULL placeholders, filing-date 13F quarter labels and
    legacy 'reit' actions."""
    from alembic.config import Config

    from alembic import command

    db = tmp_path / "m.db"
    monkeypatch.setenv("INVEST_DB_URL", f"sqlite:///{db}")
    cfg = Config("alembic.ini")
    command.upgrade(cfg, "0004")

    con = sqlite3.connect(db)
    cur = con.cursor()
    for _ in range(50):  # the same placeholder re-inserted by 50 crawls
        cur.execute("INSERT INTO insider_trades (ticker, filer, action, shares, price, date) "
                    "VALUES ('AAA', '(aggregated form-4 activity)', 'activity', NULL, NULL, '2026-09-01')")
    cur.execute("INSERT INTO insider_trades (ticker, filer, action, shares, price, date) "
                "VALUES ('AAA', 'JANE DOE', 'buy', 100, 10, '2026-09-02')")
    # Q2 portfolio filed in August was labelled Q3; Q1 filed in May labelled Q2.
    cur.execute("INSERT INTO holdings_13f (filer_cik, filer_name, ticker, shares, quarter, filing_date) "
                "VALUES ('1', 'F', 'AAA', 200, '2026Q3', '2026-08-14')")
    cur.execute("INSERT INTO holdings_13f (filer_cik, filer_name, ticker, shares, quarter, filing_date) "
                "VALUES ('1', 'F', 'AAA', 100, '2026Q2', '2026-05-15')")
    for action in ("reit", "reiterate"):
        cur.execute("INSERT INTO analyst_actions (ticker, firm, firm_key, action, date, source) "
                    f"VALUES ('AAA', 'UBS', 'ubs', '{action}', '2026-09-01', 'yfinance')")
    cur.execute("INSERT INTO analyst_actions (ticker, firm, firm_key, action, date, source) "
                "VALUES ('AAA', 'Citi', 'citi', 'reit', '2026-09-03', 'yfinance')")
    con.commit()
    con.close()

    command.upgrade(cfg, "head")

    con = sqlite3.connect(db)
    cur = con.cursor()
    assert cur.execute("SELECT COUNT(*) FROM insider_trades WHERE action='activity'").fetchone()[0] == 1
    assert cur.execute("SELECT shares, price FROM insider_trades WHERE action='activity'").fetchone() == (0, 0)
    assert cur.execute("SELECT COUNT(*) FROM insider_trades WHERE action='buy'").fetchone()[0] == 1
    q = dict(cur.execute("SELECT filing_date, quarter FROM holdings_13f").fetchall())
    assert q == {"2026-08-14": "2026Q2", "2026-05-15": "2026Q1"}
    acts = cur.execute("SELECT firm_key, action FROM analyst_actions ORDER BY firm_key").fetchall()
    assert acts == [("citi", "reiterate"), ("ubs", "reiterate")]
    tables = {r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"news_items", "sec_filings", "intel_snapshots", "grades", "calibration"} <= tables
    con.close()
