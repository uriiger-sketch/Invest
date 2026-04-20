"""Universe of tickers to track.

Data is a list of (ticker, name, sector, region) tuples so we can:
  1. Drive the crawl with the ticker column.
  2. Seed `stocks.name` on first run, which in turn lets the 13F ingester
     fuzzy-match issuer names back to tickers even before yfinance has
     populated fundamentals.

Regions:
  - US-L : US large cap (S&P 500 / NDX 100 core)
  - US-S : US small/mid cap (Russell 2000-adjacent)
  - IL   : Israel (US-listed ADRs/common)
  - EU   : Europe (US-listed ADRs or yfinance exchange suffixes)

`refresh_universe()` pulls the current S&P 500 and NASDAQ-100 membership from
Wikipedia when online and unions it with the static list so we always cover
the curated international names even if the Wikipedia fetch partially fails.
"""
from __future__ import annotations

import logging
from collections.abc import Iterable

import pandas as pd

from .config import get_settings

logger = logging.getLogger(__name__)


# -------------------------- static data --------------------------

# (ticker, name, sector, region)
_CORE: tuple[tuple[str, str, str, str], ...] = (
    # --- US large cap ---------------------------------------------------------
    ("AAPL", "Apple Inc.", "Technology", "US-L"),
    ("MSFT", "Microsoft Corporation", "Technology", "US-L"),
    ("GOOGL", "Alphabet Inc.", "Communication Services", "US-L"),
    ("GOOG", "Alphabet Inc.", "Communication Services", "US-L"),
    ("AMZN", "Amazon.com Inc.", "Consumer Discretionary", "US-L"),
    ("META", "Meta Platforms Inc.", "Communication Services", "US-L"),
    ("NVDA", "NVIDIA Corporation", "Technology", "US-L"),
    ("TSLA", "Tesla Inc.", "Consumer Discretionary", "US-L"),
    ("BRK-B", "Berkshire Hathaway Inc.", "Financials", "US-L"),
    ("JPM", "JPMorgan Chase & Co.", "Financials", "US-L"),
    ("V", "Visa Inc.", "Financials", "US-L"),
    ("UNH", "UnitedHealth Group", "Health Care", "US-L"),
    ("XOM", "Exxon Mobil Corporation", "Energy", "US-L"),
    ("LLY", "Eli Lilly and Company", "Health Care", "US-L"),
    ("MA", "Mastercard Incorporated", "Financials", "US-L"),
    ("JNJ", "Johnson & Johnson", "Health Care", "US-L"),
    ("PG", "Procter & Gamble", "Consumer Staples", "US-L"),
    ("HD", "Home Depot", "Consumer Discretionary", "US-L"),
    ("ORCL", "Oracle Corporation", "Technology", "US-L"),
    ("AVGO", "Broadcom Inc.", "Technology", "US-L"),
    ("COST", "Costco Wholesale", "Consumer Staples", "US-L"),
    ("MRK", "Merck & Co.", "Health Care", "US-L"),
    ("ABBV", "AbbVie Inc.", "Health Care", "US-L"),
    ("CVX", "Chevron Corporation", "Energy", "US-L"),
    ("WMT", "Walmart Inc.", "Consumer Staples", "US-L"),
    ("BAC", "Bank of America", "Financials", "US-L"),
    ("KO", "Coca-Cola Company", "Consumer Staples", "US-L"),
    ("PEP", "PepsiCo Inc.", "Consumer Staples", "US-L"),
    ("ADBE", "Adobe Inc.", "Technology", "US-L"),
    ("CRM", "Salesforce Inc.", "Technology", "US-L"),
    ("MCD", "McDonald's Corporation", "Consumer Discretionary", "US-L"),
    ("TMO", "Thermo Fisher Scientific", "Health Care", "US-L"),
    ("ACN", "Accenture plc", "Technology", "US-L"),
    ("ABT", "Abbott Laboratories", "Health Care", "US-L"),
    ("LIN", "Linde plc", "Materials", "US-L"),
    ("CSCO", "Cisco Systems", "Technology", "US-L"),
    ("NFLX", "Netflix Inc.", "Communication Services", "US-L"),
    ("WFC", "Wells Fargo & Company", "Financials", "US-L"),
    ("AMD", "Advanced Micro Devices", "Technology", "US-L"),
    ("DHR", "Danaher Corporation", "Health Care", "US-L"),
    ("TXN", "Texas Instruments", "Technology", "US-L"),
    ("DIS", "Walt Disney Company", "Communication Services", "US-L"),
    ("PM", "Philip Morris International", "Consumer Staples", "US-L"),
    ("VZ", "Verizon Communications", "Communication Services", "US-L"),
    ("CAT", "Caterpillar Inc.", "Industrials", "US-L"),
    ("INTU", "Intuit Inc.", "Technology", "US-L"),
    ("IBM", "International Business Machines", "Technology", "US-L"),
    ("GE", "General Electric", "Industrials", "US-L"),
    ("NEE", "NextEra Energy", "Utilities", "US-L"),
    ("UNP", "Union Pacific", "Industrials", "US-L"),
    ("AMGN", "Amgen Inc.", "Health Care", "US-L"),
    ("COP", "ConocoPhillips", "Energy", "US-L"),
    ("LOW", "Lowe's Companies", "Consumer Discretionary", "US-L"),
    ("SPGI", "S&P Global Inc.", "Financials", "US-L"),
    ("QCOM", "Qualcomm Incorporated", "Technology", "US-L"),
    ("HON", "Honeywell International", "Industrials", "US-L"),
    ("NOW", "ServiceNow Inc.", "Technology", "US-L"),
    ("BKNG", "Booking Holdings", "Consumer Discretionary", "US-L"),
    ("RTX", "RTX Corporation", "Industrials", "US-L"),
    ("AMAT", "Applied Materials", "Technology", "US-L"),
    ("GS", "Goldman Sachs Group", "Financials", "US-L"),
    ("SBUX", "Starbucks Corporation", "Consumer Discretionary", "US-L"),
    ("T", "AT&T Inc.", "Communication Services", "US-L"),
    ("UPS", "United Parcel Service", "Industrials", "US-L"),
    ("INTC", "Intel Corporation", "Technology", "US-L"),
    ("PFE", "Pfizer Inc.", "Health Care", "US-L"),
    ("MS", "Morgan Stanley", "Financials", "US-L"),
    ("BLK", "BlackRock Inc.", "Financials", "US-L"),
    ("ISRG", "Intuitive Surgical", "Health Care", "US-L"),
    ("LMT", "Lockheed Martin", "Industrials", "US-L"),
    ("AXP", "American Express", "Financials", "US-L"),
    ("DE", "Deere & Company", "Industrials", "US-L"),
    ("PLD", "Prologis Inc.", "Real Estate", "US-L"),
    ("ELV", "Elevance Health", "Health Care", "US-L"),
    ("TJX", "TJX Companies", "Consumer Discretionary", "US-L"),
    ("GILD", "Gilead Sciences", "Health Care", "US-L"),
    ("MDLZ", "Mondelez International", "Consumer Staples", "US-L"),
    ("SYK", "Stryker Corporation", "Health Care", "US-L"),
    ("ADI", "Analog Devices", "Technology", "US-L"),
    ("C", "Citigroup Inc.", "Financials", "US-L"),
    ("VRTX", "Vertex Pharmaceuticals", "Health Care", "US-L"),
    ("MDT", "Medtronic plc", "Health Care", "US-L"),
    ("ADP", "Automatic Data Processing", "Industrials", "US-L"),
    ("MMC", "Marsh & McLennan", "Financials", "US-L"),
    ("CB", "Chubb Limited", "Financials", "US-L"),
    ("PGR", "Progressive Corporation", "Financials", "US-L"),
    ("REGN", "Regeneron Pharmaceuticals", "Health Care", "US-L"),
    ("CI", "Cigna Group", "Health Care", "US-L"),
    ("LRCX", "Lam Research", "Technology", "US-L"),
    ("SCHW", "Charles Schwab", "Financials", "US-L"),
    ("TMUS", "T-Mobile US", "Communication Services", "US-L"),
    ("BSX", "Boston Scientific", "Health Care", "US-L"),
    ("ZTS", "Zoetis Inc.", "Health Care", "US-L"),
    ("SO", "Southern Company", "Utilities", "US-L"),
    ("DUK", "Duke Energy", "Utilities", "US-L"),
    ("PANW", "Palo Alto Networks", "Technology", "US-L"),
    ("EOG", "EOG Resources", "Energy", "US-L"),
    ("SLB", "Schlumberger Limited", "Energy", "US-L"),
    ("MU", "Micron Technology", "Technology", "US-L"),
    ("KLAC", "KLA Corporation", "Technology", "US-L"),
    ("EQIX", "Equinix Inc.", "Real Estate", "US-L"),
    ("ETN", "Eaton Corporation", "Industrials", "US-L"),
    ("APH", "Amphenol Corporation", "Technology", "US-L"),
    ("ITW", "Illinois Tool Works", "Industrials", "US-L"),
    ("CME", "CME Group", "Financials", "US-L"),
    ("AON", "Aon plc", "Financials", "US-L"),
    ("WM", "Waste Management", "Industrials", "US-L"),
    ("ICE", "Intercontinental Exchange", "Financials", "US-L"),
    ("CSX", "CSX Corporation", "Industrials", "US-L"),
    ("SNPS", "Synopsys Inc.", "Technology", "US-L"),
    ("CDNS", "Cadence Design Systems", "Technology", "US-L"),
    ("MO", "Altria Group", "Consumer Staples", "US-L"),
    ("PYPL", "PayPal Holdings", "Financials", "US-L"),
    ("ABNB", "Airbnb Inc.", "Consumer Discretionary", "US-L"),
    ("SHOP", "Shopify Inc.", "Technology", "US-L"),
    ("UBER", "Uber Technologies", "Industrials", "US-L"),
    ("PLTR", "Palantir Technologies", "Technology", "US-L"),
    ("COIN", "Coinbase Global", "Financials", "US-L"),
    ("F", "Ford Motor Company", "Consumer Discretionary", "US-L"),
    ("GM", "General Motors", "Consumer Discretionary", "US-L"),
    ("DAL", "Delta Air Lines", "Industrials", "US-L"),
    ("UAL", "United Airlines Holdings", "Industrials", "US-L"),
    ("NKE", "NIKE Inc.", "Consumer Discretionary", "US-L"),
    ("LULU", "Lululemon Athletica", "Consumer Discretionary", "US-L"),
    ("MAR", "Marriott International", "Consumer Discretionary", "US-L"),
    # --- US small / mid cap ---------------------------------------------------
    ("SMCI", "Super Micro Computer", "Technology", "US-S"),
    ("AFRM", "Affirm Holdings", "Financials", "US-S"),
    ("SOFI", "SoFi Technologies", "Financials", "US-S"),
    ("HOOD", "Robinhood Markets", "Financials", "US-S"),
    ("RBLX", "Roblox Corporation", "Communication Services", "US-S"),
    ("DKNG", "DraftKings Inc.", "Consumer Discretionary", "US-S"),
    ("PINS", "Pinterest Inc.", "Communication Services", "US-S"),
    ("SNAP", "Snap Inc.", "Communication Services", "US-S"),
    ("LYFT", "Lyft Inc.", "Industrials", "US-S"),
    ("BILL", "BILL Holdings", "Technology", "US-S"),
    ("U", "Unity Software", "Technology", "US-S"),
    ("RIVN", "Rivian Automotive", "Consumer Discretionary", "US-S"),
    ("LCID", "Lucid Group", "Consumer Discretionary", "US-S"),
    ("NIO", "NIO Inc.", "Consumer Discretionary", "US-S"),
    ("XPEV", "XPeng Inc.", "Consumer Discretionary", "US-S"),
    ("CHWY", "Chewy Inc.", "Consumer Discretionary", "US-S"),
    ("W", "Wayfair Inc.", "Consumer Discretionary", "US-S"),
    ("ETSY", "Etsy Inc.", "Consumer Discretionary", "US-S"),
    ("RH", "RH", "Consumer Discretionary", "US-S"),
    ("TDOC", "Teladoc Health", "Health Care", "US-S"),
    ("DOCN", "DigitalOcean Holdings", "Technology", "US-S"),
    ("NET", "Cloudflare Inc.", "Technology", "US-S"),
    ("DDOG", "Datadog Inc.", "Technology", "US-S"),
    ("MDB", "MongoDB Inc.", "Technology", "US-S"),
    ("OKTA", "Okta Inc.", "Technology", "US-S"),
    ("ZS", "Zscaler Inc.", "Technology", "US-S"),
    ("CRWD", "CrowdStrike Holdings", "Technology", "US-S"),
    ("S", "SentinelOne Inc.", "Technology", "US-S"),
    ("TTD", "Trade Desk Inc.", "Technology", "US-S"),
    ("APP", "AppLovin Corporation", "Technology", "US-S"),
    ("ROKU", "Roku Inc.", "Communication Services", "US-S"),
    ("DASH", "DoorDash Inc.", "Consumer Discretionary", "US-S"),
    ("PATH", "UiPath Inc.", "Technology", "US-S"),
    ("TWLO", "Twilio Inc.", "Technology", "US-S"),
    ("ZM", "Zoom Video Communications", "Technology", "US-S"),
    ("DOCU", "DocuSign Inc.", "Technology", "US-S"),
    ("SQ", "Block Inc.", "Financials", "US-S"),
    ("UPST", "Upstart Holdings", "Financials", "US-S"),
    ("OPEN", "Opendoor Technologies", "Real Estate", "US-S"),
    ("SGFY", "Signify Health", "Health Care", "US-S"),
    ("HIMS", "Hims & Hers Health", "Health Care", "US-S"),
    # --- Israel (mostly US-listed) -------------------------------------------
    ("TEVA", "Teva Pharmaceutical Industries", "Health Care", "IL"),
    ("CHKP", "Check Point Software Technologies", "Technology", "IL"),
    ("NICE", "NICE Ltd.", "Technology", "IL"),
    ("WIX", "Wix.com Ltd.", "Technology", "IL"),
    ("MNDY", "Monday.com Ltd.", "Technology", "IL"),
    ("CYBR", "CyberArk Software", "Technology", "IL"),
    ("ESLT", "Elbit Systems", "Industrials", "IL"),
    ("SEDG", "SolarEdge Technologies", "Technology", "IL"),
    ("ICL", "ICL Group", "Materials", "IL"),
    ("FVRR", "Fiverr International", "Communication Services", "IL"),
    ("FROG", "JFrog Ltd.", "Technology", "IL"),
    ("GLBE", "Global-E Online", "Technology", "IL"),
    ("RDWR", "Radware Ltd.", "Technology", "IL"),
    ("LMND", "Lemonade Inc.", "Financials", "IL"),
    ("MBLY", "Mobileye Global", "Technology", "IL"),
    ("INMD", "InMode Ltd.", "Health Care", "IL"),
    ("NVMI", "Nova Ltd.", "Technology", "IL"),
    ("CAMT", "Camtek Ltd.", "Technology", "IL"),
    ("AUDC", "AudioCodes Ltd.", "Technology", "IL"),
    ("GILT", "Gilat Satellite Networks", "Technology", "IL"),
    # --- Europe (US ADRs where available; LSE/EU suffixes otherwise) ---------
    ("ASML", "ASML Holding", "Technology", "EU"),
    ("NVO", "Novo Nordisk", "Health Care", "EU"),
    ("SAP", "SAP SE", "Technology", "EU"),
    ("BP", "BP plc", "Energy", "EU"),
    ("SHEL", "Shell plc", "Energy", "EU"),
    ("AZN", "AstraZeneca plc", "Health Care", "EU"),
    ("UL", "Unilever plc", "Consumer Staples", "EU"),
    ("RIO", "Rio Tinto", "Materials", "EU"),
    ("DEO", "Diageo plc", "Consumer Staples", "EU"),
    ("GSK", "GSK plc", "Health Care", "EU"),
    ("NVS", "Novartis AG", "Health Care", "EU"),
    ("SNY", "Sanofi", "Health Care", "EU"),
    ("SAN", "Banco Santander", "Financials", "EU"),
    ("ING", "ING Groep", "Financials", "EU"),
    ("HSBC", "HSBC Holdings", "Financials", "EU"),
    ("VOD", "Vodafone Group", "Communication Services", "EU"),
    ("STM", "STMicroelectronics", "Technology", "EU"),
    ("PHG", "Koninklijke Philips", "Health Care", "EU"),
    ("CRH", "CRH plc", "Materials", "EU"),
    ("MTD", "Mettler-Toledo International", "Health Care", "EU"),
    ("RYAAY", "Ryanair Holdings", "Industrials", "EU"),
    ("BCS", "Barclays plc", "Financials", "EU"),
    ("BUD", "Anheuser-Busch InBev", "Consumer Staples", "EU"),
    ("LYG", "Lloyds Banking Group", "Financials", "EU"),
    ("ERIC", "Telefonaktiebolaget LM Ericsson", "Technology", "EU"),
    ("NOK", "Nokia Corporation", "Technology", "EU"),
    ("E", "Eni S.p.A.", "Energy", "EU"),
    ("TTE", "TotalEnergies SE", "Energy", "EU"),
    ("EQNR", "Equinor ASA", "Energy", "EU"),
    ("SW", "Smurfit WestRock", "Materials", "EU"),
)


