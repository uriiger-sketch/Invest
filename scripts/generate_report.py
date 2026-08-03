"""Render top-20 per horizon to REPORT.md and docs/index.html.

Reads the latest persisted scores from SQLite and writes a human-readable
report that GitHub can render directly, plus a self-contained HTML page
that GitHub Pages serves without needing any runtime fetch.
"""
from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timedelta
from pathlib import Path

from sqlalchemy import desc, select

from invest.config import HORIZONS, get_settings
from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Holding13F, Price, RunLog, Score, Stock

HERE = Path(__file__).resolve().parent.parent
REPORT_MD = HERE / "REPORT.md"
REPORT_HTML = HERE / "docs" / "index.html"
HISTORY_PATH = HERE / "docs" / "history.jsonl"


# Pretty display names per horizon (the keys are short for storage / config).
HORIZON_TITLE: dict[str, str] = {
    "hours": "Next few hours",
    "daily": "Daily (~5 trading days)",
    "weekly": "Weekly (~1 month)",
    "monthly": "Month and above (~90 days)",
}


# Per-horizon plain-English explainer shown in the report header.
HORIZON_BLURB: dict[str, str] = {
    "hours": (
        "Next few hours / next session. Fastest signal — leans almost entirely "
        "on short-term price momentum and very-recent rating changes. Heaviest "
        "risk penalty (intraday noise is large)."
    ),
    "daily": (
        "About a week of holding (5 trading days). Same flavour as 'hours' but "
        "with more weight on 30-day rating momentum and the consensus snapshot."
    ),
    "weekly": (
        "About a month of holding (20 trading days). Balanced mix of consensus, "
        "price-target upside, rating momentum and price trend."
    ),
    "monthly": (
        "A quarter or more (90+ trading days). Leans on analyst consensus, "
        "price-target upside, and institutional (13F) flow; actively de-weights "
        "short-term price chase."
    ),
}


# Column definitions. Order matches the tables.
HORIZON_COLUMN_DOCS: list[tuple[str, str]] = [
    ("#", "Rank (1 = highest blended score in this horizon)."),
    (
        "★★ / ★★★ / ★★★★",
        "Cross-horizon highlight. ★★ = this ticker ranks in two of the four "
        "top lists; ★★★ = three of four; ★★★★ = all four horizons agree. "
        "High-conviction names.",
    ),
    ("Ticker", "Stock symbol as used on US exchanges."),
    ("Name", "Company name from Yahoo Finance."),
    ("Sector", "GICS sector classification."),
    (
        "Blended",
        "Final score = 0.6 · z(composite) + 0.4 · z(ml). Z-scored across the "
        "universe for this horizon, so 0 is average. +1 ≈ 1 std-dev above the "
        "pack. Higher = more attractive.",
    ),
    (
        "Composite",
        "Rule-based score from the weighted sum of nine transparent features "
        "(analyst consensus, price-target upside, tier-weighted rating "
        "momentum, target revision, 13F institutional flow, insider net buy, "
        "price momentum, realised-volatility risk penalty).",
    ),
    (
        "ML",
        "LightGBM regressor's predicted forward return for this horizon. "
        "Cold-start fallback = composite until ≥ 60 daily snapshots exist.",
    ),
    (
        "Pctile",
        "Percentile of the blended score inside this horizon (100 % = top).",
    ),
]


SNAPSHOT_COLUMN_DOCS: list[tuple[str, str]] = [
    ("Ticker / Sector", "Stock symbol + GICS sector."),
    (
        "Upside",
        "Analyst consensus mean target / last close − 1. Only stocks with "
        "≥ 4 % upside survive the quality gate, so every row here is bullish.",
    ),
    (
        "Buy / Hold / Sell",
        "Aggregated analyst rating counts (most recent consensus snapshot). "
        "Strong Buy + Buy → 'Buy'; Strong Sell + Sell → 'Sell'. By "
        "construction Buy + Hold + Sell == Analysts.",
    ),
    (
        "Analysts",
        "Total number of sell-side analyst firms covering the stock — "
        "sourced from yfinance's recommendations_summary plus Finnhub / FMP "
        "when API keys are configured.",
    ),
    (
        "Tier-1 firms",
        "Distinct count of tier-1 firms (Goldman, Morgan Stanley, JPM, BofA, "
        "Citi, Barclays, UBS, Jefferies, Evercore, Wells Fargo, RBC, BMO, "
        "Cowen, Wedbush, Stifel, Truist, Mizuho, …) that have issued an "
        "action on this ticker in the last 90 days. Higher = better-pedigree "
        "coverage.",
    ),
    (
        "Insts",
        "Count of tracked institutional 13F filers (Berkshire, BlackRock, "
        "Bridgewater, Renaissance, Citadel, Tiger, ARK …) currently holding "
        "the stock in their most recent 13F-HR.",
    ),
    (
        "Sources",
        "Distinct named contributors backing this stock's signal: "
        "sell-side firms with a rating action in the last 90 d ∪ tracked "
        "13F filers (latest stored quarter) ∪ insider filers (Form-4) in "
        "the last 90 d. Every top-listed stock is required to have at "
        "least 50 distinct sources — this is the floor that proves the "
        "ranking isn't driven by any single feed.",
    ),
    (
        "Horizons",
        "Which of {hours, daily, weekly, monthly} top lists the ticker "
        "appears in.",
    ),
]


