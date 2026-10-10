"""Yahoo Finance source: prices, analyst coverage, estimates, fundamentals, news.

Design (rewritten after crawls were found failing or coming back thin):

* ONE quoteSummary request per ticker fetches every module we use —
  recommendation trend, price targets, per-firm rating/target history, EPS
  trend + revisions, earnings surprises, the earnings calendar, key
  statistics, valuation and profile. The old code made a separate request
  per property (3 on the fast path, 7+ on the deep path) and so hit Yahoo's
  rate limits sooner while learning less.
* Tickers are crawled by a small thread pool; results are written to SQLite
  from the main thread only. A shared `RateGovernor` pauses every worker
  when Yahoo starts answering 429, and aborts the stage cleanly if the block
  persists, instead of each worker exhausting its own retries.
* "No such symbol" (HTTP 404, delisted) is NOT retried: the old wrapper
  turned every exception into a retryable error, so each dead or uncovered
  ticker cost ~7 s of back-off on every run.
* Parsing is done by pure functions (`parse_quote_summary`,
  `actions_from_history`, …) so it is unit-tested without the network.
"""
from __future__ import annotations

import json
import logging
import time
from concurrent.futures import FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from datetime import UTC, date, datetime, timedelta
from typing import Any

import pandas as pd
import yfinance as yf
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..db import session_scope
from ..firms import canonical_firm_key
from ..models import Consensus, IntelSnapshot, Price, Stock
from ..universe import chunks
from .base import (
    BaseSource,
    CrawlAborted,
    RateGovernor,
    RateLimitedError,
    TransientSourceError,
    log_run,
    upsert_analyst_actions,
    with_retries,
)
from .news_src import parse_yahoo_news, upsert_news

logger = logging.getLogger(__name__)

_BATCH_SIZE = 40
_QS_URL = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/{symbol}"
QS_MODULES: tuple[str, ...] = (
    "recommendationTrend",
    "financialData",
    "upgradeDowngradeHistory",
    "earningsTrend",
    "earningsHistory",
    "calendarEvents",
    "defaultKeyStatistics",
    "summaryDetail",
    "price",
    "summaryProfile",
)


class NoDataError(Exception):
    """Yahoo has no data for this symbol (404 / delisted / not covered)."""


def _utcnow() -> datetime:
    return datetime.now(UTC).replace(tzinfo=None)