def static_universe_entries() -> list[tuple[str, str, str, str]]:
    return list(_CORE)


def static_universe() -> list[str]:
    return [t for t, *_ in _CORE]


def static_name_map() -> dict[str, str]:
    """Return {ticker: name} from the static list."""
    return {t: n for t, n, *_ in _CORE}


def static_sector_map() -> dict[str, str]:
    return {t: sector for t, _, sector, _ in _CORE}


def _fetch_sp500() -> list[str]:
    tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = tables[0]
    return [t.replace(".", "-") for t in df["Symbol"].astype(str).tolist()]


def _fetch_ndx() -> list[str]:
    tables = pd.read_html("https://en.wikipedia.org/wiki/Nasdaq-100")
    for t in tables:
        if "Ticker" in t.columns or "Symbol" in t.columns:
            col = "Ticker" if "Ticker" in t.columns else "Symbol"
            return [s.replace(".", "-") for s in t[col].astype(str).tolist()]
    return []


def refresh_universe() -> list[str]:
    """Return current S&P500 ∪ NDX100 ∪ static (with intl + small cap)."""
    tickers = set(static_universe())
    try:
        tickers |= set(_fetch_sp500())
        tickers |= set(_fetch_ndx())
        logger.info("universe refreshed: %d tickers", len(tickers))
    except Exception as e:  # noqa: BLE001
        logger.warning("wikipedia fetch failed (%s); using static-only", e)
    return sorted(tickers)


