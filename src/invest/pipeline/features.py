"""Build a per-ticker feature vector from the raw tables in SQLite.

Conventions (changed in the grading overhaul — see config.PRIOR_IC):

* A feature that was NOT OBSERVED for a ticker stays NaN. The scorer maps
  NaN to z = 0, the prior mean, which is the Bayesian answer to "no
  information". The previous code wrote a raw 0 instead, and a raw 0 is not
  neutral after standardisation: e.g. with most insiders net SELLERS, a
  stock with no Form 4 data at all ranked as if its insiders were buying.
  Only `config.ZERO_IS_OBSERVATION` features (no rating changes = a real
  observation of "nothing happened") are zero-filled.
* Every number that feeds the ranking passes a sanity check first: single-
  day price spikes that immediately revert are dropped, and price targets
  that are inconsistent with the price (wrong currency / ADR ratio / stale
  pre-split targets) are flagged `target_suspect` and their upside is
  discarded rather than ranked.
"""
from __future__ import annotations

import contextlib
import json
import logging
import math
from datetime import UTC, date, datetime, timedelta

import numpy as np
import pandas as pd
from sqlalchemy import select

from ..config import FEATURE_NAMES, ZERO_IS_OBSERVATION, get_settings, normalize_sector
from ..db import session_scope
from ..models import (
    AnalystAction,
    Consensus,
    FeatureSnapshot,
    Holding13F,
    InsiderTrade,
    IntelSnapshot,
    NewsItem,
    Price,
    SecFiling,
    Stock,
)

logger = logging.getLogger(__name__)

# Persisted snapshot layout. Snapshots are stored as a compact positional
# array ({"v": 2, "x": [...]}) because the database is committed to git and
# a key-per-value JSON dict was ~4x larger. Changing FEATURE_NAMES requires a
# NEW version entry here (test_features enforces it); old versions stay
# readable forever.
SNAPSHOT_SCHEMAS: dict[int, tuple[str, ...]] = {
    2: (
        "consensus_z", "consensus_delta", "upside_z", "target_dispersion",
        "target_revision_30d", "firm_target_revision", "rating_mom_7d", "rating_mom_30d",
        "eps_revision", "eps_revision_breadth", "earnings_surprise", "news_sentiment",
        "inst_flow_13f", "insider_signal", "short_interest", "activist_13d",
        "sec_red_flags", "value", "quality", "price_mom_5d", "price_mom_21d",
        "price_mom_63d", "mom_12_1", "high_52w", "risk_penalty",
        "last_close", "dollar_volume_20d", "vol_60d",
    ),
}
SNAPSHOT_VERSION = 2


# ------------------------------------------------------------------ prices


def _load_prices(tickers: list[str], window_days: int = 400) -> pd.DataFrame:
    """Load recent price history, excluding rows with a NULL close.

    yfinance occasionally returns a row for a date with no real close (seen
    live for PRX.AS); left in, a NULL on the most recent date poisons
    `last_close` and therefore upside. Dropping NULL-close rows makes
    `closes[-1]` the most recent GOOD close. 400 calendar days covers the
    253 trading days 12-1 momentum needs.
    """
    cutoff = date.today() - timedelta(days=window_days)
    with session_scope() as s:
        rows = s.execute(
            select(Price.ticker, Price.date, Price.close, Price.volume).where(
                Price.date >= cutoff, Price.ticker.in_(tickers), Price.close.isnot(None)
            )
        ).all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "date", "close", "volume"])
    df = pd.DataFrame(rows, columns=["ticker", "date", "close", "volume"])
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values(["ticker", "date"])


def spike_mask(closes: np.ndarray, threshold: float = 0.4, revert_tol: float = 0.1) -> np.ndarray:
    """True for points to KEEP. Drops isolated one-day spikes: a jump of
    more than `threshold` in log price that is fully reversed the next day.

    Observed live: APH printed 74.3 -> 143.7 -> 74.2 on consecutive days (a
    stale pre-split quote), which manufactured a +93 % / -48 % momentum and
    volatility pair out of a data glitch. Real moves of that size do not
    round-trip within one session.
    """
    keep = np.ones(len(closes), dtype=bool)
    if len(closes) < 3:
        return keep
    lc = np.log(np.maximum(closes.astype(float), 1e-12))
    for i in range(1, len(lc) - 1):
        up = lc[i] - lc[i - 1]
        down = lc[i + 1] - lc[i]
        if abs(up) > threshold and abs(down) > threshold and np.sign(up) != np.sign(down) \
                and abs(lc[i + 1] - lc[i - 1]) < revert_tol:
            keep[i] = False
    return keep


