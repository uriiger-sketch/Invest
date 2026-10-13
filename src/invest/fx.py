"""Quote currency of each listing and its conversion to US dollars.

Yahoo quotes Tel Aviv listings in agorot (currency code ILA, 1/100 of a
shekel) and Euronext Amsterdam listings in euros; every other symbol in the
universe trades in dollars. Prices and price targets share the listing's
unit, so upside and momentum are unit-free, but the liquidity gate compares
a 20-day DOLLAR volume against a dollar floor: an agorot-denominated volume
overstates a Tel Aviv name's liquidity by ~300x.

Rates are Yahoo's `<CCY>=X` closes (units of currency per 1 USD), fetched
once per crawl and stored as `IntelSnapshot(ticker="ILS=X", kind="fx")`.
A missing or implausible rate falls back to a constant: a liquidity gate
that is off by a few percent is harmless, one that is off by 100x is not.
"""
from __future__ import annotations

import json
import logging
from datetime import UTC, datetime

logger = logging.getLogger(__name__)

# suffix -> (currency, quote units per currency unit)
_LISTINGS: dict[str, tuple[str, float]] = {
    ".TA": ("ILS", 100.0),  # agorot
    ".AS": ("EUR", 1.0),
}
PAIRS: dict[str, str] = {"ILS": "ILS=X", "EUR": "EUR=X"}
# Fallback units per USD and the band a fetched rate must fall inside.
FALLBACK_PER_USD: dict[str, float] = {"ILS": 3.1, "EUR": 0.9}  # Oct 2026 closes
_PLAUSIBLE: dict[str, tuple[float, float]] = {"ILS": (2.5, 6.0), "EUR": (0.6, 1.4)}
FX_KIND = "fx"


def listing_currency(ticker: str) -> tuple[str, float]:
    """(ISO currency, quote units per currency unit) of a symbol's quotes."""
    for suffix, cur in _LISTINGS.items():
        if ticker.upper().endswith(suffix):
            return cur
    return ("USD", 1.0)


def plausible(currency: str, per_usd: float | None) -> bool:
    lo, hi = _PLAUSIBLE.get(currency, (0.0, float("inf")))
    return per_usd is not None and lo <= per_usd <= hi


def usd_per_quote_unit(ticker: str, per_usd: dict[str, float] | None = None) -> float:
    """Multiply a quoted price (or price x volume) by this to get dollars."""
    cur, sub = listing_currency(ticker)
    if cur == "USD":
        return 1.0
    rates = per_usd if per_usd is not None else load_rates()
    rate = rates.get(cur)
    if not plausible(cur, rate):
        rate = FALLBACK_PER_USD[cur]
    return 1.0 / (rate * sub)


def to_local_price(ticker: str, quoted: float | None) -> float | None:
    """Quoted price in the listing's main unit (agorot -> shekels)."""
    if quoted is None:
        return None
    return quoted / listing_currency(ticker)[1]


def load_rates() -> dict[str, float]:
    """Stored per-USD rates, with the fallback for anything missing/implausible."""
    from sqlalchemy import select

    from .db import session_scope
    from .models import IntelSnapshot

    out = dict(FALLBACK_PER_USD)
    try:
        with session_scope() as s:
            rows = s.execute(
                select(IntelSnapshot.ticker, IntelSnapshot.payload).where(
                    IntelSnapshot.kind == FX_KIND
                )
            ).all()
    except Exception:  # noqa: BLE001 — a missing table must not break features
        logger.exception("loading FX rates failed; using fallbacks")
        return out
    by_pair = {pair: cur for cur, pair in PAIRS.items()}
    for pair, payload in rows:
        cur = by_pair.get(pair)
        try:
            rate = float(json.loads(payload).get("per_usd"))
        except (TypeError, ValueError, AttributeError):
            continue
        if cur and plausible(cur, rate):
            out[cur] = rate
    return out


def refresh_rates(download=None) -> dict[str, float]:
    """Fetch the latest close of every pair and store the plausible ones.

    `download(symbols, period)` returns a yfinance frame; defaults to
    YFinanceSource's throttled, retried downloader.
    """
    from .sources.yfinance_src import YFinanceSource, _prices_frame_to_rows, upsert_intel

    pairs = list(PAIRS.values())
    if download is None:
        download = YFinanceSource()._download_prices
    rows = _prices_frame_to_rows(download(pairs, "5d"), pairs)
    latest: dict[str, tuple] = {}
    for r in rows:
        if r["ticker"] not in latest or r["date"] > latest[r["ticker"]][0]:
            latest[r["ticker"]] = (r["date"], r["close"])
    stored: dict[str, float] = {}
    for cur, pair in PAIRS.items():
        if pair not in latest:
            continue
        d, rate = latest[pair]
        if not plausible(cur, rate):
            logger.warning("FX %s=%s outside the plausible band; ignored", pair, rate)
            continue
        upsert_intel(pair, FX_KIND, {"per_usd": rate, "date": d.isoformat(),
                                     "fetched": datetime.now(UTC).isoformat(timespec="seconds")})
        stored[cur] = rate
    return stored