def current_universe() -> list[str]:
    settings = get_settings()
    tickers = refresh_universe()
    if settings.universe_max and settings.universe_max > 0:
        tickers = tickers[: settings.universe_max]
    return tickers


def chunks(xs: Iterable[str], n: int) -> Iterable[list[str]]:
    buf: list[str] = []
    for x in xs:
        buf.append(x)
        if len(buf) >= n:
            yield buf
            buf = []
    if buf:
        yield buf


def seed_stocks_table() -> int:
    """Upsert (ticker, name, sector) rows from the static universe into `stocks`.

    Done once at startup so EDGAR's 13F ingester can fuzzy-match issuer names
    back to tickers before yfinance has run fundamentals. Returns row count.
    """
    from datetime import datetime

    from .db import session_scope
    from .models import Stock

    entries = static_universe_entries()
    written = 0
    now = datetime.utcnow()
    with session_scope() as s:
        for ticker, name, sector, _region in entries:
            existing = s.get(Stock, ticker)
            if existing is None:
                s.add(
                    Stock(
                        ticker=ticker,
                        name=name,
                        sector=sector,
                        in_universe=True,
                        updated_at=now,
                    )
                )
            else:
                # Only fill in missing values; don't clobber yfinance-sourced data.
                if not existing.name:
                    existing.name = name
                if not existing.sector:
                    existing.sector = sector
                existing.in_universe = True
            written += 1
    return written
