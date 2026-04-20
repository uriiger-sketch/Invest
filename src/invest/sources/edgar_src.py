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


# Representative list of large institutional filers with their CIKs (zero-padded).
# These are the filers we actively track for 13F signal.
TOP_FILERS: tuple[tuple[str, str], ...] = (
    ("Berkshire Hathaway", "0001067983"),
    ("BlackRock Inc.", "0001364742"),
    ("Vanguard Group", "0000102909"),
    ("State Street Corp", "0000093751"),
    ("Bridgewater Associates", "0001350694"),
    ("Renaissance Technologies", "0001037389"),
    ("Citadel Advisors", "0001423053"),
    ("Point72 Asset Management", "0001603466"),
    ("Tiger Global Management", "0001167483"),
    ("Ark Investment Management", "0001697748"),
    ("Coatue Management", "0001135730"),
    ("D.E. Shaw & Co.", "0001009207"),
    ("Two Sigma Investments", "0001179392"),
    ("Millennium Management", "0001273087"),
    ("Viking Global Investors", "0001103804"),
    ("Baupost Group", "0001061165"),
    ("Pershing Square Capital", "0001336528"),
    ("Third Point", "0001040273"),
    ("Lone Pine Capital", "0001061768"),
    ("Soros Fund Management", "0001029160"),
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
            if ns:
                found = el.find(f"n:{tag}", ns)
            else:
                found = el.find(tag)
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
            ticker_guess = (name or "").split()[0][:16].upper() if name else None
            out.append(
                {
                    "cusip": cusip,
                    "name_of_issuer": name,
                    "ticker": ticker_guess,  # best-effort; a CUSIP→ticker map would be better
                    "shares": shares,
                    "value_usd": value_usd,
                }
            )
        return out

    def ingest_13f(self, tickers: list[str]) -> int:
        """Pull latest 13F-HR for each tracked filer. Only rows whose ticker guess
        intersects our universe are persisted (best-effort match)."""
        universe = {t.upper() for t in tickers}
        written = 0
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
                with session_scope() as s:
                    for r in rows:
                        t = (r.get("ticker") or "").upper()
                        if not t or t not in universe:
                            continue
                        s.merge(
                            Holding13F(
                                filer_cik=cik,
                                filer_name=name,
                                ticker=t,
                                shares=r.get("shares"),
                                value_usd=r.get("value_usd"),
                                quarter=quarter,
                                filing_date=filing_date,
                            )
                        )
                        written += 1
            except TransientSourceError as e:
                logger.warning("edgar 13F %s failed: %s", name, e)
        return written

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