def _price_features(prices: pd.DataFrame) -> pd.DataFrame:
    feats = []
    today = pd.Timestamp(date.today())
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        closes_all = g["close"].astype(float).to_numpy()
        keep = spike_mask(closes_all)
        g = g[keep]
        closes = g["close"].astype(float).to_numpy()
        vols = g["volume"].astype(float).fillna(0).to_numpy()
        n = len(closes)
        if n < 2:
            continue
        last_close = float(closes[-1])
        # Each window uses `>=` (with N closes, index N-k is valid when N >= k).
        mom_5 = float(closes[-1] / closes[n - 6] - 1) if n >= 6 else 0.0
        mom_21 = float(closes[-1] / closes[n - 22] - 1) if n >= 22 else 0.0
        mom_63 = float(closes[-1] / closes[n - 64] - 1) if n >= 64 else 0.0
        # 12-1 momentum (Jegadeesh & Titman): return from t-252 to t-21,
        # skipping the most recent month, which reverses.
        mom_12_1 = float(closes[n - 22] / closes[n - 253] - 1) if n >= 253 else np.nan
        rets = np.diff(np.log(np.maximum(closes, 1e-9)))
        window = rets[-60:]
        vol = float(np.std(window) * np.sqrt(252)) if len(window) > 1 else np.nan
        dollar_vol = float(np.mean(closes[-20:] * vols[-20:])) if n >= 20 else 0.0
        feats.append(
            {
                "ticker": t,
                "last_close": last_close,
                "price_mom_5d": mom_5,
                "price_mom_21d": mom_21,
                "price_mom_63d": mom_63,
                "mom_12_1": mom_12_1,
                "vol_60d": vol,
                "risk_penalty": -vol if vol == vol else np.nan,
                "dollar_volume_20d": dollar_vol,
                "last_price_age_days": int((today - pd.Timestamp(g["date"].iloc[-1])).days),
                "price_history_days": int(n),
                "price_spikes_dropped": int((~keep).sum()),
            }
        )
    return pd.DataFrame(feats)


# --------------------------------------------------------------- consensus


def _latest_consensus(tickers: list[str]) -> pd.DataFrame:
    """Latest *non-stale* consensus snapshot per ticker.

    Rating counts come from the source with the deepest coverage (counts
    from different aggregators aren't additive); mean_target is the MEDIAN
    across every source's latest row so one stale / mis-scaled aggregator
    can't skew the upside.
    """
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
                "high_target": r.high_target,
                "low_target": r.low_target,
                "num_analysts": r.num_analysts or 0,
            }
            for r in rows
        ]
    )
    df = df.sort_values(["ticker", "as_of_date"], ascending=[True, False])
    latest_per_source = df.drop_duplicates(["ticker", "source"], keep="first")
    target_med = (
        latest_per_source.dropna(subset=["mean_target"])
        .groupby("ticker", as_index=False)[["mean_target", "high_target", "low_target"]]
        .median()
    )
    counts = (
        latest_per_source.sort_values("num_analysts", ascending=False)
        .drop_duplicates("ticker", keep="first")
        .drop(columns=["mean_target", "high_target", "low_target"])
    )
    return counts.merge(target_med, on="ticker", how="left")


def _historic_consensus(tickers: list[str], days_ago: int) -> pd.DataFrame:
    """Consensus target as of the closest available snapshot >= `days_ago`
    old, aggregated with the same cross-source median as `_latest_consensus`
    so `target_revision_30d` compares like with like."""
    target = date.today() - timedelta(days=days_ago)
    with session_scope() as s:
        rows = s.execute(
            select(Consensus.ticker, Consensus.as_of_date, Consensus.mean_target).where(
                Consensus.ticker.in_(tickers), Consensus.as_of_date <= target
            )
        ).all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "mean_target"])
    df = pd.DataFrame(rows, columns=["ticker", "as_of_date", "mean_target"])
    ref_date = df.groupby("ticker")["as_of_date"].transform("max")
    at_ref = df[df["as_of_date"] == ref_date]
    return (
        at_ref.dropna(subset=["mean_target"])
        .groupby("ticker", as_index=False)["mean_target"]
        .median()
    )


def _rating_score(counts: list | tuple | None) -> tuple[float, int] | None:
    """(net rating score in [-2, 2], n) from [sb, b, h, s, ss]."""
    if not counts or len(counts) < 5:
        return None
    sb, b, h, s, ss = (float(x or 0) for x in counts[:5])
    n = sb + b + h + s + ss
    if n <= 0:
        return None
    return (2 * sb + b - s - 2 * ss) / n, int(n)


# ----------------------------------------------------------------- actions


def _actions_window(tickers: list[str], days: int) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=days)
    with session_scope() as s:
        rows = s.execute(
            select(
                AnalystAction.ticker, AnalystAction.action, AnalystAction.firm,
                AnalystAction.target_price, AnalystAction.prior_target,
                AnalystAction.target_action, AnalystAction.date,
            ).where(AnalystAction.ticker.in_(tickers), AnalystAction.date >= cutoff)
        ).all()
    cols = ["ticker", "action", "firm", "target_price", "prior_target", "target_action", "date"]
    if not rows:
        return pd.DataFrame(columns=cols)
    return pd.DataFrame(rows, columns=cols)