# Kept for backwards-compatibility with the HTML <details> dl block.
COLUMN_DOCS: list[tuple[str, str]] = HORIZON_COLUMN_DOCS


# Stable sector → colour palette (deterministic by hash, so order-insensitive).
def _sector_colour(sector: str) -> str:
    if not sector:
        return "#9aa0a6"
    h = int(hashlib.md5(sector.encode("utf-8")).hexdigest(), 16)
    hue = h % 360
    return f"hsl({hue}, 55%, 55%)"


def _latest_as_of() -> date | None:
    try:
        with session_scope() as s:
            row = s.execute(select(Score.as_of).order_by(desc(Score.as_of)).limit(1)).first()
        return row[0] if row else None
    except Exception:
        return None


def _top_rows(horizon: str, as_of: date, n: int) -> list[dict]:
    from invest.pipeline.rank import select_diversified

    with session_scope() as s:
        raw = (
            s.query(
                Score.ticker,
                Score.blended_score,
                Score.composite_score,
                Score.ml_score,
                Score.percentile,
                Stock.name,
                Stock.sector,
            )
            .outerjoin(Stock, Stock.ticker == Score.ticker)
            .filter(Score.horizon == horizon, Score.as_of == as_of)
            .order_by(Score.blended_score.desc())
            .limit(n * 4)
            .all()
        )
    # Same per-sector diversification cap the CLI's top_n applies, so the
    # report and terminal output can never disagree on the top list.
    candidates = [
        {
            "ticker": r.ticker,
            "sector": r.sector,
            "_row": r,
        }
        for r in raw
    ]
    rows = [c["_row"] for c in select_diversified(candidates, n)]
    tickers = [r.ticker for r in rows]
    extras = _enrichment_for(tickers)
    return [
        {
            "rank": i + 1,
            "ticker": r.ticker,
            "name": r.name or "",
            "sector": r.sector or "",
            "blended": r.blended_score,
            "composite": r.composite_score,
            "ml": r.ml_score,
            "percentile": r.percentile,
            **extras.get(r.ticker, {}),
        }
        for i, r in enumerate(rows)
    ]


def _enrichment_for(tickers: list[str]) -> dict[str, dict]:
    """Per-ticker extras for the top-20: last close, consensus bar, firm count,
    institutional holder count, list of recent analyst actions."""
    if not tickers:
        return {}
    out: dict[str, dict] = {t: {} for t in tickers}

    with session_scope() as s:
        # Last close per ticker. Excludes NULL-close rows (yfinance
        # occasionally has a date with no real close for a given ticker,
        # observed live for PRX.AS) — without this, the report displayed
        # "—" for Price/Upside on a stock that had a perfectly good score,
        # target and gate-passing history, just because its single most
        # recent price row happened to be a data gap.
        for t in tickers:
            row = (
                s.query(Price.close, Price.date)
                .filter(Price.ticker == t, Price.close.isnot(None))
                .order_by(Price.date.desc())
                .first()
            )
            if row:
                out[t]["last_close"] = row.close

        # Latest consensus per ticker (prefer finnhub over yfinance).
        for t in tickers:
            c = (
                s.query(Consensus)
                .filter(Consensus.ticker == t)
                .order_by(Consensus.as_of_date.desc())
                .first()
            )
            if c:
                buy = (c.strong_buy or 0) + (c.buy or 0)
                hold = c.hold or 0
                sell = (c.sell or 0) + (c.strong_sell or 0)
                # Total analysts = sum of every rating bucket = num_analysts.
                # By construction `analysts == buy + hold + sell` so the row
                # numbers tie out for the user — no more "more buy+hold+sell
                # than firms" confusion.
                out[t]["buy"] = buy
                out[t]["hold"] = hold
                out[t]["sell"] = sell
                out[t]["strong_buy"] = c.strong_buy or 0
                out[t]["strong_sell"] = c.strong_sell or 0
                out[t]["analysts"] = buy + hold + sell
                out[t]["mean_target"] = c.mean_target
                last = out[t].get("last_close")
                if c.mean_target and last:
                    out[t]["upside_pct"] = c.mean_target / last - 1

        # Recent analyst-firm activity (last 90 d) for the per-row drawer.
        # NOTE: this is intentionally separate from `analysts` above — it
        # measures how many distinct firms have CHANGED their rating
        # recently, not total coverage.
        for t in tickers:
            recent = (
                s.query(AnalystAction)
                .filter(AnalystAction.ticker == t)
                .order_by(AnalystAction.date.desc())
                .limit(6)
                .all()
            )
            out[t]["recent_actions"] = [
                {
                    "date": a.date,
                    "firm": a.firm,
                    "action": a.action,
                    "from": a.from_grade,
                    "to": a.to_grade,
                    "target": a.target_price,
                    "source": a.source,
                }
                for a in recent
            ]

        # Distinct 13F filer count (latest quarter in data).
        for t in tickers:
            holders_q = (
                s.query(Holding13F.filer_cik)
                .filter(Holding13F.ticker == t)
                .distinct()
                .all()
            )
            out[t]["inst_count"] = len(holders_q)
    return out


# ------------------------------- Markdown --------------------------------










