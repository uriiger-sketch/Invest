"""Regression tests for the "same firm counted as multiple sources" bug.

Two compounding root causes, both fixed here:
1. AnalystAction had no unique constraint and every ingester blindly
   INSERTed a new row on every crawl, so a single real action re-reported
   by a rolling-window feed accumulated into dozens of duplicate rows.
2. Different feeds spell the same firm differently ("Goldman Sachs" vs
   "Goldman Sachs & Co."), and nothing collapsed those before counting
   "distinct firms".
"""
from __future__ import annotations

from datetime import date, timedelta

from invest.db import session_scope
from invest.firms import canonical_firm_key
from invest.models import AnalystAction, Stock
from invest.sources.base import upsert_analyst_actions


def _seed_stock(ticker: str) -> None:
    with session_scope() as s:
        if not s.get(Stock, ticker):
            s.add(Stock(ticker=ticker, name=ticker, sector="Technology", in_universe=True))


def test_canonical_firm_key_collapses_spelling_variants():
    variants = ["Goldman Sachs", "Goldman Sachs & Co.", "GOLDMAN SACHS GROUP", "goldman sachs inc"]
    keys = {canonical_firm_key(v) for v in variants}
    assert len(keys) == 1, f"expected one canonical identity, got {keys}"


def test_upsert_prevents_duplicate_rows_on_repeated_crawl():
    """Simulates the actual bug: the same historical action reported again
    by a later crawl (yfinance/Finnhub/FMP all return rolling windows).
    Calling upsert_analyst_actions twice with identical data must not
    create a second row."""
    _seed_stock("DUPE")
    d = date.today() - timedelta(days=5)
    row = {
        "ticker": "DUPE",
        "firm": "Goldman Sachs",
        "firm_key": canonical_firm_key("Goldman Sachs"),
        "analyst": None,
        "action": "upgrade",
        "from_grade": "Hold",
        "to_grade": "Buy",
        "target_price": 150.0,
        "date": d,
        "source": "yfinance",
    }
    upsert_analyst_actions([row])
    upsert_analyst_actions([row])  # simulates the next scheduled crawl
    upsert_analyst_actions([dict(row)])  # and the one after that

    with session_scope() as s:
        count = s.query(AnalystAction).filter(AnalystAction.ticker == "DUPE").count()
    assert count == 1, "the same action was inserted more than once"


def test_upsert_treats_different_spellings_as_the_same_row():
    """Two feeds reporting the SAME action with different spellings must
    still collapse to one row, because firm_key (not the raw firm string)
    is the identity."""
    _seed_stock("SPELL")
    d = date.today() - timedelta(days=3)
    row_a = {
        "ticker": "SPELL", "firm": "Goldman Sachs", "firm_key": canonical_firm_key("Goldman Sachs"),
        "analyst": None, "action": "upgrade", "from_grade": "Hold", "to_grade": "Buy",
        "target_price": 100.0, "date": d, "source": "yfinance",
    }
    row_b = {
        "ticker": "SPELL", "firm": "Goldman Sachs & Co.", "firm_key": canonical_firm_key("Goldman Sachs & Co."),
        "analyst": None, "action": "upgrade", "from_grade": "Hold", "to_grade": "Buy",
        "target_price": 101.0, "date": d, "source": "yfinance",
    }
    upsert_analyst_actions([row_a])
    upsert_analyst_actions([row_b])

    with session_scope() as s:
        rows = s.query(AnalystAction).filter(AnalystAction.ticker == "SPELL").all()
    assert len(rows) == 1
    # The upsert refreshes displayed fields (firm, target_price) to the latest report.
    assert rows[0].target_price == 101.0


def test_upsert_keeps_distinct_firms_and_dates_separate():
    """Sanity check the fix doesn't over-collapse: genuinely different
    firms, dates, or actions on the same ticker must all persist."""
    _seed_stock("MANY")
    base = date.today() - timedelta(days=10)
    rows = [
        {
            "ticker": "MANY", "firm": f"Firm {i}", "firm_key": canonical_firm_key(f"Firm {i}"),
            "analyst": None, "action": "upgrade", "from_grade": "Hold", "to_grade": "Buy",
            "target_price": 100.0 + i, "date": base + timedelta(days=i), "source": "yfinance",
        }
        for i in range(5)
    ]
    upsert_analyst_actions(rows)
    with session_scope() as s:
        count = s.query(AnalystAction).filter(AnalystAction.ticker == "MANY").count()
    assert count == 5


def test_firm_count_90d_dedupes_spelling_variants():
    """features.py's firm_count_90d must count 'Goldman Sachs' and
    'Goldman Sachs & Co.' as ONE distinct firm."""
    from invest.pipeline.features import build_features

    _seed_stock("FC90")
    with session_scope() as s:
        from invest.models import Price

        price = 100.0
        for i in range(90):
            s.add(Price(ticker="FC90", date=date.today() - timedelta(days=90 - i),
                        close=price, adj_close=price, volume=1_000_000))
    rows = [
        {"ticker": "FC90", "firm": "Goldman Sachs", "firm_key": canonical_firm_key("Goldman Sachs"),
         "analyst": None, "action": "upgrade", "from_grade": "Hold", "to_grade": "Buy",
         "target_price": 120.0, "date": date.today() - timedelta(days=5), "source": "yfinance"},
        {"ticker": "FC90", "firm": "Goldman Sachs & Co.", "firm_key": canonical_firm_key("Goldman Sachs & Co."),
         "analyst": None, "action": "reiterate", "from_grade": "Buy", "to_grade": "Buy",
         "target_price": 121.0, "date": date.today() - timedelta(days=2), "source": "finnhub"},
        {"ticker": "FC90", "firm": "Morgan Stanley", "firm_key": canonical_firm_key("Morgan Stanley"),
         "analyst": None, "action": "upgrade", "from_grade": "Hold", "to_grade": "Buy",
         "target_price": 122.0, "date": date.today() - timedelta(days=1), "source": "yfinance"},
    ]
    upsert_analyst_actions(rows)

    df = build_features(["FC90"]).set_index("ticker")
    # Goldman (2 spellings) + Morgan Stanley = 2 distinct firms, not 3 rows.
    assert df.loc["FC90", "firm_count_90d"] == 2