def _net_rating_momentum(df: pd.DataFrame) -> pd.Series:
    """Tier-weighted net rating changes per ticker (+1 upgrade, −1 downgrade,
    0 otherwise; × firm tier weight 1.0 / 0.5 / 0.25)."""
    if df.empty:
        return pd.Series(dtype=float)
    from ..firms import firm_weight

    s = df["action"].astype(str).str.lower().fillna("")
    sign = np.where(s.str.contains("up"), 1.0, np.where(s.str.contains("down"), -1.0, 0.0))
    tier_w = np.array([firm_weight(name) for name in df["firm"].fillna("")], dtype=float)
    return pd.DataFrame({"ticker": df["ticker"], "n": sign * tier_w}).groupby("ticker")["n"].sum()


def _firm_target_changes(df: pd.DataFrame) -> pd.DataFrame:
    """Per-firm price-target revisions in the window, tier-weighted.

    log(new / prior) per action, clipped to ±1; an action that says
    "raises"/"lowers" without numbers counts ±0.05. Most sell-side notes
    keep the rating and move only the target, so this is where most
    opinion change actually shows up (Brav & Lehavy 2003).
    """
    cols = ["ticker", "firm_target_revision", "target_raises_30d", "target_cuts_30d"]
    if df.empty:
        return pd.DataFrame(columns=cols)
    from ..firms import firm_weight

    recs: dict[str, list[tuple[float, float]]] = {}
    raises: dict[str, int] = {}
    cuts: dict[str, int] = {}
    for r in df.itertuples(index=False):
        tp, pp = r.target_price, r.prior_target
        act = (r.target_action or "").lower()
        val = None
        if tp and pp and tp > 0 and pp > 0:
            val = float(np.clip(math.log(tp / pp), -1.0, 1.0))
        elif act.startswith("rais"):
            val = 0.05
        elif act.startswith("lower"):
            val = -0.05
        if val is None:
            continue
        recs.setdefault(r.ticker, []).append((val, firm_weight(r.firm)))
        if val > 0:
            raises[r.ticker] = raises.get(r.ticker, 0) + 1
        elif val < 0:
            cuts[r.ticker] = cuts.get(r.ticker, 0) + 1
    out = []
    for t, vals in recs.items():
        w = sum(x[1] for x in vals)
        out.append({
            "ticker": t,
            "firm_target_revision": sum(v * wt for v, wt in vals) / w if w else np.nan,
            "target_raises_30d": raises.get(t, 0),
            "target_cuts_30d": cuts.get(t, 0),
        })
    return pd.DataFrame(out, columns=cols)


# ----------------------------------------------------------------- insiders


def _insider_window(tickers: list[str], days: int = 90) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=days)
    with session_scope() as s:
        rows = s.execute(
            select(InsiderTrade.ticker, InsiderTrade.action, InsiderTrade.shares,
                   InsiderTrade.price).where(
                InsiderTrade.ticker.in_(tickers), InsiderTrade.date >= cutoff
            )
        ).all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "action", "shares", "price"])
    df = pd.DataFrame(rows, columns=["ticker", "action", "shares", "price"])
    df["action"] = df["action"].fillna("").astype(str).str.lower()
    df["shares"] = pd.to_numeric(df["shares"], errors="coerce").fillna(0.0)
    df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0)
    return df


# -------------------------------------------------------------------- 13F


def _quarter_key(q: str) -> float:
    """'2026Q2' -> 8106 (year*4 + quarter number), for integer quarter-gap math."""
    try:
        year, qn = q.split("Q")
        return int(year) * 4 + int(qn)
    except (ValueError, AttributeError):
        return np.nan


def current_13f_filers(tickers: list[str]) -> dict[str, set[str]]:
    """{ticker: CIKs of tracked filers holding it in the latest two report
    periods}. Filers whose newest stored 13F is older (one tracked filer's
    latest stored portfolio is from 2024) no longer count as current holders.
    Shared by the coverage gate and the report so the two can't disagree."""
    with session_scope() as s:
        rows = s.execute(
            select(Holding13F.ticker, Holding13F.filer_cik, Holding13F.quarter).where(
                Holding13F.ticker.in_(tickers), Holding13F.filer_cik.isnot(None)
            )
        ).all()
    if not rows:
        return {}
    keys = [_quarter_key(q) for _, _, q in rows]
    valid = [k for k in keys if k == k]
    if not valid:
        return {}
    floor = max(valid) - 1
    out: dict[str, set[str]] = {}
    for (t, cik, _q), k in zip(rows, keys):
        if k == k and k >= floor:
            out.setdefault(t, set()).add(cik)
    return out