class YFinanceSource(BaseSource):
    name = "yfinance"
    rate_per_minute = 300.0  # shared by all worker threads

    def __init__(self) -> None:
        super().__init__()
        self.governor = RateGovernor()

    # --------------------------- prices ---------------------------

    @with_retries
    def _download_prices(self, tickers: list[str], period: str = "3mo") -> pd.DataFrame:
        self.throttle(len(tickers) / 4)
        try:
            df = yf.download(
                tickers=" ".join(tickers),
                period=period,
                interval="1d",
                group_by="ticker",
                auto_adjust=False,
                progress=False,
                threads=True,
            )
        except Exception as e:  # noqa: BLE001
            raise TransientSourceError(str(e)) from e
        if df is None or df.empty:
            raise TransientSourceError("yfinance returned empty frame")
        return df

    def ingest_prices(self, tickers: list[str], period: str | None = None) -> int:
        from ..config import get_settings

        period = period or get_settings().fast_price_period
        rows_written = 0
        for batch in chunks(tickers, _BATCH_SIZE):
            try:
                df = self._download_prices(batch, period)
            except TransientSourceError as e:
                logger.warning("price batch failed: %s", e)
                continue
            rows = _prices_frame_to_rows(df, batch)
            if not rows:
                continue
            with session_scope() as s:
                stmt = sqlite_insert(Price).values(rows)
                stmt = stmt.on_conflict_do_update(
                    index_elements=["ticker", "date"],
                    set_={
                        "open": stmt.excluded.open,
                        "high": stmt.excluded.high,
                        "low": stmt.excluded.low,
                        "close": stmt.excluded.close,
                        "adj_close": stmt.excluded.adj_close,
                        "volume": stmt.excluded.volume,
                    },
                )
                s.execute(stmt)
            rows_written += len(rows)
        return rows_written

    # ----------------------- quote summary -----------------------

    @with_retries
    def _quote_summary(self, ticker: str) -> dict[str, Any]:
        """All `QS_MODULES` for one symbol in a single request.

        Raises NoDataError for unknown/delisted symbols (not retried) and
        TransientSourceError / RateLimitedError for retryable failures.
        """
        self.throttle()
        try:
            from yfinance.data import YfData
            from yfinance.exceptions import YFRateLimitError
        except Exception:  # noqa: BLE001 — internal API moved: use the property API
            return self._quote_summary_fallback(ticker)
        params = {
            "modules": ",".join(QS_MODULES),
            "corsDomain": "finance.yahoo.com",
            "formatted": "false",
            "symbol": ticker,
        }
        try:
            js = YfData().get_raw_json(_QS_URL.format(symbol=ticker), params=params, timeout=20)
        except YFRateLimitError as e:
            raise RateLimitedError(str(e)) from e
        except Exception as e:  # noqa: BLE001
            status = getattr(getattr(e, "response", None), "status_code", None)
            if status == 404:
                raise NoDataError(ticker) from e
            if status == 429:
                raise RateLimitedError(str(e)) from e
            raise TransientSourceError(f"{type(e).__name__}: {e}") from e
        try:
            result = (js.get("quoteSummary") or {}).get("result") or []
        except AttributeError as e:
            raise TransientSourceError("malformed quoteSummary payload") from e
        if not result or not isinstance(result[0], dict):
            raise NoDataError(ticker)
        return result[0]

    def _quote_summary_fallback(self, ticker: str) -> dict[str, Any]:
        """Rebuild the core modules from yfinance's public properties.

        Only used if `yfinance.data.YfData` ever disappears; covers consensus,
        targets and rating history (the inputs the ranking cannot do without).
        """
        tk = yf.Ticker(ticker)
        out: dict[str, Any] = {}
        try:
            recs = tk.recommendations
            if recs is not None and not recs.empty:
                out["recommendationTrend"] = {"trend": recs.to_dict("records")}
        except Exception:  # noqa: BLE001
            pass
        try:
            tgt = tk.analyst_price_targets or {}
            out["financialData"] = {
                "currentPrice": tgt.get("current"),
                "targetMeanPrice": tgt.get("mean"),
                "targetMedianPrice": tgt.get("median"),
                "targetHighPrice": tgt.get("high"),
                "targetLowPrice": tgt.get("low"),
            }
        except Exception:  # noqa: BLE001
            pass
        try:
            ud = tk.upgrades_downgrades
            if ud is not None and not ud.empty:
                hist = ud.reset_index()
                hist["epochGradeDate"] = pd.to_datetime(hist["GradeDate"]).astype("int64") // 10**9
                hist = hist.rename(columns={"Firm": "firm", "ToGrade": "toGrade",
                                            "FromGrade": "fromGrade", "Action": "action"})
                out["upgradeDowngradeHistory"] = {"history": hist.to_dict("records")}
        except Exception:  # noqa: BLE001
            pass
        if not out:
            raise NoDataError(ticker)
        return out

    def _news(self, ticker: str) -> list[dict]:
        self.throttle()
        try:
            return yf.Ticker(ticker).get_news(count=20, tab="news") or []
        except Exception as e:  # noqa: BLE001 — news is best-effort
            logger.debug("news %s failed: %s", ticker, e)
            return []

    # ------------------------- worker -------------------------

    def _fetch_bundle(self, ticker: str, want_news: bool) -> dict[str, Any]:
        """Network-only work for one ticker (runs in a worker thread)."""
        out: dict[str, Any] = {"ticker": ticker}
        try:
            self.governor.before_request()
            out["qs"] = self._quote_summary(ticker)
            self.governor.on_success()
        except CrawlAborted:
            out["error"] = "aborted"
            return out
        except NoDataError:
            out["error"] = "no_data"
            self.governor.on_success()
        except RateLimitedError:
            self.governor.on_rate_limit()
            out["error"] = "rate_limited"
            return out
        except TransientSourceError as e:
            out["error"] = f"transient: {e}"[:200]
            return out
        if want_news:
            out["news"] = self._news(ticker)
        return out

    # ------------------------ combined coverage -------------------------

    def ingest_coverage(
        self,
        tickers: list[str],
        budget_seconds: float = 0.0,
        lookback_days: int = 90,
        want_news: bool = True,
    ) -> tuple[int, int]:
        """Crawl full analyst + estimate + fundamental intel (+ news) per ticker.

        ``budget_seconds`` (0 = unlimited) caps wall-clock time; callers pass
        the stalest tickers first so a truncated sweep still cycles the
        universe across runs. Returns ``(rows_written, tickers_processed)``.
        """
        from ..config import get_settings

        settings = get_settings()
        today = date.today()
        cutoff = today - timedelta(days=lookback_days)
        names = _stock_names(tickers)
        last_close = _last_closes(tickers)
        started = time.monotonic()
        workers = max(1, int(settings.crawl_workers))
        written = processed = 0
        stats: dict[str, int] = {}
        action_rows: list[dict] = []
        pending = list(tickers)
        in_flight: dict[Future, str] = {}

        def over_budget() -> bool:
            return bool(budget_seconds) and (time.monotonic() - started) > budget_seconds

        with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="yf") as ex:
            while pending or in_flight:
                while pending and len(in_flight) < workers * 2 and not over_budget() \
                        and not self.governor.aborted:
                    t = pending.pop(0)
                    in_flight[ex.submit(self._fetch_bundle, t, want_news)] = t
                if not in_flight:
                    break
                done, _ = wait(list(in_flight), return_when=FIRST_COMPLETED)
                for fut in done:
                    t = in_flight.pop(fut)
                    try:
                        bundle = fut.result()
                    except Exception as e:  # noqa: BLE001 — never let one ticker kill the sweep
                        logger.warning("coverage %s crashed: %s", t, e)
                        stats["crashed"] = stats.get("crashed", 0) + 1
                        continue
                    err = bundle.get("error")
                    key = err.split(":")[0] if err else "ok"
                    stats[key] = stats.get(key, 0) + 1
                    if err in ("aborted", "rate_limited") or (err or "").startswith("transient"):
                        continue
                    try:
                        w, acts = self._store_bundle(
                            bundle, today, cutoff, names.get(t), last_close.get(t)
                        )
                    except Exception:  # noqa: BLE001
                        logger.exception("coverage %s: storing failed", t)
                        stats["store_failed"] = stats.get("store_failed", 0) + 1
                        continue
                    written += w
                    action_rows.extend(acts)
                    processed += 1
        if pending:
            logger.info(
                "coverage sweep stopped with %d/%d tickers left (%s); they are stalest next run",
                len(pending), len(tickers),
                "rate-limit abort" if self.governor.aborted else "time budget",
            )
        if action_rows:
            written += upsert_analyst_actions(action_rows)
        logger.info(
            "coverage sweep: processed=%d/%d outcomes=%s rate_limited_total=%d elapsed=%.0fs",
            processed, len(tickers), stats, self.governor.rate_limited,
            time.monotonic() - started,
        )
        self.last_stats = stats
        return written, processed

    def _store_bundle(
        self,
        bundle: dict[str, Any],
        today: date,
        cutoff: date,
        company_name: str | None,
        last_close: float | None,
    ) -> tuple[int, list[dict]]:
        t = bundle["ticker"]
        written = 0
        news_rows = parse_yahoo_news(t, bundle.get("news"), company_name)
        if news_rows:
            written += upsert_news(news_rows)
        qs = bundle.get("qs")
        if not qs:
            return written, []
        parsed = parse_quote_summary(t, qs, today, cutoff)
        if parsed["consensus"] is not None:
            with session_scope() as s:
                s.execute(_consensus_upsert(parsed["consensus"]))
            written += 1
        if parsed["intel"]:
            parsed["intel"]["our_close"] = last_close
            upsert_intel(t, "quote", parsed["intel"])
            written += 1
        if parsed["stock"]:
            _update_stock(t, parsed["stock"])
        return written, parsed["actions"]

    # --------------------------- run -----------------------------

    def run(self, tickers: list[str]) -> int:  # noqa: D401
        """Deep path: a full year of prices + the full intel sweep (no budget)."""
        from ..config import get_settings

        settings = get_settings()
        total = 0
        with log_run("yfinance.prices") as c:
            c["rows"] = self.ingest_prices(tickers, period=settings.deep_price_period)
            total += c["rows"]
        from ..pipeline.ingest import active_tickers

        live = active_tickers(tickers)
        with log_run("yfinance.coverage_deep") as c:
            rows, _ = self.ingest_coverage(live, budget_seconds=settings.coverage_budget_seconds * 2)
            c["rows"] = rows
            total += rows
        return total


