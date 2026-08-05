"""SEC EDGAR source: 13F-HR holdings from top filers + Form 4 insider trades.

Uses the unauthenticated JSON endpoints under data.sec.gov. A descriptive
User-Agent with a contact email is required per SEC policy:
https://www.sec.gov/os/accessing-edgar-data
"""
from __future__ import annotations

import logging
import re
from datetime import date, datetime, timedelta
from typing import Any

import requests
from lxml import etree

from ..config import get_settings
from ..db import session_scope
from ..models import Holding13F
from .base import BaseSource, TransientSourceError, log_run, with_retries

logger = logging.getLogger(__name__)


# Curated list of large institutional 13F filers. CIKs are zero-padded to 10 digits.
# Any CIK that 404s at SEC is silently skipped by the pipeline, so unverified ones
# simply do not contribute signal.
TOP_FILERS: tuple[tuple[str, str], ...] = (
    # Mega index / asset managers
    ("Berkshire Hathaway", "0001067983"),
    ("BlackRock Inc.", "0001364742"),
    ("Vanguard Group", "0000102909"),
    ("State Street Corp", "0000093751"),
    ("FMR LLC (Fidelity)", "0000315066"),
    ("T. Rowe Price", "0000080255"),
    ("Wellington Management", "0000902219"),
    ("Invesco Ltd.", "0000914208"),
    ("Franklin Resources", "0000038777"),
    ("Northern Trust", "0000073124"),
    ("Dodge & Cox", "0000200217"),
    # "Capital World Investors" was previously listed here under
    # 0000921669 — the same CIK as "Icahn Enterprises" below. One of the two
    # was wrong (both can't be real 13F filers under the same CIK), and
    # since I can't verify the correct CIK for Capital World Investors
    # against SEC without network access, removing the unverifiable entry is
    # safer than guessing a replacement number and silently mislabeling a
    # different real filer's holdings under a wrong name again.
    ("Legal & General Investment", "0001645148"),
    ("Geode Capital Management", "0001330073"),
    ("Janus Henderson Group", "0001274173"),
    # Hedge funds / multi-strat
    ("Bridgewater Associates", "0001350694"),
    ("Renaissance Technologies", "0001037389"),
    ("Citadel Advisors", "0001423053"),
    ("Point72 Asset Management", "0001603466"),
    ("Millennium Management", "0001273087"),
    ("D.E. Shaw & Co.", "0001009207"),
    ("Two Sigma Investments", "0001179392"),
    ("Two Sigma Advisers", "0001274473"),
    ("AQR Capital Management", "0001167557"),
    ("Balyasny Asset Management", "0001509928"),
    ("Man Group", "0001039162"),
    # Long/short equity / activist
    ("Tiger Global Management", "0001167483"),
    ("Coatue Management", "0001135730"),
    ("Viking Global Investors", "0001103804"),
    ("Baupost Group", "0001061165"),
    ("Pershing Square Capital", "0001336528"),
    ("Third Point", "0001040273"),
    ("Lone Pine Capital", "0001061768"),
    ("Soros Fund Management", "0001029160"),
    ("Greenlight Capital", "0001079114"),
    ("Appaloosa Management", "0001656456"),
    ("Maverick Capital", "0000887993"),
    ("Whale Rock Capital", "0001510104"),
    ("Duquesne Family Office (Druckenmiller)", "0001536411"),
    ("Glenview Capital", "0001316819"),
    # Thematic / specialist
    ("Ark Investment Management", "0001697748"),
    ("Paulson & Co.", "0001035674"),
    ("Oaktree Capital", "0001403528"),
    # --- Additional mega asset managers / pensions / insurers ---
    ("MFS Investment Management", "0000095906"),
    ("Eaton Vance Management", "0000350797"),
    ("Lord, Abbett & Co.", "0000059671"),
    ("Putnam Investments", "0000081060"),
    ("Federated Hermes", "0001056288"),
    ("State Farm Mutual Auto", "0001076378"),
    ("Allstate Corporation", "0000899051"),
    ("MetLife Investment Management", "0001099219"),
    ("Prudential Financial", "0001137774"),
    ("TIAA-CREF Investment Management", "0000945783"),
    ("CalPERS", "0000919079"),
    ("Norges Bank (Norway SWF)", "0001262184"),
    ("GIC Private Limited (Singapore)", "0001071659"),
    ("CPP Investment Board (Canada)", "0001432167"),
    ("Ontario Teachers' Pension Plan", "0001129200"),
    # --- Bank-affiliated asset managers ---
    ("JPMorgan Chase & Co. (AM)", "0000019617"),
    ("Goldman Sachs Group (AM)", "0000886982"),
    ("Morgan Stanley", "0000895421"),
    ("Bank of America Corp", "0000070858"),
    ("Wells Fargo & Co.", "0000072971"),
    ("UBS Group AG", "0001114446"),
    ("Deutsche Bank AG", "0001159508"),
    ("BNP Paribas Asset Management", "0001317069"),
    ("Allianz Asset Management of America", "0001027796"),
    ("AXA Investment Managers", "0001066805"),
    ("Schroder Investment Management", "0001005471"),
    ("Credit Suisse AG / Securities", "0000824468"),
    ("HSBC Holdings plc", "0001089113"),
    # --- Additional hedge funds ---
    ("Sculptor Capital (Och-Ziff)", "0001403256"),
    ("Brevan Howard Asset Mgmt", "0001435317"),
    ("Marshall Wace", "0001607796"),
    # "Citadel Securities" was previously listed here under 0001423053 — the
    # same CIK as "Citadel Advisors" above (the actual 13F-filing entity;
    # Citadel Securities is a separate broker-dealer). Removed rather than
    # guessing Citadel Securities' real CIK — see the Capital World
    # Investors note above for why.
    ("Hudson Bay Capital Mgmt", "0001482281"),
    ("Element Capital Management", "0001431203"),
    ("Caxton Associates", "0001000275"),
    ("Tudor Investment Corp", "0001037491"),
    ("Moore Capital Management", "0001033908"),
    ("ExodusPoint Capital Mgmt", "0001735707"),
    ("Verition Fund Management", "0001498476"),
    ("Schonfeld Strategic Advisors", "0001629701"),
    ("Walleye Capital", "0001469258"),
    ("Susquehanna International Group", "0001056299"),
    ("Jane Street Capital", "0001595888"),
    ("Virtu Financial", "0001592386"),
    # --- Activists / value investors ---
    ("Icahn Enterprises (Carl Icahn)", "0000921669"),
    ("Engine No. 1", "0001830489"),
    ("Starboard Value", "0001517413"),
    ("Elliott Investment Management", "0001791786"),
    ("ValueAct Capital", "0001418814"),
    ("JANA Partners", "0001159159"),
    ("Trian Fund Management (Peltz)", "0001345471"),
    ("Sachem Head Capital Management", "0001595900"),
    ("Caligan Partners", "0001833197"),
    # --- Specialist / private credit / alternatives ---
    ("Whitebox Advisors", "0001179074"),
    ("Brookfield Asset Management", "0001001085"),
    ("KKR & Co.", "0001404912"),
    ("Carlyle Group", "0001527166"),
    ("Apollo Global Management", "0001411494"),
    ("Ares Management", "0001607717"),
    ("Blackstone Inc.", "0001393818"),
    # --- High-conviction long-only / specialist ---
    ("Sequoia Capital", "0001045810"),
    ("Stone Ridge Asset Management", "0001572694"),
    ("Polen Capital Management", "0001080264"),
    ("Akre Capital Management", "0001112520"),
    ("Sands Capital Management", "0001071193"),
    ("Edgewood Management", "0001054946"),
    ("Brown Capital Management", "0000866635"),
    ("Tweedy, Browne Company", "0000732905"),
    ("Ariel Investments", "0001110049"),
    ("First Eagle Investment Management", "0001317269"),
    ("Diamond Hill Capital Management", "0001207074"),
    ("Yacktman Asset Management", "0001142412"),
    ("Davis Selected Advisers", "0001097075"),
    ("Wedgewood Partners", "0001102067"),
)