def _inst_flow(tickers: list[str]) -> pd.DataFrame:
    """Position-weighted average per-filer share change, quarter-over-quarter.

    Changes are computed PER (ticker, filer) and accepted only when the two
    snapshots are exactly one quarter apart and the prior position was
    nonzero (0 -> N is a new position, not a flow). Only filers whose newest
    period is current (within one quarter of the newest in the table) count.
    """
    with session_scope() as s:
        rows = s.execute(
            select(Holding13F.ticker, Holding13F.filer_cik, Holding13F.quarter, Holding13F.shares)
            .where(Holding13F.ticker.in_(tickers))
        ).all()
    if not rows:
        return pd.DataFrame(columns=["ticker", "inst_flow_13f"])
    df = pd.DataFrame(rows, columns=["ticker", "filer_cik", "quarter", "shares"])
    df["shares"] = pd.to_numeric(df["shares"], errors="coerce").fillna(0.0)
    agg = df.groupby(["ticker", "filer_cik", "quarter"], as_index=False)["shares"].sum()
    agg["qkey"] = agg["quarter"].map(_quarter_key)
    agg = agg.dropna(subset=["qkey"]).sort_values(["ticker", "filer_cik", "qkey"])
    if agg.empty:
        return pd.DataFrame(columns=["ticker", "inst_flow_13f"])
    newest_q = agg["qkey"].max()
    grp = agg.groupby(["ticker", "filer_cik"])
    agg["prev_shares"] = grp["shares"].shift(1)
    agg["prev_qkey"] = grp["qkey"].shift(1)
    valid = (agg["qkey"] - agg["prev_qkey"] == 1) & (agg["prev_shares"] > 0)
    agg["pct"] = np.where(
        valid, ((agg["shares"] - agg["prev_shares"]) / agg["prev_shares"]).clip(-0.95, 5.0), np.nan
    )
    latest = agg.groupby(["ticker", "filer_cik"]).tail(1)
    latest = latest[latest["qkey"] >= newest_q - 1].dropna(subset=["pct"])
    if latest.empty:
        return pd.DataFrame(columns=["ticker", "inst_flow_13f"])
    latest = latest.assign(w=latest["prev_shares"].clip(lower=0.0))

    out = []
    for t, g in latest.groupby("ticker"):
        w = g["w"].to_numpy()
        val = float(np.average(g["pct"], weights=w)) if w.sum() > 0 else float(g["pct"].mean())
        out.append({"ticker": t, "inst_flow_13f": val})
    return pd.DataFrame(out, columns=["ticker", "inst_flow_13f"])


# ------------------------------------------------------------ intel / news


def load_intel(tickers: list[str], kind: str) -> dict[str, dict]:
    with session_scope() as s:
        rows = s.execute(
            select(IntelSnapshot.ticker, IntelSnapshot.payload, IntelSnapshot.as_of).where(
                IntelSnapshot.ticker.in_(tickers), IntelSnapshot.kind == kind
            )
        ).all()
    out: dict[str, dict] = {}
    for t, payload, as_of in rows:
        try:
            d = json.loads(payload)
        except (TypeError, ValueError):
            continue
        if isinstance(d, dict):
            d["_as_of"] = as_of
            out[t] = d
    return out


def _f(x) -> float:
    try:
        v = float(x)
        return v if math.isfinite(v) else np.nan
    except (TypeError, ValueError):
        return np.nan


def _intel_features(intel: dict[str, dict], last_close: dict[str, float]) -> pd.DataFrame:
    """Features derived from the per-ticker Yahoo intel payload."""
    k = get_settings().consensus_shrinkage_k
    today = date.today()
    rows = []
    for t, p in intel.items():
        rec = p.get("rec_trend") or {}
        tg = p.get("targets") or {}
        st = p.get("stats") or {}
        eps = p.get("eps") or {}
        r: dict[str, float | str | None] = {"ticker": t}

        cur, prev = _rating_score(rec.get("0m")), _rating_score(rec.get("-1m"))
        if cur and prev:
            n = cur[1]
            r["consensus_delta"] = (cur[0] - prev[0]) * n / (n + k)
        prev3 = _rating_score(rec.get("-3m"))
        r["consensus_delta_3m"] = (cur[0] - prev3[0]) if cur and prev3 else np.nan

        mean_t, hi, lo = _f(tg.get("mean")), _f(tg.get("high")), _f(tg.get("low"))
        n_t = _f(tg.get("n"))
        if mean_t > 0 and hi > 0 and lo > 0 and (n_t != n_t or n_t >= 3):
            r["target_dispersion"] = (hi - lo) / mean_t

        revs, breadth = [], []
        for period in ("0y", "+1y"):
            e = eps.get(period) or {}
            c, d30 = _f(e.get("cur")), _f(e.get("d30"))
            if c == c and d30 == d30:
                revs.append(float(np.clip((c - d30) / max(abs(c), abs(d30), 0.05), -1, 1)))
            up, dn, na = _f(e.get("up30")), _f(e.get("dn30")), _f(e.get("n"))
            if up == up or dn == dn:
                up, dn = (up if up == up else 0.0), (dn if dn == dn else 0.0)
                denom = max(na if na == na else 0.0, up + dn, 1.0)
                breadth.append((up - dn) / denom)
        if revs:
            r["eps_revision"] = float(np.mean(revs))
        if breadth:
            r["eps_revision_breadth"] = float(np.mean(breadth))
        fy = eps.get("0y") or {}
        r["eps_fy_now"] = _f(fy.get("cur"))
        r["eps_fy_30d_ago"] = _f(fy.get("d30"))
        r["eps_up_30d"] = _f(fy.get("up30"))
        r["eps_down_30d"] = _f(fy.get("dn30"))

        surprises = p.get("surprises") or []
        if surprises:
            s0 = surprises[0]
            act, est = _f(s0.get("act")), _f(s0.get("est"))
            try:
                q_end = date.fromisoformat(str(s0.get("q")))
            except ValueError:
                q_end = None
            if act == act and est == est and q_end is not None:
                # Reports land ~5 weeks after quarter end; PEAD decays over
                # roughly one quarter (Bernard & Thomas 1989).
                age = (today - (q_end + timedelta(days=35))).days
                sue = float(np.clip((act - est) / max(abs(est), 0.05), -1, 1))
                r["last_surprise"] = sue
                if age <= 200:
                    r["earnings_surprise"] = sue * math.exp(-max(age, 0) / 90.0)
        ne = p.get("next_earnings")
        if ne:
            with contextlib.suppress(ValueError):
                r["next_earnings_days"] = (date.fromisoformat(ne) - today).days

        fpe, feps = _f(st.get("fpe")), _f(st.get("feps"))
        if fpe == fpe and fpe > 0:
            r["value"] = 1.0 / fpe
        elif feps == feps and feps < 0:
            r["value"] = -0.05  # loss-making on forward estimates: bottom of the value ranks
        r["short_interest"] = _f(st.get("short_float"))
        r["roe"], r["op_margin"], r["de"] = _f(st.get("roe")), _f(st.get("op_margin")), _f(st.get("de"))
        r["fwd_pe"] = fpe
        r["mcap"] = _f(st.get("mcap"))

        y_price = _f(tg.get("yahoo_price"))
        ours = last_close.get(t, np.nan)
        ref = y_price if y_price == y_price and y_price > 0 else ours
        w52h = _f(st.get("w52_high"))
        if ref == ref and w52h == w52h and w52h > 0:
            r["high_52w"] = float(min(ref / w52h, 1.5))
        r["w52_change"] = _f(st.get("w52_change"))
        r["yahoo_price"] = y_price
        r["target_median"] = _f(tg.get("median"))
        rows.append(r)
    return pd.DataFrame(rows)