def _collect_top_by_horizon(as_of: date, n: int) -> dict[str, list[dict]]:
    """Pull top-N rows once per horizon, then annotate every row with the count
    AND labels of horizons in which that ticker also appears."""
    by_h = {h: _top_rows(h, as_of, n) for h in HORIZONS}
    # Map ticker -> ordered horizon labels it appears in.
    horizons_for: dict[str, list[str]] = {}
    for h in HORIZONS:
        for r in by_h[h]:
            horizons_for.setdefault(r["ticker"], []).append(h)
    for rows in by_h.values():
        for r in rows:
            r["horizon_count"] = len(horizons_for.get(r["ticker"], []))
            r["horizons"] = horizons_for.get(r["ticker"], [])
    return by_h


def _firm_identity(firm: str | None, firm_key: str | None) -> str:
    """Canonical identity for a (firm, firm_key) row pair. Prefer the stored
    firm_key (set at insert time); fall back to computing it on the fly for
    rows written before the firm_key column existed."""
    from invest.firms import canonical_firm_key

    return firm_key or canonical_firm_key(firm)


def _tier1_count_per_ticker(tickers: list[str], lookback_days: int = 90) -> dict[str, int]:
    """Distinct tier-1 firms with an action on the ticker in the lookback
    window. Deduped by canonical identity — "Goldman Sachs" and "Goldman
    Sachs & Co." must count as ONE firm, not two."""
    if not tickers:
        return {}
    from invest.firms import firm_tier

    cutoff = date.today() - timedelta(days=lookback_days)
    seen: dict[str, set[str]] = {}
    with session_scope() as s:
        rows = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
        ).all()
    for t, firm, firm_key in rows:
        if firm_tier(firm) != 1:
            continue
        key = _firm_identity(firm, firm_key)
        if key:
            seen.setdefault(t, set()).add(key)
    return {t: len(keys) for t, keys in seen.items()}


def _total_sources_per_ticker(tickers: list[str]) -> dict[str, int]:
    """Distinct contributors per ticker, matching `features.build_features`.

        max(covering analysts, named rating-changers in 90 d)
        + tracked 13F filers + insider filers in 90 d

    The sell-side bucket takes the MAX, not the sum: the firms that published
    a rating change are a subset of the firms covering the stock — we just
    only learn the names of the former. Summing would double-count them.

    This must stay identical to the feature computation, otherwise the column
    the reader sees disagrees with the gate that selected the row. It did
    disagree once: the report showed `Sources = 0` next to picks that had
    supposedly cleared a 12-source floor, because this counted only named
    rating-changers while the ranking ran on a different definition.
    """
    if not tickers:
        return {}
    from invest.models import Holding13F, InsiderTrade

    cutoff = date.today() - timedelta(days=90)
    named: dict[str, set[str]] = {}
    insts: dict[str, set[str]] = {}
    insiders: dict[str, set[str]] = {}
    with session_scope() as s:
        for t, firm, firm_key in s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
        ).all():
            key = _firm_identity(firm, firm_key)
            if key:
                named.setdefault(t, set()).add(key)
        for t, cik in s.execute(
            select(Holding13F.ticker, Holding13F.filer_cik).where(
                Holding13F.ticker.in_(tickers),
                Holding13F.filer_cik.isnot(None),
            )
        ).all():
            insts.setdefault(t, set()).add(cik)
        for t, ifiler in s.execute(
            select(InsiderTrade.ticker, InsiderTrade.filer).where(
                InsiderTrade.ticker.in_(tickers),
                InsiderTrade.date >= cutoff,
                InsiderTrade.filer.isnot(None),
            )
        ).all():
            insiders.setdefault(t, set()).add(ifiler.lower().strip())

    covering = _covering_analysts_per_ticker(tickers)
    return {
        t: max(covering.get(t, 0), len(named.get(t, ())))
        + len(insts.get(t, ()))
        + len(insiders.get(t, ()))
        for t in tickers
    }


def _covering_analysts_per_ticker(tickers: list[str]) -> dict[str, int]:
    """Covering-analyst count from the freshest consensus snapshot per ticker.

    Uses the larger of the rating-bucket sum and the feed's own
    `num_analysts`, since a name can carry price targets without a published
    buy/hold/sell breakdown.
    """
    if not tickers:
        return {}
    cutoff = date.today() - timedelta(days=get_settings().consensus_max_age_days)
    best: dict[str, tuple[date, int]] = {}
    with session_scope() as s:
        rows = s.execute(
            select(Consensus).where(
                Consensus.ticker.in_(tickers),
                Consensus.as_of_date >= cutoff,
            )
        ).scalars().all()
    for r in rows:
        buckets = sum(
            v or 0 for v in (r.strong_buy, r.buy, r.hold, r.sell, r.strong_sell)
        )
        n = max(buckets, r.num_analysts or 0)
        prev = best.get(r.ticker)
        if prev is None or r.as_of_date > prev[0]:
            best[r.ticker] = (r.as_of_date, n)
        elif r.as_of_date == prev[0]:
            best[r.ticker] = (prev[0], max(prev[1], n))
    return {t: n for t, (_, n) in best.items()}






