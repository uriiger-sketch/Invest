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
from ..models import Holding13F, InsiderTrade
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
    ("Capital World Investors", "0000921669"),
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
    ("Citadel Securities", "0001423053"),
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
    rate_per_minute = 300.0  # SEC asks for < 10 req/s; we stay well below

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

    def _latest_13f_for(self, cik: str) -> tuple[str, date] | None:
        """Return (accession_no_no_dashes, filing_date) of the most recent 13F-HR."""
        subs = self._filer_submissions(cik)
        if not subs:
            return None
        recent = subs.get("filings", {}).get("recent", {})
        forms = recent.get("form", [])
        dates = recent.get("filingDate", [])
        accs = recent.get("accessionNumber", [])
        for form, d, acc in zip(forms, dates, accs):
            if form == "13F-HR":
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
        """Pull latest 13F-HR for each tracked filer. Holdings are matched to our
        universe via issuer-name fuzzy match against Stock.name.

        We defensively (re)seed the stocks table from the static universe before
        building the lookup, so the match works even if yfinance fundamentals
        haven't been ingested yet.
        """
        from ..universe import seed_stocks_table

        try:
            seed_stocks_table()
        except Exception as e:  # noqa: BLE001
            logger.warning("seed_stocks_table failed: %s", e)
        lookup = self._build_name_to_ticker(tickers)
        cusip_lookup = self._build_cusip_to_ticker(tickers)
        written = 0
        filers_with_data = 0
        for name, cik in TOP_FILERS:
            try:
                latest = self._latest_13f_for(cik)
                if not latest:
                    continue
                acc, filing_date = latest
                xml = self._download_13f_infotable(cik, acc)
                if not xml:
                    continue
                rows = self._parse_infotable(xml)
                quarter = self._quarter_label(filing_date)
                batch: list[dict] = []
                for r in rows:
                    # CUSIP is the authoritative security identifier and is
                    # already in every infoTable entry. Name matching is a
                    # last resort: 13F legal names ("AMAZON COM INC") rarely
                    # equal Yahoo's ("Amazon.com, Inc."), so it silently
                    # dropped almost everything.
                    t = self._cusip_to_ticker(r.get("cusip"), cusip_lookup) or (
                        self._issuer_to_ticker(r.get("name_of_issuer") or "", lookup)
                    )
                    if not t:
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
            except TransientSourceError as e:
                logger.warning("edgar 13F %s failed: %s", name, e)
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

    _FORM4_DATE = re.compile(r"<updated>(.*?)</updated>")

    def ingest_insider(self, tickers: list[str], lookback_days: int = 120) -> int:
        """Pull a lightweight list of recent Form 4 filings per ticker.

        We do NOT parse each individual filing's XML (heavy). Instead we record
        one "activity" row per filing date as a proxy. Richer parsing is a
        follow-up.
        """
        cutoff = date.today() - timedelta(days=lookback_days)
        written = 0
        for t in tickers:
            try:
                feed = self._insider_feed(t)
            except TransientSourceError as e:
                logger.warning("edgar form4 %s failed: %s", t, e)
                continue
            if not feed:
                continue
            dates: list[date] = []
            for m in self._FORM4_DATE.finditer(feed):
                try:
                    d = datetime.fromisoformat(m.group(1).replace("Z", "+00:00")).date()
                except Exception:  # noqa: BLE001
                    continue
                if d >= cutoff:
                    dates.append(d)
            if not dates:
                continue
            with session_scope() as s:
                for d in dates:
                    s.add(
                        InsiderTrade(
                            ticker=t,
                            filer="(aggregated form-4 activity)",
                            action="activity",
                            shares=None,
                            price=None,
                            date=d,
                        )
                    )
                    written += 1
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