def _quality_score(df: pd.DataFrame) -> pd.Series:
    """Mean percentile rank of ROE, operating margin and (low) leverage —
    a compact profitability/quality composite (Novy-Marx 2013;
    Asness, Frazzini & Pedersen 2019)."""
    parts = []
    for col, sign in (("roe", 1.0), ("op_margin", 1.0), ("de", -1.0)):
        if col in df.columns:
            x = pd.to_numeric(df[col], errors="coerce") * sign
            parts.append(x.rank(pct=True))
    if not parts:
        return pd.Series(np.nan, index=df.index)
    return pd.concat(parts, axis=1).mean(axis=1, skipna=True)


def _news_features(tickers: list[str]) -> pd.DataFrame:
    """Recency-weighted, relevance-weighted headline tone, shrunk to 0.

        S = Σ wᵢ sᵢ / (Σ wᵢ + k),   wᵢ = relevanceᵢ · 2^(−ageᵢ / half-life)

    The pseudo-count k pulls a ticker with one stray headline toward
    neutral; a name with a steady stream of clearly-toned coverage keeps
    most of its average (Tetlock 2007; news tone is short-lived).
    """
    settings = get_settings()
    now = datetime.now(UTC).replace(tzinfo=None)
    since = now - timedelta(days=settings.news_lookback_days)
    with session_scope() as s:
        rows = s.execute(
            select(NewsItem.ticker, NewsItem.published_at, NewsItem.sentiment,
                   NewsItem.relevance).where(
                NewsItem.ticker.in_(tickers), NewsItem.published_at >= since
            )
        ).all()
    cols = ["ticker", "news_sentiment", "news_count_7d", "news_pos_7d", "news_neg_7d"]
    if not rows:
        return pd.DataFrame(columns=cols)
    hl = max(settings.news_half_life_days, 0.1)
    agg: dict[str, list[float]] = {}
    for t, ts, sent, rel in rows:
        age_d = max((now - ts).total_seconds() / 86400.0, 0.0)
        w = (rel if rel is not None else 0.5) * 2.0 ** (-age_d / hl)
        a = agg.setdefault(t, [0.0, 0.0, 0.0, 0.0, 0.0])
        a[0] += w * (sent or 0.0)
        a[1] += w
        if age_d <= 7:
            a[2] += 1
            if (sent or 0) > 0.15:
                a[3] += 1
            elif (sent or 0) < -0.15:
                a[4] += 1
    out = [
        {"ticker": t, "news_sentiment": a[0] / (a[1] + settings.news_shrinkage_k),
         "news_count_7d": int(a[2]), "news_pos_7d": int(a[3]), "news_neg_7d": int(a[4])}
        for t, a in agg.items()
    ]
    return pd.DataFrame(out, columns=cols)


