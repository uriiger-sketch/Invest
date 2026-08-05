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


def test_learned_cusips_persist_and_never_overwrite():
    """CUSIP learning fills BLANK Stock.cusip values only.

    `Stock.cusip` was 0-populated for all 301 tickers in production because
    yfinance has no CUSIP field, which made the CUSIP-first 13F matcher
    match against an empty map forever. We now learn the mapping from the
    filings themselves — but a mis-parsed issuer name must never be able to
    relabel a security that was already identified correctly, so an existing
    CUSIP is left alone.
    """
    from invest.db import session_scope
    from invest.models import Stock

    with session_scope() as s:
        s.add(Stock(ticker="LRNA", name="Learn A Inc.", in_universe=True))
        s.add(Stock(ticker="LRNB", name="Learn B Inc.", cusip="ORIGINAL1", in_universe=True))

    EdgarSource._persist_learned_cusips({"111111111": "LRNA", "999999999": "LRNB"})

    with session_scope() as s:
        a = s.get(Stock, "LRNA")
        b = s.get(Stock, "LRNB")
        assert a.cusip == "111111111", "blank cusip must be filled"
        assert b.cusip == "ORIGINAL1", "existing cusip must NOT be overwritten"


def test_two_pass_cusip_learning_rescues_unmatchable_issuer_names(monkeypatch):
    """The whole point of learning CUSIPs from the filings themselves.

    "AMAZON COM INC" (how many 13F filers spell it) normalises to
    'amazon com', which does not equal Yahoo's 'amazoncom' and does not
    first-token-match either — so name matching drops it, every time. But a
    DIFFERENT filer spells the same CUSIP "AMAZON.COM INC", which does
    match. Pass 1 learns 023135106 -> AMZN from that filer; pass 2 then
    resolves the unmatchable spelling via the learned CUSIP.

    Before this, both fell through to the name matcher and the second
    filer's Amazon position was silently discarded.
    """
    from datetime import date

    from invest.db import session_scope
    from invest.models import Holding13F, Stock

    with session_scope() as s:
        s.add(Stock(ticker="AMZN", name="Amazon.com, Inc.", sector="Consumer Cyclical",
                    in_universe=True))

    src = EdgarSource()
    # Confirm the premise: one spelling matches by name, the other cannot.
    lookup = src._build_name_to_ticker(["AMZN"])
    assert src._issuer_to_ticker("AMAZON.COM INC", lookup) == "AMZN"
    assert src._issuer_to_ticker("AMAZON COM INC", lookup) is None

    per_filer = {
        "0000000001": [{"cusip": "023135106", "name_of_issuer": "AMAZON.COM INC",
                        "shares": 100.0, "value_usd": 1e6}],
        "0000000002": [{"cusip": "023135106", "name_of_issuer": "AMAZON COM INC",
                        "shares": 200.0, "value_usd": 2e6}],
    }
    monkeypatch.setattr(
        "invest.sources.edgar_src.TOP_FILERS",
        (("Filer One", "0000000001"), ("Filer Two", "0000000002")),
    )
    monkeypatch.setattr(src, "_latest_13f_for", lambda cik: ("ACC" + cik, date.today()))
    monkeypatch.setattr(src, "_download_13f_infotable", lambda cik, acc: b"<x/>")
    # _parse_infotable is a plain method; return rows keyed off the accession.
    monkeypatch.setattr(
        src, "_parse_infotable",
        lambda xml: per_filer[src._current_cik],  # set below via _latest_13f_for shim
    )

    # Simpler + less fragile than threading state: drive the download shim to
    # record which filer we're on.
    def _dl(cik, acc):
        src._current_cik = cik
        return b"<x/>"

    monkeypatch.setattr(src, "_download_13f_infotable", _dl)

    src.ingest_13f(["AMZN"])

    with session_scope() as s:
        holders = {h.filer_cik for h in s.query(Holding13F).filter(Holding13F.ticker == "AMZN")}
        learned = s.get(Stock, "AMZN").cusip
    assert holders == {"0000000001", "0000000002"}, (
        "both filers' Amazon positions must land — the second only resolves "
        f"via the learned CUSIP; got {holders}"
    )
    assert learned == "023135106", "the learned CUSIP must persist for future runs"


def test_amendment_forms_are_accepted():
    """A filer whose most recent submission is a 13F-HR/A amendment was
    skipped entirely by the old exact `== "13F-HR"` match, silently losing
    that filer for the quarter. Restatements are common."""
    assert "13F-HR/A" in EdgarSource._13F_FORMS
    assert "13F-HR" in EdgarSource._13F_FORMS
