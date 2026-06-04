"""Build a per-ticker feature vector from the raw tables in SQLite."""
from __future__ import annotations

import json
import logging
from datetime import date, timedelta

import numpy as np
import pandas as pd
from sqlalchemy import select

from ..config import FEATURE_NAMES
from ..db import session_scope
from ..models import (
    AnalystAction,
    Consensus,
    FeatureSnapshot,
    Holding13F,
    InsiderTrade,
    Price,
)

logger = logging.getLogger(__name__)


def _load_prices(tickers: list[str], window_days: int = 180) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=window_days)
    with session_scope() as s:
        rows = s.execute(
            select(Price).where(Price.date >= cutoff, Price.ticker.in_(tickers))
        ).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "date", "close", "volume"])
    df = pd.DataFrame(
        [{"ticker": r.ticker, "date": r.date, "close": r.close, "volume": r.volume} for r in rows]
    )
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values(["ticker", "date"])


def _latest_consensus(tickers: list[str]) -> pd.DataFrame:
    """Latest *non-stale* consensus snapshot per ticker.

    Rows older than ``settings.consensus_max_age_days`` are ignored so a
    six-month-old Yahoo snapshot can't keep driving the ranker.
    """
    from ..config import get_settings

    cutoff = date.today() - timedelta(days=get_settings().consensus_max_age_days)
    with session_scope() as s:
        rows = s.execute(
            select(Consensus).where(
                Consensus.ticker.in_(tickers),
                Consensus.as_of_date >= cutoff,
            )
        ).scalars().all()
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(
        [
            {
                "ticker": r.ticker,
                "as_of_date": r.as_of_date,
                "source": r.source,
                "strong_buy": r.strong_buy or 0,
                "buy": r.buy or 0,
                "hold": r.hold or 0,
                "sell": r.sell or 0,
                "strong_sell": r.strong_sell or 0,
                "mean_target": r.mean_target,
                "num_analysts": r.num_analysts or 0,
            }
            for r in rows
        ]
    )
    # Prefer the most recent record per ticker, with finnhub breaking ties over yfinance.
    src_rank = {"finnhub": 0, "yfinance": 1, "finviz": 2}
    df["src_rank"] = df["source"].map(src_rank).fillna(9)
    df = df.sort_values(["ticker", "as_of_date", "src_rank"], ascending=[True, False, True])
    return df.drop_duplicates("ticker", keep="first")


def _historic_consensus(tickers: list[str], days_ago: int) -> pd.DataFrame:
    target = date.today() - timedelta(days=days_ago)
    with session_scope() as s:
        rows = s.execute(
            select(Consensus).where(
                Consensus.ticker.in_(tickers), Consensus.as_of_date <= target
            )
        ).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "mean_target"])
    df = pd.DataFrame(
        [{"ticker": r.ticker, "as_of_date": r.as_of_date, "mean_target": r.mean_target} for r in rows]
    )
    return df.sort_values("as_of_date").groupby("ticker", as_index=False).tail(1)


def _actions_window(tickers: list[str], days: int) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=days)
    with session_scope() as s:
        rows = s.execute(
            select(AnalystAction).where(
                AnalystAction.ticker.in_(tickers), AnalystAction.date >= cutoff
            )
        ).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "action", "firm"])
    return pd.DataFrame(
        [{"ticker": r.ticker, "action": r.action, "firm": r.firm} for r in rows]
    )


def _insider_window(tickers: list[str], days: int = 90) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=days)
    with session_scope() as s:
        rows = s.execute(
            select(InsiderTrade).where(
                InsiderTrade.ticker.in_(tickers), InsiderTrade.date >= cutoff
            )
        ).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "action", "shares", "price"])
    return pd.DataFrame(
        [
            {
                "ticker": r.ticker,
                "action": (r.action or "").lower(),
                "shares": r.shares or 0.0,
                "price": r.price or 0.0,
            }
            for r in rows
        ]
    )


def _inst_flow(tickers: list[str]) -> pd.DataFrame:
    """Pct change in aggregate shares held by filers quarter-over-quarter."""
    with session_scope() as s:
        rows = s.execute(select(Holding13F).where(Holding13F.ticker.in_(tickers))).scalars().all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "inst_flow_13f"])
    df = pd.DataFrame(
        [{"ticker": r.ticker, "quarter": r.quarter, "shares": r.shares or 0.0} for r in rows]
    )
    agg = df.groupby(["ticker", "quarter"], as_index=False)["shares"].sum()
    agg = agg.sort_values(["ticker", "quarter"])
    agg["prev"] = agg.groupby("ticker")["shares"].shift(1)
    agg["pct"] = (agg["shares"] - agg["prev"]) / agg["prev"].replace(0, np.nan)
    latest = agg.groupby("ticker").tail(1)
    return latest[["ticker", "pct"]].rename(columns={"pct": "inst_flow_13f"})