def _sec_features(tickers: list[str], observed: set[str]) -> pd.DataFrame:
    """Red-flag 8-K items / late filings (90 d), 13D activist stakes (180 d),
    registered offerings (90 d). Zero for crawled tickers with no events,
    NaN for tickers the filing stream has not covered yet."""
    from ..sources.edgar_src import (
        ACTIVIST_FORMS,
        LATE_FILING_FORMS,
        OFFERING_FORMS,
        RED_FLAG_ITEMS,
    )

    today = date.today()
    with session_scope() as s:
        rows = s.execute(
            select(SecFiling.ticker, SecFiling.form, SecFiling.filing_date, SecFiling.items).where(
                SecFiling.ticker.in_(tickers),
                SecFiling.filing_date >= today - timedelta(days=180),
            )
        ).all()
    stats: dict[str, dict[str, int]] = {t: {"sec_red_flags": 0, "activist_13d": 0,
                                            "offerings_90d": 0, "filings_8k_30d": 0}
                                        for t in observed}
    for t, form, fdate, items in rows:
        d = stats.setdefault(t, {"sec_red_flags": 0, "activist_13d": 0,
                                 "offerings_90d": 0, "filings_8k_30d": 0})
        age = (today - fdate).days
        item_set = {i.strip() for i in (items or "").split(",") if i.strip()}
        if age <= 90 and (item_set & RED_FLAG_ITEMS or form in LATE_FILING_FORMS):
            d["sec_red_flags"] += 1
        if form in ACTIVIST_FORMS:
            d["activist_13d"] += 1
        if age <= 90 and form in OFFERING_FORMS:
            d["offerings_90d"] += 1
        if age <= 30 and form.startswith(("8-K", "6-K")):
            d["filings_8k_30d"] += 1
    return pd.DataFrame([{"ticker": t, **v} for t, v in stats.items()],
                        columns=["ticker", "sec_red_flags", "activist_13d",
                                 "offerings_90d", "filings_8k_30d"])


# ------------------------------------------------------------------- build


