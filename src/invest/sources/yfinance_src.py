"""yfinance-backed source: prices, fundamentals, consensus, price targets, rating actions."""
from __future__ import annotations

import logging
import time
from datetime import date, datetime, timedelta
from typing import Any

import pandas as pd
import yfinance as yf
from sqlalchemy.dialects.sqlite import insert as sqlite_insert

from ..db import session_scope
from ..firms import canonical_firm_key
from ..models import Consensus, Price, Stock
from ..universe import chunks
from .base import BaseSource, TransientSourceError, log_run, upsert_analyst_actions, with_retries

logger = logging.getLogger(__name__)

_BATCH_SIZE = 40


class YFinanceSource(BaseSource):
    name = "yfinance"
    rate_per_minute = 240.0  # generous — yfinance enforces its own throttling

    # --------------------------- prices ---------------------------

    @with_retries
    def _download_prices(self, tickers: list[str], period: str = "90d") -> pd.DataFrame:
        self.throttle(len(tickers))
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

    def ingest_prices(self, tickers: list[str]) -> int:
        rows_written = 0
        for batch in chunks(tickers, _BATCH_SIZE):
            try:
                df = self._download_prices(batch)
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

    # ------------------------ fundamentals ------------------------

    @with_retries
    def _ticker_info(self, ticker: str) -> dict[str, Any]:
        self.throttle()
        try:
            info = yf.Ticker(ticker).info or {}
        except Exception as e:  # noqa: BLE001
            raise TransientSourceError(str(e)) from e
        return info

    def ingest_fundamentals(self, tickers: list[str]) -> int:
        written = 0
        now = datetime.utcnow()
        with session_scope() as s:
            for t in tickers:
                try:
                    info = self._ticker_info(t)
                except TransientSourceError:
                    continue
                existing = s.get(Stock, t)
                name = info.get("longName") or info.get("shortName")
                sector = info.get("sector")
                industry = info.get("industry")
                mcap = _coerce_float(info.get("marketCap"))
                beta = _coerce_float(info.get("beta"))
                # CUSIP lets SEC 13F holdings match on the authoritative
                # security identifier instead of fuzzy company names.
                cusip = info.get("cusip") or info.get("CUSIP")
                cusip = str(cusip).strip().upper()[:12] if cusip else None
                if existing is None:
                    s.add(
                        Stock(
                            ticker=t,
                            name=name,
                            sector=sector,
                            industry=industry,
                            market_cap=mcap,
                            beta=beta,
                            cusip=cusip,
                            in_universe=True,
                            updated_at=now,
                        )
                    )
                else:
                    if name:
                        existing.name = name
                    if sector:
                        existing.sector = sector
                    if industry:
                        existing.industry = industry
                    if cusip:
                        existing.cusip = cusip
                    if mcap is not None:
                        existing.market_cap = mcap
                    if beta is not None:
                        existing.beta = beta
                    existing.in_universe = True
                    existing.updated_at = now
                written += 1
        return written

    # -------------------- consensus + targets ---------------------

    @with_retries
    def _recs_summary(self, ticker: str, tk: Any = None) -> pd.DataFrame | None:
        self.throttle()
        try:
            tk = tk or yf.Ticker(ticker)
            # Newer yfinance: .recommendations_summary; older: fall back to .recommendations
            df = getattr(tk, "recommendations_summary", None)
            if df is None or (hasattr(df, "empty") and df.empty):
                df = getattr(tk, "recommendations", None)
        except Exception as e:  # noqa: BLE001
            raise TransientSourceError(str(e)) from e
        return df

    @with_retries
    def _price_targets(self, ticker: str, tk: Any = None) -> dict[str, Any]:
        self.throttle()
        try:
            tk = tk or yf.Ticker(ticker)
            tgt = getattr(tk, "analyst_price_targets", None)
            return tgt or {}
        except Exception as e:  # noqa: BLE001
            raise TransientSourceError(str(e)) from e

    def ingest_consensus(self, tickers: list[str]) -> int:
        today = date.today()
        written = 0
        with session_scope() as s:
            for t in tickers:
                # One Ticker object per symbol: yfinance caches the quoteSummary
                # response on the instance, so the recs + targets pair costs one
                # network round-trip instead of two.
                tk = yf.Ticker(t)
                try:
                    summary = self._recs_summary(t, tk)
                    tgt = self._price_targets(t, tk)
                except TransientSourceError:
                    continue
                values = _consensus_values(t, today, summary, tgt)
                if values is None:
                    continue
                s.execute(_consensus_upsert(values))
                written += 1
        return written

    # ------------------- upgrades / downgrades --------------------

    @with_retries
    def _upgrades(self, ticker: str, tk: Any = None) -> pd.DataFrame | None:
        self.throttle()
        try:
            tk = tk or yf.Ticker(ticker)
            df = getattr(tk, "upgrades_downgrades", None)
            if df is None or (hasattr(df, "empty") and df.empty):
                df = getattr(tk, "recommendations", None)
            return df
        except Exception as e:  # noqa: BLE001
            raise TransientSourceError(str(e)) from e

    def ingest_actions(self, tickers: list[str], lookback_days: int = 90) -> int:
        cutoff = date.today() - timedelta(days=lookback_days)
        all_rows: list[dict] = []
        for t in tickers:
            try:
                df = self._upgrades(t)
            except TransientSourceError:
                continue
            if df is None or getattr(df, "empty", True):
                continue
            all_rows.extend(_actions_frame_to_rows(df, t, cutoff))
        # Upsert on (ticker, firm_key, date, action, source) so re-crawling
        # the same historical action updates the existing row instead of
        # creating a duplicate "source".
        return upsert_analyst_actions(all_rows)

    # ------------------------ combined coverage -------------------------

    def ingest_coverage(
        self,
        tickers: list[str],
        budget_seconds: float = 0.0,
        lookback_days: int = 90,
    ) -> tuple[int, int]:
        """Crawl consensus + price targets + named rating actions in one pass.

        This is the hourly workhorse. Doing all three per symbol against a
        single ``yf.Ticker`` reuses yfinance's per-instance response cache, so
        a full sweep costs roughly what consensus alone used to.

        ``budget_seconds`` (0 = unlimited) caps wall-clock time. Callers pass
        the stalest tickers first, so a truncated sweep still makes forward
        progress and the universe cycles across runs instead of a slow run
        blowing the job timeout.

        Returns ``(rows_written, tickers_processed)``.
        """
        today = date.today()
        cutoff = today - timedelta(days=lookback_days)
        started = time.monotonic()
        written = 0
        processed = 0
        action_rows: list[dict] = []
        for t in tickers:
            if budget_seconds and (time.monotonic() - started) > budget_seconds:
                logger.info(
                    "coverage sweep hit its %.0fs budget after %d/%d tickers; "
                    "the remainder are the stalest next run",
                    budget_seconds, processed, len(tickers),
                )
                break
            tk = yf.Ticker(t)
            try:
                summary = self._recs_summary(t, tk)
                tgt = self._price_targets(t, tk)
            except TransientSourceError:
                summary, tgt = None, {}
            consensus_row = _consensus_values(t, today, summary, tgt)
            if consensus_row is not None:
                with session_scope() as s:
                    s.execute(_consensus_upsert(consensus_row))
                written += 1
            try:
                df = self._upgrades(t, tk)
            except TransientSourceError:
                df = None
            if df is not None and not getattr(df, "empty", True):
                action_rows.extend(_actions_frame_to_rows(df, t, cutoff))
            processed += 1
        if action_rows:
            written += upsert_analyst_actions(action_rows)
        return written, processed

    # --------------------------- run -----------------------------

    def run(self, tickers: list[str]) -> int:  # noqa: D401
        total = 0
        with log_run("yfinance.prices") as c:
            c["rows"] = self.ingest_prices(tickers)
            total += c["rows"]
        with log_run("yfinance.fundamentals") as c:
            c["rows"] = self.ingest_fundamentals(tickers)
            total += c["rows"]
        with log_run("yfinance.consensus") as c:
            c["rows"] = self.ingest_consensus(tickers)
            total += c["rows"]
        with log_run("yfinance.actions") as c:
            c["rows"] = self.ingest_actions(tickers)
            total += c["rows"]
        return total