# ----------------------------- storage helpers -----------------------------


def upsert_intel(ticker: str, kind: str, payload: dict[str, Any]) -> None:
    body = json.dumps(payload, separators=(",", ":"), default=str)
    with session_scope() as s:
        stmt = sqlite_insert(IntelSnapshot).values(
            ticker=ticker, kind=kind, as_of=_utcnow(), payload=body
        )
        stmt = stmt.on_conflict_do_update(
            index_elements=["ticker", "kind"],
            set_={"as_of": stmt.excluded.as_of, "payload": stmt.excluded.payload},
        )
        s.execute(stmt)


def _stock_names(tickers: list[str]) -> dict[str, str]:
    with session_scope() as s:
        return {
            t: n for t, n in s.query(Stock.ticker, Stock.name).filter(Stock.ticker.in_(tickers)) if n
        }


def _last_closes(tickers: list[str]) -> dict[str, float]:
    from sqlalchemy import func, select

    with session_scope() as s:
        sub = (
            select(Price.ticker, func.max(Price.date).label("d"))
            .where(Price.ticker.in_(tickers), Price.close.isnot(None))
            .group_by(Price.ticker)
            .subquery()
        )
        rows = s.execute(
            select(Price.ticker, Price.close).join(
                sub, (Price.ticker == sub.c.ticker) & (Price.date == sub.c.d)
            )
        ).all()
    return {t: float(c) for t, c in rows if c}