def build_features(tickers: list[str]) -> pd.DataFrame:
    """One row per ticker: FEATURE_NAMES plus diagnostics/display columns.

    FEATURE_NAMES columns are NaN where unobserved (see module docstring).
    """
    settings = get_settings()
    prices = _load_prices(tickers)
    if prices.empty:
        logger.warning("no price data; features will be sparse")
    price_df = _price_features(prices)
    last_close = dict(zip(price_df.get("ticker", []), price_df.get("last_close", [])))

    cons = _latest_consensus(tickers)
    cons_prev = _historic_consensus(tickers, days_ago=30).rename(
        columns={"mean_target": "mean_target_30d_ago"}
    )
    if not cons.empty:
        total = cons[["strong_buy", "buy", "hold", "sell", "strong_sell"]].sum(axis=1).replace(0, np.nan)
        raw_consensus = (
            2 * cons["strong_buy"] + cons["buy"] - cons["sell"] - 2 * cons["strong_sell"]
        ) / total
        # Analyst-reliability shrinkage n/(n+k): a 3-analyst unanimous "buy"
        # can't outrank a 30-analyst 80 %-buy.
        n = total.fillna(0)
        cons["consensus_z"] = raw_consensus * (n / (n + settings.consensus_shrinkage_k))
        # Preserve the feed's analyst count (targets without a rating
        # breakdown are still real coverage) BEFORE overwriting it with the
        # bucket sum, which by construction equals Buy + Hold + Sell.
        cons["target_analysts"] = (
            pd.to_numeric(cons["num_analysts"], errors="coerce").fillna(0).astype(int)
        )
        cons["num_analysts"] = total.fillna(0).astype(int)
        cons = cons.merge(cons_prev, on="ticker", how="left")
        cons["target_revision_30d"] = (
            cons["mean_target"] / cons["mean_target_30d_ago"] - 1
        ).replace([np.inf, -np.inf], np.nan)
    else:
        cons = pd.DataFrame(columns=["ticker", "consensus_z", "mean_target", "target_revision_30d"])

    acts_7 = _actions_window(tickers, 7)
    acts_30 = _actions_window(tickers, 30)
    rating_mom_7d = _net_rating_momentum(acts_7).rename("rating_mom_7d").reset_index()
    rating_mom_30d = _net_rating_momentum(acts_30).rename("rating_mom_30d").reset_index()
    firm_targets = _firm_target_changes(acts_30)
    if not acts_30.empty:
        a = acts_30["action"].astype(str).str.lower()
        updown = pd.DataFrame({
            "ticker": acts_30["ticker"],
            "up": a.str.contains("up").astype(int),
            "down": a.str.contains("down").astype(int),
        }).groupby("ticker", as_index=False).sum().rename(
            columns={"up": "upgrades_30d", "down": "downgrades_30d"})
    else:
        updown = pd.DataFrame(columns=["ticker", "upgrades_30d", "downgrades_30d"])

    # Insider activity. `insider_net_buy_90d` (buy $ − sell $) is kept for
    # display; the scored `insider_signal` down-weights sales (most are
    # diversification / 10b5-1 plans and carry little information —
    # Lakonishok & Lee 2001) and scales by market cap so a $1M purchase at a
    # $500M company outweighs one at a $3T company.
    _INSIDER_SIGN = {"buy": 1.0, "sell": -1.0}
    ins = _insider_window(tickers)
    if not ins.empty:
        signed = ins["action"].map(_INSIDER_SIGN).fillna(0.0)
        usd = ins["shares"] * ins["price"]
        ins = ins.assign(
            net_usd=signed * usd,
            buy_usd=np.where(ins["action"] == "buy", usd, 0.0),
            sell_usd=np.where(ins["action"] == "sell", usd, 0.0),
        )
        insider = ins.groupby("ticker", as_index=False)[["net_usd", "buy_usd", "sell_usd"]].sum()
        insider = insider.rename(columns={"net_usd": "insider_net_buy_90d"})
    else:
        insider = pd.DataFrame(columns=["ticker", "insider_net_buy_90d", "buy_usd", "sell_usd"])

    inst = _inst_flow(tickers)

    intel = load_intel(tickers, "quote")
    intel_df = _intel_features(intel, last_close)
    if not intel_df.empty:
        intel_df["quality"] = _quality_score(intel_df)
    news = _news_features(tickers)
    sec_observed = set(load_intel(tickers, "sec"))
    sec = _sec_features(tickers, sec_observed)

    # Coverage buckets feeding `total_sources_count`:
    #   named_firm_sources — sell-side desks with a rating action in 90 d
    #                        (deduped by canonical firm key)
    #   inst_sources       — tracked 13F filers holding it in a CURRENT period
    #   insider_sources    — distinct insider filers in the last 90 d
    from ..firms import canonical_firm_key

    cutoff_90 = date.today() - timedelta(days=90)
    with session_scope() as s:
        firm_pairs = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff_90,
                AnalystAction.firm.isnot(None),
            )
        ).all()
        insider_pairs = s.execute(
            select(InsiderTrade.ticker, InsiderTrade.filer).where(
                InsiderTrade.ticker.in_(tickers),
                InsiderTrade.date >= cutoff_90,
                InsiderTrade.filer.isnot(None),
            )
        ).all()
        sectors = {t: normalize_sector(sec_) for t, sec_ in
                   s.query(Stock.ticker, Stock.sector).filter(Stock.ticker.in_(tickers))}
        mcaps = {t: m for t, m in
                 s.query(Stock.ticker, Stock.market_cap).filter(Stock.ticker.in_(tickers)) if m}
    named_firms: dict[str, set[str]] = {}
    insider_filers: dict[str, set[str]] = {}
    for t, firm, firm_key in firm_pairs:
        key = firm_key or canonical_firm_key(firm)
        if key:
            named_firms.setdefault(t, set()).add(key)
    for t, ifiler in insider_pairs:
        insider_filers.setdefault(t, set()).add(ifiler.lower().strip())
    inst_filers = current_13f_filers(tickers)
    source_buckets = pd.DataFrame(
        [
            {
                "ticker": t,
                "named_firm_sources": len(named_firms.get(t, ())),
                "firm_count_90d": len(named_firms.get(t, ())),
                "inst_sources": len(inst_filers.get(t, ())),
                "insider_sources": len(insider_filers.get(t, ())),
            }
            for t in tickers
        ]
    )

    # `cons` must not carry its own last_close or the merge would suffix it.
    cons = cons.drop(columns=["last_close"], errors="ignore")
    out = pd.DataFrame({"ticker": tickers})
    for d in (price_df, cons, rating_mom_7d, rating_mom_30d, firm_targets, updown,
              insider, inst, intel_df, news, sec, source_buckets):
        if d is not None and not d.empty:
            out = out.merge(d, on="ticker", how="left")
    collided = [c for c in out.columns if c.endswith(("_x", "_y"))]
    if collided:
        raise RuntimeError(
            f"feature merge produced duplicated columns {collided}; "
            "two source frames share a column name — drop the duplicate before merging"
        )

    for _c in ("num_analysts", "target_analysts", "named_firm_sources", "firm_count_90d",
               "inst_sources", "insider_sources"):
        if _c not in out.columns:
            out[_c] = 0
        out[_c] = pd.to_numeric(out[_c], errors="coerce").fillna(0).astype(int)

    # total_sources_count = distinct contributors backing the name. The
    # sell-side bucket is max(covering analysts, named 90-day changers) —
    # the changers are a subset of the coverage universe, so summing them
    # would double-count.
    out["sell_side_sources"] = np.maximum(
        np.maximum(out["num_analysts"], out["target_analysts"]), out["named_firm_sources"]
    ).astype(int)
    out["total_sources_count"] = (
        out["sell_side_sources"] + out["inst_sources"] + out["insider_sources"]
    ).astype(int)

    for col in ("last_close", "mean_target", "high_target", "low_target", "yahoo_price",
                "mom_12_1", "w52_change", "mcap", "buy_usd", "sell_usd"):
        if col not in out.columns:
            out[col] = np.nan
        out[col] = pd.to_numeric(out[col], errors="coerce")

    # ---- target sanity: discard upside that can't be trusted ----
    lc = out["last_close"]
    tol = settings.target_price_mismatch_tol
    band = settings.target_band_factor
    yp = out["yahoo_price"]
    mismatch = (yp > 0) & (lc > 0) & ((yp / lc - 1).abs() > tol)
    outside = (
        (out["low_target"] > 0) & (lc > 0) & (lc < out["low_target"] / band)
    ) | ((out["high_target"] > 0) & (lc > out["high_target"] * band))
    out["target_suspect"] = (mismatch | outside).fillna(False).astype(bool)
    upside = out["mean_target"] / lc - 1
    out["upside_z"] = upside.where(~out["target_suspect"]).replace([np.inf, -np.inf], np.nan)
    if out["target_suspect"].any():
        logger.info("target sanity: discarded upside for %d tickers: %s",
                    int(out["target_suspect"].sum()),
                    ", ".join(out.loc[out["target_suspect"], "ticker"].head(30)))

    # 12-1 momentum fallback from Yahoo's 52-week change when we hold less
    # than a year of history: (1 + r_12m) / (1 + r_1m) − 1.
    if "price_mom_21d" in out.columns:
        fb = (1 + out["w52_change"]) / (1 + pd.to_numeric(out["price_mom_21d"], errors="coerce")) - 1
        out["mom_12_1"] = out["mom_12_1"].fillna(fb)

    # Insider signal (see above): NaN when no Form 4 data at all.
    mcap = out["mcap"].fillna(out["ticker"].map(mcaps))
    has_ins = out["ticker"].isin(set(ins["ticker"])) if not ins.empty else pd.Series(False, index=out.index)
    sig = (out["buy_usd"].fillna(0) - 0.3 * out["sell_usd"].fillna(0)) / mcap
    out["insider_signal"] = sig.where(has_ins & (mcap > 0))
    out["mcap"] = mcap

    out["sector"] = out["ticker"].map(sectors).fillna("")

    for col in FEATURE_NAMES:
        if col not in out.columns:
            out[col] = np.nan
        out[col] = pd.to_numeric(out[col], errors="coerce").replace([np.inf, -np.inf], np.nan)
        if col in ZERO_IS_OBSERVATION:
            out[col] = out[col].fillna(0.0)

    if "dollar_volume_20d" not in out.columns:
        out["dollar_volume_20d"] = 0.0
    out["dollar_volume_20d"] = pd.to_numeric(out["dollar_volume_20d"], errors="coerce").fillna(0.0)
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
    if "vol_60d" not in out.columns:
        out["vol_60d"] = np.nan
    return out


