"""Regression tests for the 13F issuer-name to ticker fuzzy match.

The whole point of EDGAR 13F ingestion is to count how many tracked
institutional filers hold each ticker — but that only works if we can map
the `nameOfIssuer` field (e.g. "APPLE INC COM") back to AAPL. Silent
regressions here mean the `Insts` column in the report stays at zero.
"""
from __future__ import annotations

from invest.sources.edgar_src import EdgarSource
from invest.universe import seed_stocks_table, static_universe_entries


def test_normalise_strips_corp_suffixes():
    src = EdgarSource()
    assert src._normalise_name("Apple Inc.") == "apple"
    assert src._normalise_name("Berkshire Hathaway Inc Class B") == "berkshire hathaway"
    assert src._normalise_name("ASML HOLDING N.V.") == "asml holding nv"
    assert src._normalise_name("NOVO NORDISK A/S") == "novo nordisk a/s"


def test_fuzzy_match_resolves_common_issuers():
    """Seed from the static universe and check issuer names resolve."""
    src = EdgarSource()
    lookup = {src._normalise_name(n): t for t, n, *_ in static_universe_entries()}

    cases = [
        ("Apple Inc", "AAPL"),
        ("BERKSHIRE HATHAWAY INC", "BRK-B"),
        ("ASML HOLDING N.V.", "ASML"),
        ("Teva Pharmaceutical Industries Ltd.", "TEVA"),
        ("NOVO NORDISK A/S ADS", "NVO"),
        ("CHECK POINT SOFTWARE TECH", "CHKP"),
        ("NVIDIA CORP", "NVDA"),
        ("Mondelez International", "MDLZ"),
    ]
    for issuer, expected in cases:
        got = src._issuer_to_ticker(issuer, lookup)
        assert got == expected, f"{issuer!r} -> {got}, expected {expected}"


def test_seed_stocks_populates_name_and_sector():
    written = seed_stocks_table()
    assert written >= 200  # we ship ~216 entries

    from sqlalchemy import select

    from invest.db import session_scope
    from invest.models import Stock

    with session_scope() as s:
        rows = s.execute(
            select(Stock).where(Stock.ticker.in_(["AAPL", "TEVA", "ASML", "SMCI"]))
        ).scalars().all()
    by_ticker = {r.ticker: r for r in rows}
    assert by_ticker["AAPL"].name == "Apple Inc."
    assert by_ticker["TEVA"].name.startswith("Teva")
    assert by_ticker["ASML"].sector == "Technology"
    assert by_ticker["SMCI"].name == "Super Micro Computer"