def _update_stock(ticker: str, info: dict[str, Any]) -> None:
    with session_scope() as s:
        st = s.get(Stock, ticker)
        if st is None:
            st = Stock(ticker=ticker, in_universe=True)
            s.add(st)
        for field in ("name", "sector", "industry"):
            if info.get(field):
                setattr(st, field, str(info[field])[:255 if field == "name" else 128])
        for field in ("market_cap", "beta"):
            if info.get(field) is not None:
                setattr(st, field, info[field])
        st.updated_at = _utcnow()


# ----------------------------- parsing -----------------------------


def _raw(v: Any) -> Any:
    """quoteSummary values arrive either bare or as {"raw": x, "fmt": "..."}."""
    if isinstance(v, dict):
        return v.get("raw")
    return v


def _coerce_float(x: Any) -> float | None:
    try:
        x = _raw(x)
        if x is None or isinstance(x, bool):
            return None
        f = float(x)
        if f != f or f in (float("inf"), float("-inf")):  # NaN / inf
            return None
        return f
    except (TypeError, ValueError):
        return None


def _pos(x: Any) -> float | None:
    f = _coerce_float(x)
    return f if f is not None and f > 0 else None


def _epoch_to_date(x: Any) -> date | None:
    f = _coerce_float(x)
    if f is None or f <= 0:
        return None
    try:
        return datetime.fromtimestamp(f, UTC).date()
    except (OverflowError, OSError, ValueError):
        return None