# ------------------------------------------------------------- snapshots


def _round(v: float | None) -> float | None:
    if v is None or not math.isfinite(v):
        return None
    if v == 0:
        return 0.0
    return float(f"{v:.5g}")


def persist_feature_snapshot(df: pd.DataFrame, as_of: date | None = None) -> int:
    """Write today's per-ticker feature vectors (compact positional JSON)."""
    as_of = as_of or date.today()
    fields = SNAPSHOT_SCHEMAS[SNAPSHOT_VERSION]
    written = 0
    with session_scope() as s:
        for _, r in df.iterrows():
            vals = []
            for k in fields:
                v = r[k] if k in df.columns else None
                vals.append(None if v is None or pd.isna(v) else _round(float(v)))
            payload = json.dumps({"v": SNAPSHOT_VERSION, "x": vals}, separators=(",", ":"))
            existing = s.get(FeatureSnapshot, (r["ticker"], as_of))
            if existing is None:
                s.add(FeatureSnapshot(ticker=r["ticker"], as_of=as_of, feature_json=payload))
            else:
                existing.feature_json = payload
            written += 1
    return written


def decode_snapshot(feature_json: str) -> dict[str, float | None]:
    """Snapshot JSON (any version, incl. the legacy key/value dict) -> dict."""
    try:
        data = json.loads(feature_json)
    except (TypeError, ValueError):
        return {}
    if isinstance(data, dict) and "v" in data and "x" in data:
        fields = SNAPSHOT_SCHEMAS.get(int(data["v"]))
        if not fields:
            return {}
        return dict(zip(fields, data["x"]))
    if isinstance(data, dict):
        # Legacy (v1) snapshots stored names that were later renamed.
        legacy = dict(data)
        if "insider_net_buy_90d" in legacy:
            legacy.pop("insider_net_buy_90d")  # raw $ — not comparable to insider_signal
        return legacy
    return {}


def load_feature_snapshots(min_as_of: date | None = None) -> pd.DataFrame:
    """All stored snapshots as a long frame [ticker, as_of, <fields>...]."""
    q = select(FeatureSnapshot.ticker, FeatureSnapshot.as_of, FeatureSnapshot.feature_json)
    if min_as_of is not None:
        q = q.where(FeatureSnapshot.as_of >= min_as_of)
    with session_scope() as s:
        rows = s.execute(q).all()
    if not rows:
        return pd.DataFrame()
    recs = []
    for t, as_of, js in rows:
        d = decode_snapshot(js)
        if d:
            recs.append({"ticker": t, "as_of": as_of, **d})
    df = pd.DataFrame(recs)
    for col in FEATURE_NAMES:
        if col not in df.columns:
            df[col] = np.nan
    return df


def compute_and_persist(tickers: list[str]) -> pd.DataFrame:
    df = build_features(tickers)
    persist_feature_snapshot(df)
    return df