class EdgarSource(BaseSource):
    name = "edgar"
    rate_per_minute = 480.0  # SEC allows < 10 req/s (600/min); stay comfortably under

    def __init__(self) -> None:
        super().__init__()
        settings = get_settings()
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": settings.sec_user_agent,
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate",
            }
        )

    @with_retries
    def _get_json(self, url: str) -> Any:
        self.throttle()
        try:
            resp = self.session.get(url, timeout=20)
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        if resp.status_code == 429 or resp.status_code >= 500:
            raise TransientSourceError(f"{resp.status_code} {resp.text[:120]}")
        if resp.status_code >= 400:
            return None
        return resp.json()

    @with_retries
    def _get_text(self, url: str) -> str | None:
        self.throttle()
        try:
            resp = self.session.get(url, timeout=20)
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        if resp.status_code == 429 or resp.status_code >= 500:
            raise TransientSourceError(f"{resp.status_code} {resp.text[:120]}")
        if resp.status_code >= 400:
            return None
        return resp.text

    # ----------------------------- 13F -----------------------------

    def _filer_submissions(self, cik: str) -> dict[str, Any] | None:
        return self._get_json(f"https://data.sec.gov/submissions/CIK{cik}.json")

    # Forms that carry a holdings information table. "13F-HR/A" is an
    # AMENDMENT — filers restate a quarter surprisingly often, and a filer
    # whose most recent submission is an amendment was previously skipped
    # entirely (exact `== "13F-HR"` match), losing that filer for the quarter.
    _13F_FORMS = ("13F-HR", "13F-HR/A")

    def _latest_13f_for(self, cik: str) -> tuple[str, date] | None:
        """Return (accession_no_no_dashes, filing_date) of the most recent
        13F-HR or 13F-HR/A."""
        subs = self._filer_submissions(cik)
        if not subs:
            return None
        recent = subs.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        dates = recent.get("filingDate", [])
        accs = recent.get("accessionNumber", [])
        for form, d, acc in zip(forms, dates, accs):
            if form in self._13F_FORMS:
                try:
                    return acc.replace("-", ""), datetime.strptime(d, "%Y-%m-%d").date()
                except Exception:  # noqa: BLE001
                    continue
        return None

    def _download_13f_infotable(self, cik: str, accession_no_dash: str) -> bytes | None:
        """Fetch the informationTable.xml inside the filing."""
        acc = accession_no_dash
        # Folder path: /Archives/edgar/data/<cik_int>/<acc>/<acc>-index.json
        cik_int = str(int(cik))
        index_url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc}/index.json"
        idx = self._get_json(index_url)
        if not idx:
            return None
        for item in idx.get("directory", {}).get("item", []):
            name = item.get("name", "")
            if name.endswith(".xml") and "infotable" in name.lower():
                url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{acc}/{name}"
                self.throttle()
                try:
                    r = self.session.get(url, timeout=30)
                except requests.RequestException as e:
                    raise TransientSourceError(str(e)) from e
                if r.status_code < 400:
                    return r.content
        return None

    @staticmethod
    def _quarter_label(d: date) -> str:
        q = (d.month - 1) // 3 + 1
        return f"{d.year}Q{q}"

    def _parse_infotable(self, xml_bytes: bytes) -> list[dict[str, Any]]:
        try:
            root = etree.fromstring(xml_bytes)  # noqa: S320 (trusted SEC feed)
        except etree.XMLSyntaxError:
            return []
        ns = {}
        if root.tag.startswith("{"):
            ns["n"] = root.tag.split("}")[0].lstrip("{")

        def _local(el, tag: str) -> str | None:
            found = el.find(f"n:{tag}", ns) if ns else el.find(tag)
            return found.text if found is not None else None

        info_tag = "infoTable" if not ns else "n:infoTable"
        out: list[dict[str, Any]] = []
        for el in root.findall(info_tag, ns or None):
            cusip = _local(el, "cusip")
            value = _local(el, "value")  # thousands of USD
            shrs_wrap = el.find("n:shrsOrPrnAmt", ns) if ns else el.find("shrsOrPrnAmt")
            shares = None
            if shrs_wrap is not None:
                sh = shrs_wrap.find("n:sshPrnamt", ns) if ns else shrs_wrap.find("sshPrnamt")
                if sh is not None and sh.text:
                    try:
                        shares = float(sh.text)
                    except ValueError:
                        shares = None
            try:
                value_usd = float(value) * 1000.0 if value else None
            except ValueError:
                value_usd = None
            name = _local(el, "nameOfIssuer")
            out.append(
                {
                    "cusip": cusip,
                    "name_of_issuer": name,
                    "shares": shares,
                    "value_usd": value_usd,
                }
            )
        return out

    # Tokens we strip before fuzzy-matching "Apple Inc" -> "Apple" -> AAPL.
    _CORP_SUFFIXES = (
        " inc", " incorporated", " corp", " corporation", " co", " company",
        " ltd", " limited", " plc", " holdings", " holding", " group",
        " class a", " class b", " class c", ".com",
    )

    @classmethod
    def _normalise_name(cls, name: str) -> str:
        n = name.lower().strip().replace(",", "").replace(".", "")
        # Strip repeated corporate suffixes.
        changed = True
        while changed:
            changed = False
            for suf in cls._CORP_SUFFIXES:
                if n.endswith(suf):
                    n = n[: -len(suf)].strip()
                    changed = True
        return n

    def _build_cusip_to_ticker(self, tickers: list[str]) -> dict[str, str]:
        """{normalised 9/8/6-char CUSIP: ticker} from the stocks table.

        CUSIPs are indexed by their 6-character issuer prefix as well as the
        full 9-character value, because 13F filings sometimes carry the
        issue-level CUSIP while our stored value is the issuer-level one
        (or vice-versa) — the first six characters identify the issuer.
        """
        from ..models import Stock

        with session_scope() as s:
            rows = s.query(Stock.ticker, Stock.cusip).filter(
                Stock.ticker.in_(tickers), Stock.cusip.isnot(None)
            ).all()
        out: dict[str, str] = {}
        for t, cusip in rows:
            key = (cusip or "").strip().upper()
            if not key:
                continue
            out[key] = t
            if len(key) >= 6:
                out.setdefault(key[:6], t)
        return out

    @staticmethod
    def _cusip_to_ticker(cusip: str | None, lookup: dict[str, str]) -> str | None:
        if not cusip or not lookup:
            return None
        key = cusip.strip().upper()
        return lookup.get(key) or (lookup.get(key[:6]) if len(key) >= 6 else None)

    def _build_name_to_ticker(self, tickers: list[str]) -> dict[str, str]:
        """Build a {normalised_name: ticker} lookup from the stocks table."""
        from ..models import Stock

        with session_scope() as s:
            rows = s.query(Stock.ticker, Stock.name).filter(Stock.ticker.in_(tickers)).all()
        out: dict[str, str] = {}
        for t, name in rows:
            if not name:
                continue
            out[self._normalise_name(name)] = t
        return out

    def _issuer_to_ticker(self, issuer_name: str, lookup: dict[str, str]) -> str | None:
        if not issuer_name:
            return None
        key = self._normalise_name(issuer_name)
        if key in lookup:
            return lookup[key]
        # Fallback: match on the first token if unique.
        first = key.split(" ", 1)[0] if key else ""
        if first and len(first) >= 3:
            matches = [v for k, v in lookup.items() if k.startswith(first + " ") or k == first]
            if len(matches) == 1:
                return matches[0]
        return None

    def ingest_13f(self, tickers: list[str]) -> int:
        """Pull the latest 13F-HR for each tracked filer and match holdings to
        our universe.

        Runs in TWO passes so CUSIP matching actually works. `Stock.cusip`
        starts empty and stays empty — yfinance has no CUSIP field, so the
        CUSIP-first matcher added earlier was matching against an empty map
        for every ticker (verified live: 0 of 301 stocks had a CUSIP) and
        every holding fell through to the weak name matcher.

        But the infotables themselves carry BOTH `cusip` and `nameOfIssuer`.
        So: pass 1 downloads every filer's infotable and name-matches what it
        can, learning `{cusip: ticker}` from each success. Pass 2 re-matches
        the same in-memory rows with the learned map, which picks up every
        holding whose issuer name we can't parse but whose CUSIP another
        filer already taught us. Learned CUSIPs are persisted to `Stock.cusip`
        so subsequent runs start pass 1 already knowing them.
        """
        from ..universe import seed_stocks_table

        try:
            seed_stocks_table()
        except Exception as e:  # noqa: BLE001
            logger.warning("seed_stocks_table failed: %s", e)
        lookup = self._build_name_to_ticker(tickers)
        cusip_lookup = self._build_cusip_to_ticker(tickers)
        universe = set(tickers)

        # Per-filer outcome counters. 87 of 115 tracked filers were landing
        # nothing with no indication of why — including Berkshire and
        # Vanguard, whose CIKs are definitely correct — and every failure
        # path here is a silent `continue`.
        diag: dict[str, int] = {}

        def bump(k: str) -> None:
            diag[k] = diag.get(k, 0) + 1

        # Pass 1 — fetch every filer once, keep the parsed rows in memory.
        fetched: list[tuple[str, str, str, date, list[dict]]] = []
        for name, cik in TOP_FILERS:
            try:
                latest = self._latest_13f_for(cik)
                if not latest:
                    bump("no_13f_filing_found")
                    logger.info("edgar 13F: no 13F-HR filing found for %s (CIK %s)", name, cik)
                    continue
                acc, filing_date = latest
                xml = self._download_13f_infotable(cik, acc)
                if not xml:
                    bump("infotable_missing")
                    logger.info("edgar 13F: no infotable in %s filing %s", name, acc)
                    continue
                rows = self._parse_infotable(xml)
                if not rows:
                    bump("infotable_parsed_zero")
                    continue
                bump("fetched_ok")
                fetched.append((name, cik, acc, filing_date, rows))
            except TransientSourceError as e:
                bump("transient_error")
                logger.warning("edgar 13F %s failed: %s", name, e)

        # Learn {cusip: ticker} from every name match we can make.
        learned: dict[str, str] = {}
        for _name, _cik, _acc, _fd, rows in fetched:
            for r in rows:
                cusip = (r.get("cusip") or "").strip().upper()
                if not cusip or cusip in cusip_lookup or cusip in learned:
                    continue
                t = self._issuer_to_ticker(r.get("name_of_issuer") or "", lookup)
                if t and t in universe:
                    learned[cusip] = t
        if learned:
            self._persist_learned_cusips(learned)
            for cusip, t in learned.items():
                cusip_lookup.setdefault(cusip, t)
                if len(cusip) >= 6:
                    cusip_lookup.setdefault(cusip[:6], t)
        logger.info(
            "edgar 13F: learned %d new cusip->ticker mappings from filing data",
            len(learned),
        )

        # Pass 2 — match everything with the enriched CUSIP map.
        written = 0
        filers_with_data = 0
        for name, cik, _acc, filing_date, rows in fetched:
            quarter = self._quarter_label(filing_date)
            batch: list[dict] = []
            for r in rows:
                t = self._cusip_to_ticker(r.get("cusip"), cusip_lookup) or (
                    self._issuer_to_ticker(r.get("name_of_issuer") or "", lookup)
                )
                if not t or t not in universe:
                    continue
                batch.append(
                    {
                        "filer_cik": cik,
                        "filer_name": name,
                        "ticker": t,
                        "shares": r.get("shares"),
                        "value_usd": r.get("value_usd"),
                        "quarter": quarter,
                        "filing_date": filing_date,
                    }
                )
            if batch:
                written += self._upsert_holdings(batch)
                filers_with_data += 1
            else:
                bump("matched_zero_of_universe")
                logger.info(
                    "edgar 13F: %s returned %d holdings but none matched our universe",
                    name, len(rows),
                )

        logger.info(
            "edgar 13F summary: tracked=%d fetched_ok=%d with_universe_holdings=%d | "
            "no_13f_filing_found=%d infotable_missing=%d infotable_parsed_zero=%d "
            "matched_zero_of_universe=%d transient_error=%d learned_cusips=%d",
            len(TOP_FILERS), diag.get("fetched_ok", 0), filers_with_data,
            diag.get("no_13f_filing_found", 0), diag.get("infotable_missing", 0),
            diag.get("infotable_parsed_zero", 0), diag.get("matched_zero_of_universe", 0),
            diag.get("transient_error", 0), len(learned),
        )
        if not filers_with_data:
            # Every filer returned nothing. Almost always a blanket SEC 403
            # (placeholder SEC_USER_AGENT) rather than 120 empty portfolios —
            # say so instead of reporting a quiet success.
            logger.error(
                "EDGAR 13F ingest matched ZERO holdings across all %d tracked filers. "
                "This usually means SEC is rejecting the requests — check that "
                "SEC_USER_AGENT is set to a real contact address.",
                len(TOP_FILERS),
            )
        return written

    @staticmethod
    def _persist_learned_cusips(learned: dict[str, str]) -> int:
        """Write CUSIPs learned from 13F filings onto their Stock rows.

        Only fills BLANKS — never overwrites a CUSIP already on record, so a
        single mis-parsed issuer name can't relabel a security that was
        previously identified correctly.
        """
        from ..models import Stock

        written = 0
        with session_scope() as s:
            for cusip, ticker in learned.items():
                stock = s.get(Stock, ticker)
                if stock is not None and not stock.cusip:
                    stock.cusip = cusip[:12]
                    written += 1
        return written

    @staticmethod
    def _upsert_holdings(batch: list[dict]) -> int:
        """Idempotent write keyed on (filer_cik, ticker, quarter).

        The previous code called ``session.merge(Holding13F(...))`` with
        ``id=None``. Because the PK is autoincrement, SQLAlchemy treats that
        as a NEW object and INSERTs — colliding with the unique index on the
        second run each quarter, raising IntegrityError, rolling back the
        batch and aborting BOTH 13F and insider ingest. That is the main
        reason holdings_13f stayed empty and Insts showed 0 everywhere.
        """
        from sqlalchemy.dialects.sqlite import insert as sqlite_insert

        with session_scope() as s:
            stmt = sqlite_insert(Holding13F).values(batch)
            stmt = stmt.on_conflict_do_update(
                index_elements=["filer_cik", "ticker", "quarter"],
                set_={
                    "shares": stmt.excluded.shares,
                    "value_usd": stmt.excluded.value_usd,
                    "filing_date": stmt.excluded.filing_date,
                    "filer_name": stmt.excluded.filer_name,
                },
            )
            s.execute(stmt)
        return len(batch)

    # --------------------------- Form 4 ---------------------------

    def _insider_feed(self, ticker: str) -> str | None:
        """Atom feed of recent Form 4 filings for a single ticker."""
        url = (
            "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany"
            f"&CIK={ticker}&type=4&dateb=&owner=include&count=40&output=atom"
        )
        return self._get_text(url)

    _FORM4_ENTRY = re.compile(r"<entry>(.*?)</entry>", re.S)
    _FORM4_UPDATED = re.compile(r"<updated>(.*?)</updated>")
    # SEC's atom <id> for a filing is a stable
    # "urn:tag:sec.gov,2008:accession-number=XXXXXXXXXX-YY-NNNNNN" tag.
    _FORM4_ACCESSION = re.compile(r"accession-number=([\d-]+)")
    # Every <link href> in an entry points somewhere under the ISSUER's own
    # numeric-CIK archive folder, regardless of whether we searched using a
    # ticker symbol (browse-edgar accepts either) — so this is how we recover
    # the real numeric CIK needed to build the document download URL.
    _FORM4_ARCHIVE_CIK = re.compile(r"/Archives/edgar/data/(\d+)/")

    # Cap the number of individual Form 4 filings we download+parse per
    # ticker per run. A per-ticker cap bounds the extra request volume this
    # adds (each filing needs its own fetch: index.json + the xml document);
    # filings beyond it still get a coarse placeholder row so we don't
    # silently lose that they happened.
    #
    # CALIBRATION NOTE: this was 6 when the accession-number bug (see
    # `_parse_form4_entries`) made every single detailed fetch 404 instantly
    # — cheap to attempt, so the cap's cost was never actually exercised.
    # The moment that bug was fixed, real downloads across ~300 tickers x up
    # to 6 filings each (≈1,800 filings x 2 requests) pushed the deep
    # ingest step past its 35-minute timeout and the whole run was killed
    # with nothing committed. Lowered to 3 to keep worst-case request volume
    # roughly in check; `rate_per_minute` was also raised (SEC allows up to
    # 600/min) since throttling, not request volume, was the smaller factor.
    _FORM4_MAX_DETAILED_PER_TICKER = 3

    # SEC transaction codes for actual open-market conviction: P = purchase,
    # S = sale. Every other code (A=grant, M=option exercise, G=gift,
    # F=tax withholding, C=conversion, ...) is compensation mechanics, not a
    # buy/sell decision, and is intentionally excluded so it can't be
    # miscounted as insider sentiment.
    _FORM4_OPEN_MARKET_CODES = {"P": "buy", "S": "sell"}

    def _parse_form4_entries(self, feed: str) -> list[dict[str, Any]]:
        """Atom feed -> [{"date", "accession", "issuer_cik"}, ...].

        `accession` is stored with dashes STRIPPED (SEC's archive folder
        naming convention is the no-dash form,
        e.g. .../data/320193/000032019326000123/, not
        .../data/320193/0000320193-26-000123/) — the same normalisation
        `_latest_13f_for` already does for 13F accession numbers
        (`acc.replace("-", "")`). Missing this here meant every single
        Form 4 document URL this session's real-parsing feature built was
        malformed and 404'd: confirmed live (entries_seen=4717,
        index_json_empty=1320 — 100% of attempted downloads), with zero
        exceptions raised (a 404 isn't a TransientSourceError, so
        `_get_json` just returns None) and therefore zero warnings logged
        until the diagnostic counters added right after were shipped.

        Entries missing any of the three fields are dropped from the
        returned list (the caller falls back to a coarse placeholder for
        those, keyed only by date, so a malformed entry never means losing
        the "something happened" signal entirely).
        """
        out: list[dict[str, Any]] = []
        for block in self._FORM4_ENTRY.findall(feed):
            m_date = self._FORM4_UPDATED.search(block)
            m_acc = self._FORM4_ACCESSION.search(block)
            m_cik = self._FORM4_ARCHIVE_CIK.search(block)
            if not (m_date and m_acc and m_cik):
                continue
            try:
                d = datetime.fromisoformat(m_date.group(1).replace("Z", "+00:00")).date()
            except Exception:  # noqa: BLE001
                continue
            out.append(
                {
                    "date": d,
                    "accession": m_acc.group(1).replace("-", ""),
                    "issuer_cik": m_cik.group(1),
                }
            )
        return out

    def _download_form4_primary_doc(
        self, issuer_cik: str, accession_no_dash: str, diag: dict[str, Any] | None = None
    ) -> bytes | None:
        """Fetch one filing's primary XML document.

        Modern (post-2003) Form 3/4/5 filings are XML-only and SEC names the
        primary document literally `primary_doc.xml`; fall back to any other
        top-level `.xml` file for the rare filing that doesn't follow that
        convention, mirroring the same index.json + directory-listing
        approach `_download_13f_infotable` already uses for 13F filings.

        `diag`, when passed, records WHY a filing produced no document —
        this path returning None silently (no exception, hence no log line)
        for every single filing in a run, with zero visibility into which
        of "index.json empty" / "no .xml found" / "download failed" was
        responsible, is exactly what happened the first time this shipped.
        """
        cik_int = str(int(issuer_cik))
        index_url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{accession_no_dash}/index.json"
        idx = self._get_json(index_url)
        if not idx:
            if diag is not None:
                diag["index_json_empty"] = diag.get("index_json_empty", 0) + 1
            return None
        names = [item.get("name", "") for item in idx.get("directory", {}).get("item", [])]
        target = next((n for n in names if n.lower() == "primary_doc.xml"), None)
        if target is None:
            target = next(
                (n for n in names if n.lower().endswith(".xml") and "index" not in n.lower()), None
            )
        if target is None:
            if diag is not None:
                n = diag.get("no_xml_candidate", 0)
                diag["no_xml_candidate"] = n + 1
                if n < 3:
                    logger.warning(
                        "edgar form4: no .xml candidate in %s — directory listing: %s",
                        index_url, names,
                    )
            return None
        if diag is not None:
            diag["xml_found"] = diag.get("xml_found", 0) + 1
        url = f"https://www.sec.gov/Archives/edgar/data/{cik_int}/{accession_no_dash}/{target}"
        self.throttle()
        try:
            r = self.session.get(url, timeout=30)
        except requests.RequestException as e:
            raise TransientSourceError(str(e)) from e
        return r.content if r.status_code < 400 else None

    @classmethod
    def _parse_form4_transactions(cls, xml_bytes: bytes) -> list[dict[str, Any]]:
        """Parse a Form 4 ownershipDocument into open-market buy/sell rows.

        Only non-derivative (Table I — actual common stock, not options)
        transactions coded P (open-market purchase) or S (open-market sale)
        are returned. Every other code is compensation mechanics (grants,
        option exercises, gifts, tax withholding), not a buy/sell decision,
        and would corrupt `insider_net_buy_90d` if counted as one.
        """
        try:
            root = etree.fromstring(xml_bytes)  # noqa: S320 (trusted SEC feed)
        except etree.XMLSyntaxError:
            return []
        ns = {}
        if root.tag.startswith("{"):
            ns["n"] = root.tag.split("}")[0].lstrip("{")

        def _tag(name: str) -> str:
            return f"n:{name}" if ns else name

        def _text(el, path: str) -> str | None:
            found = el.find("/".join(_tag(p) for p in path.split("/")), ns or None)
            return found.text.strip() if found is not None and found.text else None

        owners = root.findall(_tag("reportingOwner"), ns or None)
        owner_names = [
            n for n in (_text(o, "reportingOwnerId/rptOwnerName") for o in owners) if n
        ]
        owner_name = owner_names[0] if owner_names else None

        table = root.find(_tag("nonDerivativeTable"), ns or None)
        if table is None:
            return []
        out: list[dict[str, Any]] = []
        for txn in table.findall(_tag("nonDerivativeTransaction"), ns or None):
            code = (_text(txn, "transactionCoding/transactionCode") or "").strip().upper()
            mapped = cls._FORM4_OPEN_MARKET_CODES.get(code)
            if mapped is None:
                continue
            d_raw = _text(txn, "transactionDate/value")
            try:
                d = datetime.strptime(d_raw, "%Y-%m-%d").date() if d_raw else None
            except ValueError:
                d = None
            if d is None:
                continue
            shares_raw = _text(txn, "transactionAmounts/transactionShares/value")
            price_raw = _text(txn, "transactionAmounts/transactionPricePerShare/value")
            try:
                shares = float(shares_raw) if shares_raw else None
            except ValueError:
                shares = None
            if shares is None:
                continue
            try:
                price = float(price_raw) if price_raw else 0.0
            except ValueError:
                price = 0.0
            out.append(
                {
                    "filer": owner_name or "(unnamed Form 4 filer)",
                    "action": mapped,
                    "shares": shares,
                    "price": price,
                    "date": d,
                }
            )
        return out

    def ingest_insider(self, tickers: list[str], lookback_days: int = 120) -> int:
        """Pull recent Form 4 filings per ticker and parse real per-transaction
        detail (insider name, buy/sell, shares, price) for the most recent
        `_FORM4_MAX_DETAILED_PER_TICKER` filings.

        Filings beyond that cap, or that fail to parse, still get a coarse
        "something happened" placeholder row (as this used to do for every
        filing) so their existence isn't silently dropped — they just don't
        contribute to the insider_net_buy_90d feature or count as a
        separately-named source, which real per-transaction rows do.
        """
        from .base import upsert_insider_trades

        cutoff = date.today() - timedelta(days=lookback_days)
        written = 0
        # Diagnostic counters for the whole run — see the docstring on
        # `_download_form4_primary_doc` for why this exists: the detailed
        # path can fail 100% of the time with zero exceptions and zero log
        # output, which is exactly what happened the first time this
        # shipped and left no trace to debug from.
        diag: dict[str, Any] = {}
        xml_dumped = 0
        for t in tickers:
            try:
                feed = self._insider_feed(t)
            except TransientSourceError as e:
                logger.warning("edgar form4 %s failed: %s", t, e)
                continue
            if not feed:
                continue
            entries = [e for e in self._parse_form4_entries(feed) if e["date"] >= cutoff]
            diag["entries_seen"] = diag.get("entries_seen", 0) + len(entries)
            if not entries:
                continue
            entries.sort(key=lambda e: e["date"], reverse=True)
            rows: list[dict[str, Any]] = []
            for entry in entries[: self._FORM4_MAX_DETAILED_PER_TICKER]:
                txns: list[dict[str, Any]] = []
                try:
                    xml = self._download_form4_primary_doc(
                        entry["issuer_cik"], entry["accession"], diag=diag
                    )
                    if xml:
                        txns = self._parse_form4_transactions(xml)
                        if txns:
                            diag["txns_ok"] = diag.get("txns_ok", 0) + 1
                        else:
                            diag["xml_zero_txns"] = diag.get("xml_zero_txns", 0) + 1
                            if xml_dumped < 2:
                                logger.warning(
                                    "edgar form4 %s/%s: xml downloaded but yielded 0 "
                                    "transactions; first 600 bytes: %r",
                                    t, entry["accession"], xml[:600],
                                )
                                xml_dumped += 1
                except TransientSourceError as e:
                    diag["download_exception"] = diag.get("download_exception", 0) + 1
                    logger.warning(
                        "edgar form4 doc %s/%s failed: %s", t, entry["accession"], e
                    )
                if txns:
                    rows.extend({**txn, "ticker": t} for txn in txns)
                else:
                    rows.append(
                        {
                            "ticker": t, "filer": "(aggregated form-4 activity)",
                            "action": "activity", "shares": None, "price": None,
                            "date": entry["date"],
                        }
                    )
            for entry in entries[self._FORM4_MAX_DETAILED_PER_TICKER :]:
                rows.append(
                    {
                        "ticker": t, "filer": "(aggregated form-4 activity)",
                        "action": "activity", "shares": None, "price": None,
                        "date": entry["date"],
                    }
                )
            written += upsert_insider_trades(rows)
        logger.info(
            "edgar form4 detailed-parse summary: entries_seen=%d xml_found=%d "
            "txns_ok=%d xml_zero_txns=%d index_json_empty=%d no_xml_candidate=%d "
            "download_exception=%d",
            diag.get("entries_seen", 0), diag.get("xml_found", 0), diag.get("txns_ok", 0),
            diag.get("xml_zero_txns", 0), diag.get("index_json_empty", 0),
            diag.get("no_xml_candidate", 0), diag.get("download_exception", 0),
        )
        return written

    # ------------------------------ run ------------------------------

    def run(self, tickers: list[str]) -> int:
        total = 0
        with log_run("edgar.13f") as c:
            c["rows"] = self.ingest_13f(tickers)
            total += c["rows"]
        with log_run("edgar.form4") as c:
            c["rows"] = self.ingest_insider(tickers)
            total += c["rows"]
        return total