def _named_firms_for_tickers(tickers: list[str], lookback_days: int = 90) -> dict[str, list[tuple[str, int]]]:
    """For each ticker, return the distinct named sell-side firms seen in
    the last `lookback_days` along with each firm's tier (0..3). Deduped by
    canonical identity — the same real firm shows once, using the
    alphabetically-first raw spelling seen, not once per spelling variant.
    Sorted by tier ASC (tier-1 first) then by firm name."""
    if not tickers:
        return {}
    from invest.firms import firm_tier

    cutoff = date.today() - timedelta(days=lookback_days)
    out: dict[str, dict[str, str]] = {}  # ticker -> {canonical key: representative name}
    with session_scope() as s:
        for t, firm, firm_key in s.execute(
            select(AnalystAction.ticker, AnalystAction.firm, AnalystAction.firm_key).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
        ).all():
            key = _firm_identity(firm, firm_key)
            if not key:
                continue
            bucket = out.setdefault(t, {})
            if key not in bucket or firm.lower() < bucket[key].lower():
                bucket[key] = firm
    return {
        t: sorted(((f, firm_tier(f)) for f in reps.values()), key=lambda x: (x[1] or 99, x[0].lower()))
        for t, reps in out.items()
    }








# ------------------------- history persistence -------------------------


def _append_history(by_h: dict[str, list[dict]], generated_at: datetime) -> None:
    """Append one JSON line per ranked row to docs/history.jsonl.

    The file is small (~20 lines per run × 12 runs/day ≈ 240 lines/day,
    well under a MB per year) and is committed alongside REPORT.md so the
    history survives even if the GitHub Actions SQLite cache is evicted.
    """
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    iso = generated_at.replace(microsecond=0).isoformat()
    lines: list[str] = []
    for h, rows in by_h.items():
        for r in rows:
            lines.append(
                json.dumps(
                    {
                        "ts": iso,
                        "h": h,
                        "rank": r["rank"],
                        "ticker": r["ticker"],
                        "score": round(float(r.get("blended", r.get("blended_score") or 0)), 4),
                        "hc": int(r.get("horizon_count") or 1),
                    },
                    separators=(",", ":"),
                )
            )
    if lines:
        with HISTORY_PATH.open("a") as f:
            f.write("\n".join(lines) + "\n")


def _load_history(days: int) -> list[dict]:
    """Read recent history rows from docs/history.jsonl."""
    if not HISTORY_PATH.exists():
        return []
    cutoff = datetime.utcnow() - timedelta(days=days)
    out: list[dict] = []
    with HISTORY_PATH.open() as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw)
                ts = datetime.fromisoformat(rec["ts"])
            except (json.JSONDecodeError, KeyError, ValueError):
                continue
            if ts < cutoff:
                continue
            rec["_ts"] = ts
            out.append(rec)
    return out














# -------------------------- international picks --------------------------


_REGION_LABEL = {"IL": "🇮🇱 Israel", "EU": "🇪🇺 Europe"}


def _ticker_region_map() -> dict[str, str]:
    """{ticker: 'IL' | 'EU'} for every non-US name in the static universe.
    US-L / US-S tickers are omitted since this map only exists to flag
    international names in the report."""
    from invest.universe import static_universe_entries

    return {t: region for t, _name, _sector, region in static_universe_entries() if region in ("IL", "EU")}








# --------------------------- main table ---------------------------


_HORIZON_LETTER = {"hours": "H", "daily": "D", "weekly": "W", "monthly": "M"}


def main_table_rows(by_h: dict[str, list[dict]]) -> list[dict]:
    """Collapse the four per-horizon lists into ONE ranked table.

    A ticker's strength is how many horizons rank it and how well: we sum
    its per-horizon percentile so a name that only tops the 'hours' list
    can't outrank one that every horizon likes. Ties break on upside.
    Returns rows sorted best-first, capped to `settings.main_table_size`.

    Unioning four independently-diversified horizon lists produces however
    many DISTINCT tickers that union happens to contain, not a fixed
    number — observed 27 on one live run. The cap makes the row count
    predictable regardless of how much the four lists overlap.
    """
    agg: dict[str, dict] = {}
    for h in HORIZONS:
        for r in by_h.get(h, []):
            t = r["ticker"]
            row = agg.setdefault(
                t,
                {
                    "ticker": t,
                    "name": r.get("name") or "",
                    "sector": r.get("sector") or "",
                    "upside_pct": r.get("upside_pct"),
                    "last_close": r.get("last_close"),
                    "mean_target": r.get("mean_target"),
                    "analysts": r.get("analysts") or 0,
                    "horizons": [],
                    "score": 0.0,
                    "best_rank": 99,
                },
            )
            row["horizons"].append(h)
            row["score"] += float(r.get("percentile") or 0.0)
            row["best_rank"] = min(row["best_rank"], int(r.get("rank") or 99))

    rows = list(agg.values())
    tickers = [r["ticker"] for r in rows]
    sources = _total_sources_per_ticker(tickers)
    for r in rows:
        r["sources"] = sources.get(r["ticker"], 0)
    rows.sort(
        key=lambda r: (-(r["score"]), -(r.get("upside_pct") or 0.0), r["best_rank"])
    )
    rows = rows[: get_settings().main_table_size]
    for i, r in enumerate(rows, start=1):
        r["rank"] = i
    return rows


def _timeframe_marks(horizons: list[str]) -> str:
    """Compact H/D/W/M markers — replaces four near-duplicate tables."""
    present = {h for h in horizons}
    return "".join(
        _HORIZON_LETTER[h] if h in present else "·" for h in HORIZONS
    )