def parse_quote_summary(
    ticker: str, qs: dict[str, Any], as_of: date, cutoff: date
) -> dict[str, Any]:
    """quoteSummary result -> {"consensus", "actions", "intel", "stock"}."""
    fin = qs.get("financialData") or {}
    stats = qs.get("defaultKeyStatistics") or {}
    summ = qs.get("summaryDetail") or {}
    price = qs.get("price") or {}
    prof = qs.get("summaryProfile") or {}

    # --- recommendation trend (0m / -1m / -2m / -3m) ---
    rec_trend: dict[str, list[int]] = {}
    for row in (qs.get("recommendationTrend") or {}).get("trend") or []:
        p = str(row.get("period") or "")
        if not p:
            continue
        counts = [int(_coerce_float(row.get(k)) or 0)
                  for k in ("strongBuy", "buy", "hold", "sell", "strongSell")]
        rec_trend[p] = counts
    current = rec_trend.get("0m")

    # --- price targets ---
    mean_t = _pos(fin.get("targetMeanPrice"))
    targets = {
        "mean": mean_t,
        "median": _pos(fin.get("targetMedianPrice")),
        "high": _pos(fin.get("targetHighPrice")),
        "low": _pos(fin.get("targetLowPrice")),
        "n": _coerce_float(fin.get("numberOfAnalystOpinions")),
        "rec_mean": _coerce_float(fin.get("recommendationMean")),
        "yahoo_price": _pos(fin.get("currentPrice")) or _pos(price.get("regularMarketPrice")),
        "currency": price.get("currency") or summ.get("currency"),
        "fin_currency": fin.get("financialCurrency"),
    }

    consensus = None
    if current is not None or mean_t is not None:
        n_buckets = sum(current) if current else None
        consensus = {
            "ticker": ticker,
            "as_of_date": as_of,
            "source": "yfinance",
            "strong_buy": current[0] if current else None,
            "buy": current[1] if current else None,
            "hold": current[2] if current else None,
            "sell": current[3] if current else None,
            "strong_sell": current[4] if current else None,
            "mean_target": mean_t,
            "high_target": targets["high"],
            "low_target": targets["low"],
            "num_analysts": (n_buckets or None) if n_buckets else (
                int(targets["n"]) if targets["n"] else None
            ),
        }

    actions = actions_from_history(
        ticker, (qs.get("upgradeDowngradeHistory") or {}).get("history") or [], cutoff
    )

    # --- EPS trend / revisions / estimate counts per period ---
    eps: dict[str, dict[str, float | None]] = {}
    for row in (qs.get("earningsTrend") or {}).get("trend") or []:
        p = str(row.get("period") or "")
        if p not in ("0q", "+1q", "0y", "+1y"):
            continue
        tr = row.get("epsTrend") or {}
        rv = row.get("epsRevisions") or {}
        est = row.get("earningsEstimate") or {}
        rv_l = {str(k).lower(): v for k, v in rv.items()}
        eps[p] = {
            "cur": _coerce_float(tr.get("current")),
            "d7": _coerce_float(tr.get("7daysAgo")),
            "d30": _coerce_float(tr.get("30daysAgo")),
            "d60": _coerce_float(tr.get("60daysAgo")),
            "d90": _coerce_float(tr.get("90daysAgo")),
            "up7": _coerce_float(rv_l.get("uplast7days")),
            "up30": _coerce_float(rv_l.get("uplast30days")),
            "dn7": _coerce_float(rv_l.get("downlast7days")),
            "dn30": _coerce_float(rv_l.get("downlast30days")),
            "n": _coerce_float(est.get("numberOfAnalysts")),
            "growth": _coerce_float(row.get("growth")),
        }

    # --- earnings surprises (latest first) ---
    surprises = []
    for row in (qs.get("earningsHistory") or {}).get("history") or []:
        q = _epoch_to_date(row.get("quarter"))
        act, est = _coerce_float(row.get("epsActual")), _coerce_float(row.get("epsEstimate"))
        if q is None or act is None or est is None:
            continue
        surprises.append({"q": q.isoformat(), "act": act, "est": est,
                          "pct": _coerce_float(row.get("surprisePercent"))})
    surprises.sort(key=lambda r: r["q"], reverse=True)

    next_earn = None
    for d in ((qs.get("calendarEvents") or {}).get("earnings") or {}).get("earningsDate") or []:
        dd = _epoch_to_date(d)
        if dd is not None and (next_earn is None or dd < next_earn):
            next_earn = dd

    key_stats = {
        "fpe": _coerce_float(summ.get("forwardPE")) or _coerce_float(stats.get("forwardPE")),
        "tpe": _coerce_float(summ.get("trailingPE")),
        "feps": _coerce_float(stats.get("forwardEps")),
        "pb": _coerce_float(stats.get("priceToBook")),
        "ev_ebitda": _coerce_float(stats.get("enterpriseToEbitda")),
        "short_float": _coerce_float(stats.get("shortPercentOfFloat")),
        "short_ratio": _coerce_float(stats.get("shortRatio")),
        "shares_short": _coerce_float(stats.get("sharesShort")),
        "shares_short_prior": _coerce_float(stats.get("sharesShortPriorMonth")),
        "held_insiders": _coerce_float(stats.get("heldPercentInsiders")),
        "held_inst": _coerce_float(stats.get("heldPercentInstitutions")),
        "w52_change": _coerce_float(stats.get("52WeekChange")),
        "w52_high": _pos(summ.get("fiftyTwoWeekHigh")),
        "w52_low": _pos(summ.get("fiftyTwoWeekLow")),
        "mcap": _pos(summ.get("marketCap")) or _pos(price.get("marketCap")),
        "beta": _coerce_float(summ.get("beta")) or _coerce_float(stats.get("beta")),
        "roe": _coerce_float(fin.get("returnOnEquity")),
        "roa": _coerce_float(fin.get("returnOnAssets")),
        "op_margin": _coerce_float(fin.get("operatingMargins")),
        "gross_margin": _coerce_float(fin.get("grossMargins")),
        "profit_margin": _coerce_float(fin.get("profitMargins")),
        "rev_growth": _coerce_float(fin.get("revenueGrowth")),
        "earn_growth": _coerce_float(fin.get("earningsGrowth")),
        "de": _coerce_float(fin.get("debtToEquity")),
        "div_yield": _coerce_float(summ.get("dividendYield")),
    }

    intel = {
        "rec_trend": rec_trend,
        "targets": targets,
        "eps": eps,
        "surprises": surprises[:4],
        "next_earnings": next_earn.isoformat() if next_earn else None,
        "stats": {k: v for k, v in key_stats.items() if v is not None},
    }
    stock = {
        "name": price.get("longName") or price.get("shortName"),
        "sector": prof.get("sector"),
        "industry": prof.get("industry"),
        "market_cap": key_stats["mcap"],
        "beta": key_stats["beta"],
    }
    return {
        "consensus": consensus,
        "actions": actions,
        "intel": intel,
        "stock": {k: v for k, v in stock.items() if v not in (None, "")},
    }


