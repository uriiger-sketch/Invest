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
    # Cross-source merge instead of winner-takes-all:
    #  - rating counts come from the source with the deepest coverage
    #    (max num_analysts) — counts from different aggregators aren't
    #    additive, so we can't sum them.
    #  - mean_target is the MEDIAN across every source's latest row, so a
    #    single aggregator's stale/mis-scaled target can't skew the upside.
    df = df.sort_values(["ticker", "as_of_date"], ascending=[True, False])
    latest_per_source = df.drop_duplicates(["ticker", "source"], keep="first")

    target_med = (
        latest_per_source.dropna(subset=["mean_target"])
        .groupby("ticker", as_index=False)["mean_target"]
        .median()
    )
    counts = (
        latest_per_source.sort_values("num_analysts", ascending=False)
        .drop_duplicates("ticker", keep="first")
        .drop(columns=["mean_target"])
    )
    merged = counts.merge(target_med, on="ticker", how="left")
    return merged


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
        # Data-quality fields for the reliability gate: how fresh is the last
        # close, and how much history backs the vol/momentum numbers.
        last_dt = g["date"].iloc[-1]
        last_price_age = (pd.Timestamp(date.today()) - pd.Timestamp(last_dt)).days
        price_feats.append(
            {
                "ticker": t,
                "last_close": last_close,
                "price_mom_21d": mom_21,
                "risk_penalty": -vol,
                "dollar_volume_20d": dollar_vol,
                "last_price_age_days": int(last_price_age),
                "price_history_days": int(len(closes)),
            }
        )
    price_df = pd.DataFrame(price_feats)

    cons = _latest_consensus(tickers)
    cons_prev = _historic_consensus(tickers, days_ago=30).rename(
        columns={"mean_target": "mean_target_30d_ago"}
    )
    if not cons.empty:
        from ..config import get_settings as _gs

        total = cons[["strong_buy", "buy", "hold", "sell", "strong_sell"]].sum(axis=1).replace(0, np.nan)
        raw_consensus = (
            2 * cons["strong_buy"] + cons["buy"] - cons["sell"] - 2 * cons["strong_sell"]
        ) / total
        # Analyst-reliability shrinkage: multiply by n/(n+k) so a 3-analyst
        # unanimous "buy" (raw = 1.0, shrunk ≈ 0.23 with k=10) can't outrank a
        # 30-analyst 80 %-buy (raw = 0.8, shrunk = 0.6). More opinions →
        # more trust in the consensus number.
        k = _gs().consensus_shrinkage_k
        n = total.fillna(0)
        cons["consensus_z"] = raw_consensus * (n / (n + k))
        # Preserve the feed's own analyst count BEFORE overwriting it below.
        # Yahoo reports `numberOfAnalysts` alongside the price target, which
        # can be non-zero for names that have targets but no published
        # buy/hold/sell breakdown — real coverage the bucket sum can't see.
        cons["target_analysts"] = (
            pd.to_numeric(cons["num_analysts"], errors="coerce").fillna(0).astype(int)
        )
        # num_analysts = sum of every rating bucket. By construction this
        # equals Buy + Hold + Sell in the report, so the columns tie out.
        # Do NOT widen this to include target_analysts: the report's column
        # math depends on the identity, and a user already reported the
        # mismatch once.
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
    #
    # Dedup by canonical firm_key, NOT the raw firm string: different feeds
    # spell the same real firm differently ("Goldman Sachs" vs "Goldman
    # Sachs & Co."), and without this the same analyst desk gets counted as
    # multiple separate sources. firm_key is populated at insert time by the
    # ingesters; fall back to computing it on the fly for any row where it
    # isn't (e.g. rows written before the firm_key column existed).
    from ..firms import canonical_firm_key

    cutoff_90 = date.today() - timedelta(days=90)
    with session_scope() as s:
        firm_rows = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff_90,
                AnalystAction.firm.isnot(None),
            )
        ).all()
    if firm_rows:
        firms_df = pd.DataFrame(firm_rows, columns=["ticker", "firm", "firm_key"])
        firms_df["key"] = firms_df["firm_key"].where(
            firms_df["firm_key"].notna() & (firms_df["firm_key"] != ""),
            firms_df["firm"].map(canonical_firm_key),
        )
        firm_count_90d = (
            firms_df.drop_duplicates(["ticker", "key"])
            .groupby("ticker", as_index=False)["key"]
            .count()
            .rename(columns={"key": "firm_count_90d"})
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

    # Coverage buckets feeding `total_sources_count` (assembled after the
    # merge below, because the sell-side bucket also needs `num_analysts`):
    #   named_firm_sources — sell-side desks that published a rating ACTION
    #                        in the last 90 d, deduped by canonical_firm_key
    #                        so one desk spelled two ways counts once
    #   inst_sources       — distinct 13F filers holding the name
    #   insider_sources    — distinct insider filers in the last 90 d
    cutoff_90 = date.today() - timedelta(days=90)
    with session_scope() as s:
        firm_pairs = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
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
    named_firms: dict[str, set[str]] = {}
    inst_filers: dict[str, set[str]] = {}
    insider_filers: dict[str, set[str]] = {}
    for t, firm, firm_key in firm_pairs:
        key = firm_key or canonical_firm_key(firm)
        if key:
            named_firms.setdefault(t, set()).add(key)
    for t, cik in filer_pairs:
        inst_filers.setdefault(t, set()).add(cik)
    for t, ifiler in insider_pairs:
        insider_filers.setdefault(t, set()).add(ifiler.lower().strip())

    _bucket_tickers = set(named_firms) | set(inst_filers) | set(insider_filers)
    source_buckets = pd.DataFrame(
        [
            {
                "ticker": t,
                "named_firm_sources": len(named_firms.get(t, ())),
                "inst_sources": len(inst_filers.get(t, ())),
                "insider_sources": len(insider_filers.get(t, ())),
            }
            for t in _bucket_tickers
        ]
    ) if _bucket_tickers else pd.DataFrame(
        columns=["ticker", "named_firm_sources", "inst_sources", "insider_sources"]
    )

    # Merge all.
    #
    # `cons` carries its own copy of `last_close` (it needs it to compute
    # upside_z). Left in place, the unsuffixed merge below would produce
    # `last_close_x` / `last_close_y` and NO plain `last_close` column — so
    # the guard further down silently set last_close to NaN for every single
    # ticker, poisoning the persisted feature snapshots and the ML training
    # set. price_df is the authoritative source, so drop the duplicate here.
    cons = cons.drop(columns=["last_close"], errors="ignore")

    out = pd.DataFrame({"ticker": tickers})
    for d in (
        price_df, cons, rating_mom_7d, rating_mom_30d,
        insider, inst, firm_count_90d, source_buckets,
    ):
        if d is not None and not d.empty:
            out = out.merge(d, on="ticker", how="left")
    # Any accidental duplicate-column suffixes would silently break the
    # downstream guards, so fail loudly rather than shipping NaN features.
    collided = [c for c in out.columns if c.endswith(("_x", "_y"))]
    if collided:
        raise RuntimeError(
            f"feature merge produced duplicated columns {collided}; "
            "two source frames share a column name — drop the duplicate before merging"
        )
    if "firm_count_90d" not in out.columns:
        out["firm_count_90d"] = 0
    out["firm_count_90d"] = pd.to_numeric(out["firm_count_90d"], errors="coerce").fillna(0)
    for _bucket in ("named_firm_sources", "inst_sources", "insider_sources"):
        if _bucket not in out.columns:
            out[_bucket] = 0
        out[_bucket] = pd.to_numeric(out[_bucket], errors="coerce").fillna(0).astype(int)

    # total_sources_count = distinct contributors backing the name.
    #
    # The sell-side bucket is max(num_analysts, named_firm_sources), NOT their
    # sum: `num_analysts` is the count of desks currently *covering* the stock
    # (the buy/hold/sell census), while `named_firm_sources` counts desks that
    # published a rating *change* in the last 90 d — a strict subset of the
    # coverage universe, just the only ones we learn the name of. Summing them
    # would double-count every firm that both covers the name and moved on it.
    #
    # This previously counted ONLY the named 90-day changers, which is why a
    # freshly-restored database reported 0 sources for all 301 tickers and the
    # coverage gate rejected the entire universe: no rating-change history had
    # been crawled yet, even though consensus showed 30-50 covering analysts.
    # A stock followed by 45 analysts is well covered whether or not any of
    # them happened to change their rating this quarter.
    for _c in ("num_analysts", "target_analysts"):
        if _c not in out.columns:
            out[_c] = 0
        out[_c] = pd.to_numeric(out[_c], errors="coerce").fillna(0).astype(int)
    out["sell_side_sources"] = np.maximum(
        np.maximum(out["num_analysts"], out["target_analysts"]),
        out["named_firm_sources"],
    ).astype(int)
    out["total_sources_count"] = (
        out["sell_side_sources"] + out["inst_sources"] + out["insider_sources"]
    ).astype(int)

    # Fill missing feature columns with 0 so the scoring stage doesn't drop rows.
    for col in FEATURE_NAMES:
        if col not in out.columns:
            out[col] = 0.0
        out[col] = pd.to_numeric(out[col], errors="coerce").fillna(0.0)

    if "last_close" not in out.columns:
        out["last_close"] = np.nan
    if "dollar_volume_20d" not in out.columns:
        out["dollar_volume_20d"] = 0.0
    # Data-quality columns: tickers with no price rows at all get worst-case
    # defaults so the reliability gate excludes them rather than passing NaN.
    if "last_price_age_days" not in out.columns:
        out["last_price_age_days"] = 999
    out["last_price_age_days"] = pd.to_numeric(
        out["last_price_age_days"], errors="coerce"
    ).fillna(999).astype(int)
    if "price_history_days" not in out.columns:
        out["price_history_days"] = 0
    out["price_history_days"] = pd.to_numeric(
        out["price_history_days"], errors="coerce"
    ).fillna(0).astype(int)
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