def _main_table_md(rows: list[dict]) -> str:
    if not rows:
        return "_(no picks cleared the quality gates this run)_\n"
    headers = [
        "#", "Ticker", "Name", "Sector", "Upside",
        "Price", "Target", "Score", "H/D/W/M", "Analysts", "Sources",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        upside = (
            f"**{(r.get('upside_pct') or 0) * 100:+.1f}%**"
            if r.get("upside_pct") is not None
            else "—"
        )
        price = f"{r['last_close']:.2f}" if r.get("last_close") else "—"
        target = f"{r['mean_target']:.2f}" if r.get("mean_target") else "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["rank"]),
                    f"**{r['ticker']}**",
                    (r["name"] or "")[:34],
                    (r["sector"] or "")[:20],
                    upside,
                    price,
                    target,
                    f"{r['score']:.2f}",
                    _timeframe_marks(r["horizons"]),
                    str(r["analysts"]),
                    str(r["sources"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _staleness_banner_md(as_of: date) -> str | None:
    """Loud warning when the newest scores are old.

    Without this the page happily presented a five-week-old ranking as if it
    were current, because the enrichment columns were recomputed live.
    """
    age = (date.today() - as_of).days
    if age <= get_settings().max_score_age_days:
        return None
    return (
        f"> ⚠️ **STALE DATA — these rankings are {age} days old** "
        f"(scored {as_of.isoformat()}). The crawler has not produced fresh "
        f"scores since then; treat everything below as out of date.\n"
    )


# ------------------------------ Markdown ------------------------------


def _build_markdown(as_of: date, n: int) -> str:
    """ONE ranked main table, Upside first. Nothing else.

    Previously this emitted four near-duplicate per-timeframe tables plus a
    wall of ~64 firm names, a per-pick firm table, a 14-day history matrix,
    sustained picks and a separate IL/EU section — burying the single number
    that actually drives a decision. Those are all gone: the four timeframes
    are collapsed into one H/D/W/M column, and international names now
    compete in the main table on merit.
    """
    by_h = _collect_top_by_horizon(as_of, n)
    # Persist this run's top-N into the history file (still used by the
    # HTML view and for auditing), before rendering.
    _append_history(by_h, datetime.utcnow())

    parts: list[str] = []
    banner = _staleness_banner_md(as_of)
    if banner:
        parts.append(banner)
        parts.append("")
    parts.append(_main_table_md(main_table_rows(by_h)))
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------- HTML ----------------------------------


def _html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )




def _main_table_html(rows: list[dict], by_h: dict[str, list[dict]]) -> str:
    """The single main table, Upside first, with a click-to-expand drawer
    per row showing that stock's recent named analyst actions."""
    if not rows:
        return "<p><em>(no picks cleared the quality gates this run)</em></p>"

    # Recent-actions payload lives on the per-horizon rows; index it once.
    actions_by_ticker: dict[str, list[dict]] = {}
    for h in HORIZONS:
        for r in by_h.get(h, []):
            actions_by_ticker.setdefault(r["ticker"], r.get("recent_actions") or [])

    from invest.firms import firm_tier

    head = (
        "<thead><tr>"
        "<th>#</th><th>Ticker</th><th>Name</th><th>Sector</th>"
        "<th title='Consensus price target vs current price.'>Upside</th>"
        "<th>Price</th><th>Target</th>"
        "<th title='Sum of per-timeframe percentiles — higher means more timeframes rank it highly.'>Score</th>"
        "<th title='Which timeframes rank this name: Hours / Daily / Weekly / Monthly.'>H/D/W/M</th>"
        "<th>Analysts</th>"
        "<th title='Distinct named contributors: sell-side firms, 13F filers, insider filers.'>Sources</th>"
        "</tr></thead>"
    )

    def _tier_cell(firm: str | None) -> str:
        t = firm_tier(firm)
        if t == 1:
            return "<td class='tier1'><strong>T1</strong></td>"
        if t == 2:
            return "<td class='tier2'>T2</td>"
        if t == 3:
            return "<td class='tier3'>T3</td>"
        return "<td class='src'>—</td>"

    body: list[str] = []
    for i, r in enumerate(rows):
        upside = (
            f"{(r.get('upside_pct') or 0) * 100:+.1f}%"
            if r.get("upside_pct") is not None
            else "—"
        )
        up_cls = "num up-pos" if (r.get("upside_pct") or 0) > 0 else "num"
        price = f"{r['last_close']:.2f}" if r.get("last_close") else "—"
        target = f"{r['mean_target']:.2f}" if r.get("mean_target") else "—"
        sector = r["sector"] or ""
        sector_html = (
            f"<span class='sector' style='background:{_sector_colour(sector)}'>"
            f"{_html_escape(sector[:22])}</span>"
            if sector
            else ""
        )
        actions = actions_by_ticker.get(r["ticker"], [])
        drawer_rows = "".join(
            "<tr>"
            f"<td>{a['date'].isoformat() if a.get('date') else ''}</td>"
            + _tier_cell(a.get("firm"))
            + f"<td>{_html_escape(a.get('firm') or '')}</td>"
            f"<td>{_html_escape((a.get('action') or '').title())}</td>"
            f"<td>{_html_escape((a.get('from') or '') + ' → ' + (a.get('to') or ''))}</td>"
            f"<td class='num'>{a.get('target') or ''}</td>"
            f"<td class='src'>{_html_escape(a.get('source') or '')}</td>"
            "</tr>"
            for a in actions
        )
        drawer = (
            f"<tr class='drawer' id='d-{r['ticker']}-{i}' style='display:none'>"
            "<td colspan='11'><strong>Recent analyst actions</strong>"
            "<table class='inner'><thead><tr><th>Date</th><th>Tier</th><th>Firm</th>"
            "<th>Action</th><th>From → To</th><th>Target</th><th>Source</th></tr></thead>"
            f"<tbody>{drawer_rows}</tbody></table></td></tr>"
            if drawer_rows
            else ""
        )
        toggle = (
            f" onclick=\"var d=document.getElementById('d-{r['ticker']}-{i}');"
            "if(d){d.style.display=d.style.display==='none'?'table-row':'none'}\""
            if drawer_rows
            else ""
        )
        body.append(
            f"<tr class='row-main'{toggle} style='cursor:pointer'>"
            f"<td>{r['rank']}</td>"
            f"<td><strong>{_html_escape(r['ticker'])}</strong></td>"
            f"<td>{_html_escape((r['name'] or '')[:40])}</td>"
            f"<td>{sector_html}</td>"
            f"<td class='{up_cls}'><strong>{upside}</strong></td>"
            f"<td class='num'>{price}</td>"
            f"<td class='num'>{target}</td>"
            f"<td class='num'>{r['score']:.2f}</td>"
            f"<td class='tf'>{_html_escape(_timeframe_marks(r['horizons']))}</td>"
            f"<td class='num'>{r['analysts']}</td>"
            f"<td class='num'>{r['sources']}</td>"
            "</tr>" + drawer
        )
    return f"<table class='top'>{head}<tbody>{''.join(body)}</tbody></table>"


def _heartbeat_badge() -> str:
    """Return an HTML badge that the client will keep updating from a
    machine-readable ISO timestamp. Server side we just emit the bones —
    the inline JS at the bottom of the page computes "N min ago" live on
    every render and re-colours the badge based on the current age.

    Without this, the badge would freeze at the value computed when
    REPORT.md was generated, so every reader saw "0 min ago" forever.
    """
    try:
        with session_scope() as s:
            row = (
                s.query(RunLog.finished_at)
                .filter(RunLog.status == "ok", RunLog.finished_at.isnot(None))
                .order_by(RunLog.finished_at.desc())
                .first()
            )
    except Exception:
        row = None
    if not row or not row[0]:
        return (
            "<span class='badge red' title='No successful run recorded yet'>"
            "no runs yet</span>"
        )
    finished = row[0]
    iso = finished.isoformat(timespec="seconds") + "Z"
    title = f"Last successful pipeline run at {iso}"
    # Initial classes — JS will overwrite them on load.
    return (
        f"<span class='badge live-ago amber' data-iso='{iso}' title='{title}'>"
        f"last crawl: <span class='ago'>—</span></span>"
    )


# Repo/workflow this report is generated for — used by the "Refresh now"
# button. Triggering workflow_dispatch needs an authenticated GitHub API
# call; a public static page can never ship that credential itself (anyone
# viewing the page could steal and abuse it — spam-trigger runs, or worse
# if the token's scope is broader than intended). Instead the button's
# inline JS asks whoever CLICKS it to paste their own GitHub personal
# access token once, keeps it only in that browser's localStorage, and
# calls the GitHub API directly from the browser. No secret ever ships in
# the page; a visitor with no token literally cannot trigger anything.
#
# NOTE: `_DEPLOY_REF` must match whichever branch's copy of the workflow
# should run — update it if the deploy branch ever changes.
_REPO_OWNER = "uriiger-sketch"
_REPO_NAME = "Invest"
_WORKFLOW_FILE = "crawl.yml"
_DEPLOY_REF = "claude/stock-crawler-planning-WaaeO"
_REPO_ACTIONS_URL = f"https://github.com/{_REPO_OWNER}/{_REPO_NAME}/actions/workflows/{_WORKFLOW_FILE}"


def _build_html(as_of: date, n: int) -> str:
    now = datetime.utcnow()
    generated = now.strftime("%Y-%m-%d %H:%M UTC")
    generated_iso = now.replace(microsecond=0).isoformat() + "Z"
    heartbeat = _heartbeat_badge()
    by_h = _collect_top_by_horizon(as_of, n)
    rows = main_table_rows(by_h)
    sections: list[str] = []
    banner = _staleness_banner_md(as_of)
    if banner:
        age = (date.today() - as_of).days
        sections.append(
            "<section><p class='stale-banner'>⚠️ <strong>STALE DATA — these "
            f"rankings are {age} days old</strong> (scored {as_of.isoformat()}). "
            "The crawler has not produced fresh scores since then.</p></section>"
        )
    sections.append(
        "<section><h2>Top picks</h2>"
        "<p class='blurb'>One ranked table across all four timeframes. "
        "Upside is the consensus price target vs the current price; H/D/W/M "
        "shows which timeframes rank the name. Click a row for that stock's "
        "recent analyst actions.</p>"
        f"{_main_table_html(rows, by_h)}</section>"
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Invest — Top {len(rows)}</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="favicon.svg">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="120">
<style>
  :root {{ color-scheme: light dark; --accent: #2b6cb0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
         max-width: 1280px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
  h1 {{ margin-bottom: 0.25rem; }}
  h2 {{ border-bottom: 1px solid rgba(127,127,127,0.25); padding-bottom: 0.25rem; margin-top: 2.5rem; }}
  .meta {{ color: #666; font-size: 0.9rem; }}
  .blurb {{ color: #555; font-style: italic; margin-top: 0.25rem; }}
  blockquote {{ border-left: 3px solid var(--accent); margin: 1rem 0; padding: 0.5rem 1rem; color: #444; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.92rem; margin-top: 0.5rem; }}
  th, td {{ padding: 0.45rem 0.55rem; border-bottom: 1px solid rgba(127,127,127,0.18);
            text-align: left; vertical-align: top; }}
  th {{ background: rgba(127,127,127,0.08); font-weight: 600; }}
  td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  td.ok {{ color: #28823a; }}
  td.err {{ color: #b00; }}
  tr.drawer td {{ background: rgba(43,108,176,0.04); padding: 0.6rem 0.8rem; }}
  table.inner {{ margin-top: 0.4rem; font-size: 0.85rem; }}
  table.inner th {{ background: transparent; }}
  .src {{ color: #777; font-size: 0.8rem; }}
  .sector {{ display: inline-block; padding: 0.1rem 0.45rem; border-radius: 4px; color: #fff; font-size: 0.8rem; }}
  dl.columns {{ display: grid; grid-template-columns: max-content 1fr; gap: 0.25rem 1rem; margin: 0.5rem 0; }}
  dl.columns dt {{ font-weight: 600; color: var(--accent); }}
  dl.columns dd {{ margin: 0; color: #444; }}
  tr.err td {{ color: #b00; }}
  details > summary {{ cursor: pointer; font-weight: 600; }}
  .badge {{ display: inline-block; padding: 0.15rem 0.5rem; border-radius: 4px;
            font-size: 0.82rem; font-weight: 600; color: #fff; margin-left: 0.5rem; }}
  .badge.green {{ background: #2f855a; }}
  .badge.amber {{ background: #b7791f; }}
  .badge.red   {{ background: #c53030; }}
  td.star {{ color: #d69e2e; font-weight: 700; text-align: center; }}
  tr.row-main.star {{ background: rgba(214,158,46,0.08); }}
  tr.row-main.star:hover {{ background: rgba(214,158,46,0.16); }}
  .starred {{ background: rgba(214,158,46,0.1); border-left: 3px solid #d69e2e;
              padding: 0.6rem 1rem; margin: 1rem 0; border-radius: 4px; }}
  .starred.muted {{ background: rgba(127,127,127,0.08); border-left-color: #aaa; color: #666; }}
  td.tier1 {{ color: #2f5fa7; }}
  td.tier2 {{ color: #6b6b6b; }}
  td.tier3 {{ color: #999; }}
  table.snapshot {{ margin-top: 0.5rem; }}
  td.up-pos {{ color: #1e7e45; font-weight: 700; }}
  td.tf {{ font-family: ui-monospace, SFMono-Regular, Menlo, monospace; letter-spacing: 1px; }}
  .stale-banner {{ background: #fff4e5; border-left: 4px solid #d97706;
                   padding: 0.75rem 1rem; border-radius: 4px; color: #7c2d12; }}
  ul.intl-picks {{ margin: 0.5rem 0 0 0; padding-left: 1.2rem; line-height: 1.7; }}
  .refresh-btn {{ display: inline-block; margin-left: 0.6rem; padding: 0.2rem 0.7rem;
                   border-radius: 5px; background: var(--accent); color: #fff;
                   border: none; cursor: pointer; font-size: 0.85rem; font-weight: 600;
                   vertical-align: middle; font-family: inherit; }}
  .refresh-btn:hover {{ opacity: 0.85; }}
  .refresh-btn:disabled {{ opacity: 0.6; cursor: default; }}
  .refresh-status {{ margin-left: 0.6rem; font-size: 0.85rem; vertical-align: middle; }}
  .refresh-fallback {{ font-size: 0.78rem; margin-left: 0.4rem; }}
</style>
</head>
<body>
<h1>Invest — Top {len(rows)} {heartbeat}
<button type="button" class="refresh-btn" id="refresh-btn"
        title="Triggers an immediate crawl. Asks for a GitHub token the first click; stored only in this browser.">
  🔄 Refresh now
</button>
<span class="refresh-status" id="refresh-status"></span>
<a class="refresh-fallback" href="{_REPO_ACTIONS_URL}" target="_blank" rel="noopener"
   title="No GitHub token handy? Trigger it manually from the Actions page instead.">(or open Actions manually)</a></h1>
<p class="meta">Generated: <span class="live-ago" data-iso="{generated_iso}" title="{generated}">
<span class="ago">just now</span></span> · Scores as of: <strong>{as_of.isoformat()}</strong>
 · page auto-refreshes every 2 min · pipeline runs every 30 min via GitHub Actions.</p>

{"".join(sections)}

<script>
(function () {{
  function fmt(mins) {{
    if (mins < 1) return "just now";
    if (mins < 60) return mins + " min ago";
    var h = Math.floor(mins / 60), m = mins % 60;
    if (h < 24) return h + " h " + m + " min ago";
    var d = Math.floor(h / 24);
    return d + " d " + (h % 24) + " h ago";
  }}
  function refresh() {{
    var now = Date.now();
    var nodes = document.querySelectorAll(".live-ago");
    for (var i = 0; i < nodes.length; i++) {{
      var el = nodes[i];
      var iso = el.getAttribute("data-iso");
      if (!iso) continue;
      var ts = Date.parse(iso);
      if (isNaN(ts)) continue;
      var mins = Math.max(0, Math.floor((now - ts) / 60000));
      var target = el.querySelector(".ago") || el;
      target.textContent = fmt(mins);
      if (el.classList.contains("badge")) {{
        el.classList.remove("green", "amber", "red");
        el.classList.add(mins < 30 ? "green" : mins < 120 ? "amber" : "red");
      }}
    }}
  }}
  refresh();
  setInterval(refresh, 60000);
}})();
</script>
<script>
(function () {{
  // Triggers workflow_dispatch directly from the browser. No token is ever
  // shipped in this page — the FIRST click prompts whoever is clicking to
  // paste their own GitHub personal access token, which is then kept only
  // in this browser's localStorage and sent straight to GitHub's API, never
  // anywhere else. A visitor with no token of their own literally cannot
  // trigger anything; this is not a "public button", it's a "remember my
  // own credential locally" convenience for whoever legitimately can.
  var OWNER = {_REPO_OWNER!r}, REPO = {_REPO_NAME!r}, WORKFLOW = {_WORKFLOW_FILE!r}, REF = {_DEPLOY_REF!r};
  var TOKEN_KEY = "invest_gh_token";
  var btn = document.getElementById("refresh-btn");
  var status = document.getElementById("refresh-status");
  if (!btn || !status) return;

  function setStatus(msg, color) {{
    status.textContent = msg;
    status.style.color = color;
  }}

  function trigger(token) {{
    btn.disabled = true;
    setStatus("Triggering…", "#666");
    fetch(
      "https://api.github.com/repos/" + OWNER + "/" + REPO + "/actions/workflows/" + WORKFLOW + "/dispatches",
      {{
        method: "POST",
        headers: {{
          "Authorization": "Bearer " + token,
          "Accept": "application/vnd.github+json",
          "Content-Type": "application/json"
        }},
        body: JSON.stringify({{ ref: REF }})
      }}
    ).then(function (r) {{
      btn.disabled = false;
      if (r.status === 204) {{
        setStatus("✓ Crawl triggered — takes a few minutes; this page will pick it up on its next refresh.", "#2f855a");
      }} else if (r.status === 401 || r.status === 403) {{
        localStorage.removeItem(TOKEN_KEY);
        setStatus("✗ Token rejected (expired / wrong scope) — click again to re-enter it.", "#c53030");
      }} else {{
        r.text().then(function (t) {{
          setStatus("✗ GitHub returned " + r.status + ": " + t.slice(0, 150), "#c53030");
        }});
      }}
    }}).catch(function (e) {{
      btn.disabled = false;
      setStatus("✗ Request failed: " + e.message, "#c53030");
    }});
  }}

  btn.addEventListener("click", function () {{
    var token = localStorage.getItem(TOKEN_KEY);
    if (!token) {{
      token = window.prompt(
        "Paste a GitHub personal access token to trigger a crawl.\\n\\n" +
        "Create one at github.com/settings/personal-access-tokens — a " +
        "fine-grained token scoped ONLY to the " + REPO + " repo with " +
        "'Actions: Read and write' permission is the safest choice.\\n\\n" +
        "Stored only in THIS browser (localStorage) — never sent anywhere " +
        "except directly to api.github.com."
      );
      if (!token) return;
      token = token.trim();
      if (!token) return;
      localStorage.setItem(TOKEN_KEY, token);
    }}
    trigger(token);
  }});
}})();
</script>
</body>
</html>
"""


def _placeholder() -> tuple[str, str]:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    md = "_(awaiting first crawl)_\n"
    _ = generated  # used only in the HTML placeholder below
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Invest — awaiting first crawl</title>
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta http-equiv="refresh" content="60"></head>
<body style="font-family: -apple-system, Helvetica, sans-serif; max-width: 800px; margin: 3rem auto;">
<h1>Invest — awaiting first crawl
<a href="{_REPO_ACTIONS_URL}" target="_blank" rel="noopener"
   style="margin-left:0.6rem; padding:0.2rem 0.7rem; border-radius:5px; background:#2b6cb0;
          color:#fff; text-decoration:none; font-size:0.85rem; font-weight:600; vertical-align:middle;">
  🔄 Refresh now
</a></h1>
<p>Generated: <strong>{generated}</strong>. The pipeline has not yet produced any scores.
The GitHub Actions workflow runs every 30 minutes — refresh this page later, or click
"Refresh now" above to trigger it immediately (requires GitHub login with repo access).</p>
</body></html>
"""
    return md, html


def main() -> None:
    settings = get_settings()
    REPORT_HTML.parent.mkdir(parents=True, exist_ok=True)
    as_of = _latest_as_of()
    if as_of is None:
        md, html = _placeholder()
        REPORT_MD.write_text(md)
        REPORT_HTML.write_text(html)
        print("no scores yet; wrote placeholder")
        return

    REPORT_MD.write_text(_build_markdown(as_of, settings.top_n))
    REPORT_HTML.write_text(_build_html(as_of, settings.top_n))
    print(f"wrote {REPORT_MD} and {REPORT_HTML}")


if __name__ == "__main__":
    main()