_ACTION_MAP = {
    "up": "upgrade",
    "upgrade": "upgrade",
    "main": "reiterate",
    # "reit" and "reiterated" both appear across different yfinance schema
    # vintages for the same concept. Without mapping both to the same
    # canonical string, the SAME real analyst note landed under two
    # different `action` values on different crawls, and since `action` is
    # part of the AnalystAction unique index (ticker, firm_key, date,
    # action, source), that meant it bypassed dedup and was counted as two
    # separate rating events instead of one.
    "reit": "reiterate",
    "reiterated": "reiterate",
    "reiterate": "reiterate",
    "down": "downgrade",
    "downgrade": "downgrade",
    "init": "init",
    "initiated": "init",
}


def actions_from_history(ticker: str, history: list[dict], cutoff: date) -> list[dict]:
    """upgradeDowngradeHistory entries -> AnalystAction rows, INCLUDING the
    firm's current and prior price target and what it did to it."""
    rows: list[dict] = []
    for item in history:
        d = _epoch_to_date(item.get("epochGradeDate"))
        if d is None or d < cutoff:
            continue
        firm = str(item.get("firm") or "").strip()[:128] or None
        action_raw = str(item.get("action") or "").strip().lower()
        tgt_action = str(item.get("priceTargetAction") or "").strip().lower()[:16] or None
        rows.append(
            {
                "ticker": ticker,
                "firm": firm,
                "firm_key": canonical_firm_key(firm),
                "analyst": None,
                "action": _ACTION_MAP.get(action_raw, action_raw or None),
                "from_grade": (str(item.get("fromGrade") or "")[:64] or None),
                "to_grade": (str(item.get("toGrade") or "")[:64] or None),
                "target_price": _pos(item.get("currentPriceTarget")),
                "prior_target": _pos(item.get("priorPriceTarget")),
                "target_action": tgt_action,
                "date": d,
                "source": "yfinance",
            }
        )
    return rows


def _prices_frame_to_rows(df: pd.DataFrame, batch: list[str]) -> list[dict]:
    """Normalise yfinance multi-index frame into Price rows."""
    rows: list[dict] = []
    if df is None or df.empty:
        return rows

    def emit(ticker: str, frame: pd.DataFrame) -> None:
        for dt, r in frame.dropna(how="all").iterrows():
            close = _coerce_float(r.get("Close"))
            if close is None or close <= 0:
                continue
            rows.append(
                {
                    "ticker": ticker,
                    "date": pd.Timestamp(dt).date(),
                    "open": _coerce_float(r.get("Open")),
                    "high": _coerce_float(r.get("High")),
                    "low": _coerce_float(r.get("Low")),
                    "close": close,
                    "adj_close": _coerce_float(r.get("Adj Close")),
                    "volume": _coerce_float(r.get("Volume")),
                }
            )

    # Single-ticker result has flat columns, multi-ticker has MultiIndex with ticker as top level.
    if isinstance(df.columns, pd.MultiIndex):
        level0 = set(df.columns.get_level_values(0))
        for ticker in batch:
            if ticker in level0:
                emit(ticker, df[ticker])
    else:
        emit(batch[0], df)
    return rows


