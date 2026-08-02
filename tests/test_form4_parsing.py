"""Regression tests for real Form 4 parsing.

Form 4 ingest used to write one placeholder row per filing
("(aggregated form-4 activity)", no shares/price/action), which made
`insider_net_buy_90d` permanently zero and `insider_sources` permanently
capped at 1 per ticker (every row shared the identical filer string). These
tests validate the real per-transaction parser against hand-built XML/atom
fixtures shaped exactly like SEC's actual schema, since the sandbox this was
written in has no network access to SEC EDGAR.
"""
from __future__ import annotations

from invest.sources.edgar_src import EdgarSource

_FORM4_XML = b"""<?xml version="1.0"?>
<ownershipDocument>
  <issuer>
    <issuerCik>0000320193</issuerCik>
    <issuerTradingSymbol>AAPL</issuerTradingSymbol>
  </issuer>
  <reportingOwner>
    <reportingOwnerId>
      <rptOwnerCik>0001214156</rptOwnerCik>
      <rptOwnerName>COOK TIMOTHY D</rptOwnerName>
    </reportingOwnerId>
  </reportingOwner>
  <nonDerivativeTable>
    <nonDerivativeTransaction>
      <transactionDate><value>2026-07-15</value></transactionDate>
      <transactionCoding>
        <transactionCode>S</transactionCode>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>50000</value></transactionShares>
        <transactionPricePerShare><value>223.45</value></transactionPricePerShare>
      </transactionAmounts>
    </nonDerivativeTransaction>
    <nonDerivativeTransaction>
      <transactionDate><value>2026-07-14</value></transactionDate>
      <transactionCoding>
        <transactionCode>A</transactionCode>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>10000</value></transactionShares>
        <transactionPricePerShare><value>0</value></transactionPricePerShare>
      </transactionAmounts>
    </nonDerivativeTransaction>
    <nonDerivativeTransaction>
      <transactionDate><value>2026-07-10</value></transactionDate>
      <transactionCoding>
        <transactionCode>P</transactionCode>
      </transactionCoding>
      <transactionAmounts>
        <transactionShares><value>2000</value></transactionShares>
        <transactionPricePerShare><value>210.00</value></transactionPricePerShare>
      </transactionAmounts>
    </nonDerivativeTransaction>
  </nonDerivativeTable>
</ownershipDocument>"""

_ATOM_FEED = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <title>4 - COOK TIMOTHY D (Reporting)</title>
    <link rel="alternate" type="text/html"
          href="https://www.sec.gov/Archives/edgar/data/320193/000032019326000123/0000320193-26-000123-index.htm"/>
    <summary type="html">Filed: 2026-07-15 AccNo: 0000320193-26-000123</summary>
    <updated>2026-07-15T18:30:00-04:00</updated>
    <id>urn:tag:sec.gov,2008:accession-number=0000320193-26-000123</id>
  </entry>
  <entry>
    <title>4 - SOME OTHER PERSON (Reporting)</title>
    <link rel="alternate" type="text/html"
          href="https://www.sec.gov/Archives/edgar/data/320193/000032019326000099/0000320193-26-000099-index.htm"/>
    <updated>2026-06-01T12:00:00-04:00</updated>
    <id>urn:tag:sec.gov,2008:accession-number=0000320193-26-000099</id>
  </entry>
  <entry>
    <title>4 - MALFORMED ENTRY (Reporting)</title>
    <updated>2026-06-02T12:00:00-04:00</updated>
  </entry>
</feed>"""


def test_parses_open_market_transactions_only():
    """P (purchase) and S (sale) survive; A (grant) is compensation
    mechanics and must be excluded so it can't corrupt insider sentiment."""
    rows = EdgarSource._parse_form4_transactions(_FORM4_XML)
    actions = {r["action"] for r in rows}
    assert actions == {"sell", "buy"}
    assert len(rows) == 2

    sell = next(r for r in rows if r["action"] == "sell")
    assert sell["filer"] == "COOK TIMOTHY D"
    assert sell["shares"] == 50000.0
    assert sell["price"] == 223.45

    buy = next(r for r in rows if r["action"] == "buy")
    assert buy["shares"] == 2000.0
    assert buy["price"] == 210.00


def test_parse_form4_transactions_handles_garbage_input():
    assert EdgarSource._parse_form4_transactions(b"not xml at all") == []
    assert EdgarSource._parse_form4_transactions(b"<ownershipDocument></ownershipDocument>") == []


def test_atom_feed_entries_extract_accession_and_issuer_cik():
    """The issuer's numeric CIK must come from the archive URL, not the
    ticker/CIK we searched with (browse-edgar accepts either, but Archives
    paths always use the real numeric CIK).

    `accession` must come back with DASHES STRIPPED. This was wrong once
    already: the atom `<id>` gives the accession WITH dashes
    ("0000320193-26-000123"), but SEC's archive folder naming convention is
    the no-dash form ("000032019326000123") — every document-download URL
    built from the dashed form 404s. Confirmed live: the first deployment
    of Form 4 detail parsing downloaded ZERO documents across 1,320
    attempts, silently (a 404 doesn't raise, so nothing logged) falling
    back to the coarse placeholder for every single filing, because this
    exact test asserted the WRONG (dashed) value and so didn't catch it.
    """
    src = EdgarSource()
    entries = src._parse_form4_entries(_ATOM_FEED)
    # The third entry has no <link>/<id> and must be dropped, not crash.
    assert len(entries) == 2
    assert entries[0]["accession"] == "000032019326000123"
    assert entries[0]["issuer_cik"] == "320193"
    assert entries[1]["accession"] == "000032019326000099"
    assert "-" not in entries[0]["accession"], "accession must be dash-free for the archive URL"


def test_download_url_uses_dash_free_accession(monkeypatch):
    """End-to-end: an accession parsed from the atom feed must produce a
    dash-free URL when handed to the document downloader. This is the
    exact seam where the bug lived — `_parse_form4_entries` and
    `_download_form4_primary_doc` were both individually "correct" in
    isolation (and individually tested), but the value handed between them
    had dashes the downstream URL-building code never expected."""
    src = EdgarSource()
    entries = src._parse_form4_entries(_ATOM_FEED)
    requested_urls = []

    def _fake_get_json(url):
        requested_urls.append(url)
        return None  # doesn't matter for this test — we only check the URL

    monkeypatch.setattr(src, "_get_json", _fake_get_json)
    src._download_form4_primary_doc(entries[0]["issuer_cik"], entries[0]["accession"])
    assert requested_urls, "the downloader never called _get_json"
    assert "/000032019326000123/" in requested_urls[0]
    assert "-" not in requested_urls[0].split("/data/")[1], (
        f"accession in URL still has dashes: {requested_urls[0]}"
    )


def test_top_filers_have_no_duplicate_ciks():
    """Two entries previously shared a CIK (Capital World Investors / Icahn
    Enterprises both under 0000921669; Citadel Advisors / Citadel Securities
    both under 0001423053), which silently mislabels one real filer's
    holdings under a second firm's name on every re-crawl (the upsert key is
    (filer_cik, ticker, quarter), so whichever name runs last in the list
    wins the display name for that CIK's data)."""
    from invest.sources.edgar_src import TOP_FILERS

    ciks = [cik for _, cik in TOP_FILERS]
    dupes = {c for c in ciks if ciks.count(c) > 1}
    assert not dupes, f"duplicate CIKs in TOP_FILERS: {dupes}"