def build_features(tickers: list[str]) -> pd.DataFrame:
    """Return a DataFrame with one row per ticker and columns FEATURE_NAMES ∪ {ticker, last_close}."""
    prices = _load_prices(tickers)
    if prices.empty:
        logger.warning("no price data; features will be sparse")

    # Price momentum + volatility + liquidity + last close.
    price_feats = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        closes = g["close"].astype(float).values
        vols = g["volume"].astype(float).fillna(0).values
        if len(closes) < 2:
            continue
        last_close = float(closes[-1])
        mom_21 = float(closes[-1] / closes[max(0, len(closes) - 22)] - 1) if len(closes) > 22 else 0.0
        # realised vol (daily log returns, annualised).
        rets = np.diff(np.log(np.maximum(closes, 1e-9)))
        window = rets[-60:] if len(rets) >= 60 else rets
        vol = float(np.std(window) * np.sqrt(252)) if len(window) > 1 else 0.0
        dollar_vol = float(np.mean((closes[-20:] * vols[-20:])[-20:])) if len(closes) >= 20 else 0.0
        price_feats.append(
            {
                "ticker": t,
                "last_close": last_close,
                "price_mom_21d": mom_21,
                "risk_penalty": -vol,
                "dollar_volume_20d": dollar_vol,
            }
        )
    price_df = pd.DataFrame(price_feats)

    cons = _latest_consensus(tickers)
    cons_prev = _historic_consensus(tickers, days_ago=30).rename(
        columns={"mean_target": "mean_target_30d_ago"}
    )
    if not cons.empty:
        total = cons[["strong_buy", "buy", "hold", "sell", "strong_sell"]].sum(axis=1).replace(0, np.nan)
        cons["consensus_z"] = (
            2 * cons["strong_buy"] + cons["buy"] - cons["sell"] - 2 * cons["strong_sell"]
        ) / total
        # num_analysts = sum of every rating bucket. By construction this
        # equals Buy + Hold + Sell in the report, so the columns tie out.
        cons["num_analysts"] = total.fillna(0).astype(int)
        cons = cons.merge(price_df[["ticker", "last_close"]], on="ticker", how="left")
        cons["upside_z"] = cons["mean_target"] / cons["last_close"] - 1
        cons = cons.merge(cons_prev, on="ticker", how="left")
        cons["target_revision_30d"] = (
            cons["mean_target"] / cons["mean_target_30d_ago"] - 1
        ).replace([np.inf, -np.inf], np.nan)
    else:
        cons = pd.DataFrame(columns=["ticker", "consensus_z", "upside_z", "target_revision_30d"])

    acts_7 = _actions_window(tickers, 7)
    acts_30 = _actions_window(tickers, 30)

    def _net(df: pd.DataFrame) -> pd.Series:
        """Tier-weighted net rating-momentum per ticker.

        Each action is signed (+1 upgrade, −1 downgrade, 0 reiterate/etc.) and
        multiplied by the firm's tier weight (tier-1 = 1.0, tier-2 = 0.5,
        tier-3 / unknown = 0.25). A handful of Goldman / Morgan Stanley
        upgrades count for more than a dozen unknown-shop reiterations.
        """
        if df.empty:
            return pd.Series(dtype=float)
        from ..firms import firm_weight

        s = df["action"].astype(str).str.lower().fillna("")
        sign = np.where(s.str.contains("up"), 1.0, np.where(s.str.contains("down"), -1.0, 0.0))
        firms = df["firm"] if "firm" in df.columns else pd.Series([None] * len(df))
        tier_w = np.array([firm_weight(name) for name in firms.fillna("")], dtype=float)
        weighted = sign * tier_w
        return pd.DataFrame({"ticker": df["ticker"], "n": weighted}).groupby("ticker")["n"].sum()

    rating_mom_7d = _net(acts_7).rename("rating_mom_7d").reset_index()
    rating_mom_30d = _net(acts_30).rename("rating_mom_30d").reset_index()

    # Distinct firm count over the last 90 d — used by the outlook gate to
    # exclude thinly-covered names (where consensus is unreliable).
    cutoff_90 = date.today() - timedelta(days=90)
    with session_scope() as s:
        firm_rows = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff_90,
                AnalystAction.firm.isnot(None),
            )
        ).all()
    if firm_rows:
        firms_df = pd.DataFrame(firm_rows, columns=["ticker", "firm"])
        firm_count_90d = (
            firms_df.drop_duplicates()
            .groupby("ticker", as_index=False)["firm"]
            .count()
            .rename(columns={"firm": "firm_count_90d"})
        )
    else:
        firm_count_90d = pd.DataFrame(columns=["ticker", "firm_count_90d"])

    ins = _insider_window(tickers)
    if not ins.empty:
        signed = np.where(ins["action"].str.startswith("buy") | ins["action"].str.startswith("p"), 1, -1)
        ins["net_usd"] = signed * ins["shares"] * ins["price"]
        insider = ins.groupby("ticker", as_index=False)["net_usd"].sum().rename(
            columns={"net_usd": "insider_net_buy_90d"}
        )
    else:
        insider = pd.DataFrame(columns=["ticker", "insider_net_buy_90d"])

    inst = _inst_flow(tickers)

    # total_sources_count = distinct named contributors per ticker:
    #   sell-side firms in last 90 d  ∪
    #   tracked 13F filers (latest stored quarter)  ∪
    #   insider filers in last 90 d
    # This is the headline coverage number the report shows and the
    # outlook gate enforces (≥ settings.min_total_sources).
    cutoff_90 = date.today() - timedelta(days=90)
    with session_scope() as s:
        firm_pairs = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff_90,
                AnalystAction.firm.isnot(None),
            )
        ).all()
        filer_pairs = s.execute(
            select(Holding13F.ticker, Holding13F.filer_cik).where(
                Holding13F.ticker.in_(tickers),
                Holding13F.filer_cik.isnot(None),
            )
        ).all()
        insider_pairs = s.execute(
            select(InsiderTrade.ticker, InsiderTrade.filer).where(
                InsiderTrade.ticker.in_(tickers),
                InsiderTrade.date >= cutoff_90,
                InsiderTrade.filer.isnot(None),
            )
        ).all()
    sources_set: dict[str, set[tuple[str, str]]] = {}
    for t, firm in firm_pairs:
        sources_set.setdefault(t, set()).add(("firm", firm.lower().strip()))
    for t, cik in filer_pairs:
        sources_set.setdefault(t, set()).add(("13f", cik))
    for t, ifiler in insider_pairs:
        sources_set.setdefault(t, set()).add(("insider", ifiler.lower().strip()))
    total_sources = pd.DataFrame(
        [{"ticker": t, "total_sources_count": len(s_)} for t, s_ in sources_set.items()]
    ) if sources_set else pd.DataFrame(columns=["ticker", "total_sources_count"])

    # Merge all
    out = pd.DataFrame({"ticker": tickers})
    for d in (
        price_df, cons, rating_mom_7d, rating_mom_30d,
        insider, inst, firm_count_90d, total_sources,
    ):
        if d is not None and not d.empty:
            out = out.merge(d, on="ticker", how="left")
    if "firm_count_90d" not in out.columns:
        out["firm_count_90d"] = 0
    out["firm_count_90d"] = pd.to_numeric(out["firm_count_90d"], errors="coerce").fillna(0)
    if "total_sources_count" not in out.columns:
        out["total_sources_count"] = 0
    out["total_sources_count"] = pd.to_numeric(
        out["total_sources_count"], errors="coerce"
    ).fillna(0).astype(int)

    # Fill missing feature columns with 0 so the scoring stage doesn't drop rows.
    for col in FEATURE_NAMES:
        if col not in out.columns:
            out[col] = 0.0
        out[col] = pd.to_numeric(out[col], errors="coerce").fillna(0.0)

    if "last_close" not in out.columns:
        out["last_close"] = np.nan
    if "dollar_volume_20d" not in out.columns:
        out["dollar_volume_20d"] = 0.0
    return out


def persist_feature_snapshot(df: pd.DataFrame, as_of: date | None = None) -> int:
    """Write per-ticker feature JSON to `features` table. Returns row count."""
    as_of = as_of or date.today()
    written = 0
    with session_scope() as s:
        for _, r in df.iterrows():
            payload = {
                k: (None if pd.isna(r[k]) else float(r[k]))
                for k in (*FEATURE_NAMES, "last_close", "dollar_volume_20d")
                if k in df.columns
            }
            existing = s.get(FeatureSnapshot, (r["ticker"], as_of))
            if existing is None:
                s.add(
                    FeatureSnapshot(
                        ticker=r["ticker"], as_of=as_of, feature_json=json.dumps(payload)
                    )
                )
            else:
                existing.feature_json = json.dumps(payload)
            written += 1
    return written


def compute_and_persist(tickers: list[str]) -> pd.DataFrame:
    df = build_features(tickers)
    persist_feature_snapshot(df)
    return df