def _consensus_values(
    ticker: str, as_of: date, summary: pd.DataFrame | None, tgt: Any
) -> dict[str, Any] | None:
    """Build a Consensus row from a recommendations summary + price targets.

    Returns None when the feed gave us neither, so callers can skip the write.
    """
    row = _recs_summary_to_counts(summary)
    if row is None and not tgt:
        return None
    strong_buy = row.get("strongBuy") if row else None
    buy = row.get("buy") if row else None
    hold = row.get("hold") if row else None
    sell = row.get("sell") if row else None
    strong_sell = row.get("strongSell") if row else None
    num = None
    if row:
        num = sum(v for v in (strong_buy, buy, hold, sell, strong_sell) if v) or None
    mean_t = _coerce_float(tgt.get("mean") if isinstance(tgt, dict) else None)
    high_t = _coerce_float(tgt.get("high") if isinstance(tgt, dict) else None)
    low_t = _coerce_float(tgt.get("low") if isinstance(tgt, dict) else None)
    num_t = tgt.get("numberOfAnalysts") if isinstance(tgt, dict) else None
    if num is None and isinstance(num_t, (int, float)):
        num = int(num_t)
    return {
        "ticker": ticker,
        "as_of_date": as_of,
        "source": "yfinance",
        "strong_buy": strong_buy,
        "buy": buy,
        "hold": hold,
        "sell": sell,
        "strong_sell": strong_sell,
        "mean_target": mean_t,
        "high_target": high_t,
        "low_target": low_t,
        "num_analysts": num,
    }


def _consensus_upsert(values: dict[str, Any]):
    """Idempotent write keyed on (ticker, as_of_date, source)."""
    stmt = sqlite_insert(Consensus).values(**values)
    return stmt.on_conflict_do_update(
        index_elements=["ticker", "as_of_date", "source"],
        set_={
            "strong_buy": stmt.excluded.strong_buy,
            "buy": stmt.excluded.buy,
            "hold": stmt.excluded.hold,
            "sell": stmt.excluded.sell,
            "strong_sell": stmt.excluded.strong_sell,
            "mean_target": stmt.excluded.mean_target,
            "high_target": stmt.excluded.high_target,
            "low_target": stmt.excluded.low_target,
            "num_analysts": stmt.excluded.num_analysts,
        },
    )


def _recs_summary_to_counts(df: pd.DataFrame | None) -> dict[str, int] | None:
    if df is None or getattr(df, "empty", True):
        return None
    cols = {c.lower(): c for c in df.columns}
    needed = {"strongbuy", "buy", "hold", "sell", "strongsell"}
    if needed.issubset(set(cols)):
        # Filtering to period == "0m" can legitimately come back empty (only
        # historical rows); fall back to the first row rather than crash.
        current = df[df["period"] == "0m"] if "period" in df.columns else df
        latest = current.iloc[0] if not current.empty else df.iloc[0]
        return {
            "strongBuy": int(latest[cols["strongbuy"]] or 0),
            "buy": int(latest[cols["buy"]] or 0),
            "hold": int(latest[cols["hold"]] or 0),
            "sell": int(latest[cols["sell"]] or 0),
            "strongSell": int(latest[cols["strongsell"]] or 0),
        }
    if "To Grade" in df.columns:
        counts = {"strongBuy": 0, "buy": 0, "hold": 0, "sell": 0, "strongSell": 0}
        for g in df["To Grade"].dropna().astype(str).str.lower():
            if "strong buy" in g or "outperform" in g or "overweight" in g or "buy" in g:
                counts["buy"] += 1
            elif "hold" in g or "neutral" in g or "equal" in g or "market perform" in g:
                counts["hold"] += 1
            elif "sell" in g or "underperform" in g or "underweight" in g:
                counts["sell"] += 1
        return counts
    return None