# ----------------------------- helpers -----------------------------


def _coerce_float(x: Any) -> float | None:
    try:
        if x is None:
            return None
        f = float(x)
        if f != f:  # NaN
            return None
        return f
    except (TypeError, ValueError):
        return None


def _prices_frame_to_rows(df: pd.DataFrame, batch: list[str]) -> list[dict]:
    """Normalise yfinance multi-index frame into Price rows."""
    rows: list[dict] = []
    if df is None or df.empty:
        return rows
    # Single-ticker result has flat columns, multi-ticker has MultiIndex with ticker as top level.
    if isinstance(df.columns, pd.MultiIndex):
        for ticker in batch:
            if ticker not in df.columns.get_level_values(0):
                continue
            sub = df[ticker].dropna(how="all")
            for dt, r in sub.iterrows():
                rows.append(
                    {
                        "ticker": ticker,
                        "date": pd.Timestamp(dt).date(),
                        "open": _coerce_float(r.get("Open")),
                        "high": _coerce_float(r.get("High")),
                        "low": _coerce_float(r.get("Low")),
                        "close": _coerce_float(r.get("Close")),
                        "adj_close": _coerce_float(r.get("Adj Close")),
                        "volume": _coerce_float(r.get("Volume")),
                    }
                )
    else:
        ticker = batch[0]
        for dt, r in df.dropna(how="all").iterrows():
            rows.append(
                {
                    "ticker": ticker,
                    "date": pd.Timestamp(dt).date(),
                    "open": _coerce_float(r.get("Open")),
                    "high": _coerce_float(r.get("High")),
                    "low": _coerce_float(r.get("Low")),
                    "close": _coerce_float(r.get("Close")),
                    "adj_close": _coerce_float(r.get("Adj Close")),
                    "volume": _coerce_float(r.get("Volume")),
                }
            )
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
    # Newer yfinance returns a frame with columns strongBuy/buy/hold/sell/strongSell and
    # rows indexed by 'period' (0m, -1m ...). We want the most recent (period == 0m).
    cols = {c.lower(): c for c in df.columns}
    needed = {"strongbuy", "buy", "hold", "sell", "strongsell"}
    if needed.issubset(set(cols)):
        # `df` is guaranteed non-empty by the guard above, but filtering to
        # period == "0m" can legitimately come back empty (e.g. a feed with
        # only historical -1m/-2m/-3m rows and no current snapshot yet) — an
        # unguarded `.iloc[0]` there raised IndexError, which was NOT a
        # TransientSourceError, so it propagated out of the per-ticker loop
        # in `ingest_coverage`/`ingest_consensus` and aborted the sweep for
        # every remaining ticker in the batch. Fall back to the first row of
        # the full frame (still real data, just not guaranteed "current")
        # rather than crash.
        current = df[df["period"] == "0m"] if "period" in df.columns else df
        latest = current.iloc[0] if not current.empty else df.iloc[0]
        return {
            "strongBuy": int(latest[cols["strongbuy"]] or 0),
            "buy": int(latest[cols["buy"]] or 0),
            "hold": int(latest[cols["hold"]] or 0),
            "sell": int(latest[cols["sell"]] or 0),
            "strongSell": int(latest[cols["strongsell"]] or 0),
        }
    # Older schema: a long frame of individual actions with a "To Grade" column; aggregate.
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


def _actions_frame_to_rows(df: pd.DataFrame, ticker: str, cutoff: date) -> list[dict]:
    rows: list[dict] = []
    idx = df.reset_index()
    # Column name normalisation.
    cols = {c.lower(): c for c in idx.columns}

    def col(name: str) -> str | None:
        for k, v in cols.items():
            if name in k:
                return v
        return None

    date_col = col("date") or col("grade date")
    firm_col = col("firm")
    action_col = col("action")
    from_col = col("from grade") or col("fromgrade")
    to_col = col("to grade") or col("tograde")
    if not (date_col and firm_col):
        return rows
    for _, r in idx.iterrows():
        d = pd.Timestamp(r[date_col]).date() if pd.notna(r[date_col]) else None
        if d is None or d < cutoff:
            continue
        action_raw = str(r[action_col]).strip().lower() if action_col else ""
        firm = str(r[firm_col])[:128] if firm_col else None
        rows.append(
            {
                "ticker": ticker,
                "firm": firm,
                "firm_key": canonical_firm_key(firm),
                "analyst": None,
                "action": _ACTION_MAP.get(action_raw, action_raw or None),
                "from_grade": str(r[from_col])[:64] if from_col and pd.notna(r[from_col]) else None,
                "to_grade": str(r[to_col])[:64] if to_col and pd.notna(r[to_col]) else None,
                "target_price": None,
                "date": d,
                "source": "yfinance",
            }
        )
    return rows
