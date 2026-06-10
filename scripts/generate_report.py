"""Render top-20 per horizon to REPORT.md and docs/index.html.

Reads the latest persisted scores from SQLite and writes a human-readable
report that GitHub can render directly, plus a self-contained HTML page
that GitHub Pages serves without needing any runtime fetch.
"""
from __future__ import annotations

import hashlib
import json
from collections import defaultdict
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
        "Which of {hours, daily, weekly, monthly} top-8 lists the ticker "
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
    with session_scope() as s:
        rows = (
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
            .limit(n)
            .all()
        )
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
        # Last close per ticker.
        for t in tickers:
            row = (
                s.query(Price.close, Price.date)
                .filter(Price.ticker == t)
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


def _recent_runs(limit: int = 20) -> list[dict]:
    with session_scope() as s:
        rows = (
            s.query(RunLog)
            .order_by(RunLog.started_at.desc())
            .limit(limit)
            .all()
        )
    return [
        {
            "job": r.job,
            "status": r.status,
            "rows": r.rows_written,
            "started": r.started_at,
            "finished": r.finished_at,
            "error": (r.error or "")[:120],
        }
        for r in rows
    ]


def _recent_runs_safe(limit: int = 20) -> list[dict]:
    try:
        return _recent_runs(limit)
    except Exception:
        return []


# ------------------------------- Markdown --------------------------------


def _md_table(rows: list[dict]) -> str:
    """Horizon table: horizon-specific score columns + Upside (the single
    most relevant stock-level fact). Buy/Hold/Sell/Analysts/Insts stay in
    the Stock coverage snapshot section to avoid four-way duplication."""
    if not rows:
        return "_(no data)_\n"
    headers = [
        "#", "★", "Ticker", "Name", "Sector",
        "Blended", "Composite", "ML", "Pctile", "Upside",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        pct = f"{(r['percentile'] or 0) * 100:.1f}%"
        upside = (
            f"{(r.get('upside_pct') or 0) * 100:+.1f}%"
            if r.get("upside_pct") is not None
            else "—"
        )
        hc = r.get("horizon_count") or 1
        stars = "★" * hc if hc >= 2 else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["rank"]),
                    stars,
                    f"**{r['ticker']}**",
                    (r["name"] or "")[:40],
                    (r["sector"] or "")[:20],
                    f"{r['blended']:.3f}",
                    f"{r['composite']:.3f}",
                    f"{r['ml']:.3f}",
                    pct,
                    upside,
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _runs_md_table(rows: list[dict]) -> str:
    if not rows:
        return "_(no runs logged)_\n"
    lines = [
        "| Job | Status | Rows | Started | Error |",
        "|---|---|---:|---|---|",
    ]
    for r in rows:
        started = r["started"].strftime("%Y-%m-%d %H:%M:%SZ") if r["started"] else ""
        err = (r["error"] or "").replace("|", "\\|")
        lines.append(
            f"| {r['job']} | {r['status']} | {r['rows']} | {started} | {err} |"
        )
    return "\n".join(lines) + "\n"


def _columns_md() -> str:
    lines = ["| Column | What it means |", "|---|---|"]
    for name, doc in COLUMN_DOCS:
        lines.append(f"| **{name}** | {doc} |")
    return "\n".join(lines) + "\n"


def _heartbeat_md() -> str:
    """Plain-text version of the freshness badge for Markdown output."""
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
        return "⚪ no crawl run recorded"
    finished = row[0]
    mins = int((datetime.utcnow() - finished).total_seconds() / 60)
    icon = "🟢" if mins < 30 else "🟡" if mins < 120 else "🔴"
    label = f"{mins} min ago" if mins < 120 else f"{mins / 60:.1f} h ago"
    return f"{icon} last successful crawl: {label} (at {finished.isoformat(timespec='seconds')}Z)"


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


def _tier1_count_per_ticker(tickers: list[str], lookback_days: int = 90) -> dict[str, int]:
    """Distinct tier-1 firms with an action on the ticker in the lookback window."""
    if not tickers:
        return {}
    from invest.firms import firm_tier

    cutoff = date.today() - timedelta(days=lookback_days)
    out: dict[str, int] = dict.fromkeys(tickers, 0)
    with session_scope() as s:
        rows = s.execute(
            select(AnalystAction.ticker, AnalystAction.firm)
            .where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
            .distinct()
        ).all()
    for t, firm in rows:
        if firm_tier(firm) == 1:
            out[t] = out.get(t, 0) + 1
    return out


def _total_sources_per_ticker(tickers: list[str]) -> dict[str, int]:
    """Distinct named contributors per ticker: sell-side firms (last 90 d) ∪
    tracked 13F filers (latest quarter) ∪ insider filers (last 90 d).

    Read directly from the same tables `features.py` uses so the snapshot
    column and the `min_total_sources` gate stay in sync."""
    if not tickers:
        return {}
    from invest.models import Holding13F, InsiderTrade

    cutoff = date.today() - timedelta(days=90)
    out: dict[str, set[tuple[str, str]]] = {}
    with session_scope() as s:
        for t, firm in s.execute(
            select(AnalystAction.ticker, AnalystAction.firm).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
        ).all():
            out.setdefault(t, set()).add(("firm", firm.lower().strip()))
        for t, cik in s.execute(
            select(Holding13F.ticker, Holding13F.filer_cik).where(
                Holding13F.ticker.in_(tickers),
                Holding13F.filer_cik.isnot(None),
            )
        ).all():
            out.setdefault(t, set()).add(("13f", cik))
        for t, ifiler in s.execute(
            select(InsiderTrade.ticker, InsiderTrade.filer).where(
                InsiderTrade.ticker.in_(tickers),
                InsiderTrade.date >= cutoff,
                InsiderTrade.filer.isnot(None),
            )
        ).all():
            out.setdefault(t, set()).add(("insider", ifiler.lower().strip()))
    return {t: len(s_) for t, s_ in out.items()}


def _recognised_firms_count() -> int:
    """Total distinct firm aliases we recognise in the tier map. Used in the
    report header to prove the system isn't just rebadging one feed."""
    from invest.firms import TIER_1, TIER_2, TIER_3

    return len(TIER_1) + len(TIER_2) + len(TIER_3)


def _firms_seen_in_window(lookback_days: int = 90) -> dict[int, list[str]]:
    """Distinct named firms seen across ALL tickers in the window, grouped
    by tier. Proves how many real firms actually contributed signal."""
    from invest.firms import firm_tier

    cutoff = date.today() - timedelta(days=lookback_days)
    seen: set[str] = set()
    with session_scope() as s:
        for (firm,) in s.execute(
            select(AnalystAction.firm)
            .where(AnalystAction.date >= cutoff, AnalystAction.firm.isnot(None))
            .distinct()
        ).all():
            if firm:
                seen.add(firm)
    by_tier: dict[int, list[str]] = {1: [], 2: [], 3: [], 0: []}
    for firm in sorted(seen, key=str.lower):
        by_tier[firm_tier(firm)].append(firm)
    return by_tier


def _named_firms_for_tickers(tickers: list[str], lookback_days: int = 90) -> dict[str, list[tuple[str, int]]]:
    """For each ticker, return the distinct named sell-side firms seen in
    the last `lookback_days` along with each firm's tier (0..3). Sorted
    by tier ASC (tier-1 first) then by firm name."""
    if not tickers:
        return {}
    from invest.firms import firm_tier

    cutoff = date.today() - timedelta(days=lookback_days)
    out: dict[str, set[str]] = {}
    with session_scope() as s:
        for t, firm in s.execute(
            select(AnalystAction.ticker, AnalystAction.firm).where(
                AnalystAction.ticker.in_(tickers),
                AnalystAction.date >= cutoff,
                AnalystAction.firm.isnot(None),
            )
        ).all():
            out.setdefault(t, set()).add(firm)
    return {
        t: sorted(((f, firm_tier(f)) for f in firms), key=lambda x: (x[1] or 99, x[0].lower()))
        for t, firms in out.items()
    }


def _coverage_snapshot_rows(by_h: dict[str, list[dict]]) -> list[dict]:
    """One row per unique ticker that appears in any horizon's top list."""
    seen: dict[str, dict] = {}
    for h in HORIZONS:
        for r in by_h.get(h, []):
            t = r["ticker"]
            if t not in seen:
                seen[t] = {
                    "ticker": t,
                    "name": r.get("name") or "",
                    "sector": r.get("sector") or "",
                    "upside_pct": r.get("upside_pct"),
                    "buy": r.get("buy") or 0,
                    "hold": r.get("hold") or 0,
                    "sell": r.get("sell") or 0,
                    "analysts": r.get("analysts") or 0,
                    "inst_count": r.get("inst_count") or 0,
                    "horizons": r.get("horizons") or [],
                }
    tier1 = _tier1_count_per_ticker(list(seen.keys()))
    total_sources = _total_sources_per_ticker(list(seen.keys()))
    named_firms = _named_firms_for_tickers(list(seen.keys()))
    for t, row in seen.items():
        row["tier1_firms"] = tier1.get(t, 0)
        row["total_sources"] = total_sources.get(t, 0)
        row["named_firms"] = named_firms.get(t, [])
    rows = list(seen.values())
    rows.sort(key=lambda r: (-(r.get("total_sources") or 0), -(r.get("upside_pct") or 0)))
    return rows


def _coverage_snapshot_md(rows: list[dict]) -> str:
    if not rows:
        return "_(no tickers passed the quality gate this run)_\n"
    headers = [
        "Ticker", "Sector", "Upside", "Buy", "Hold", "Sell",
        "Analysts", "Tier-1 firms", "Insts", "Sources", "Horizons",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        upside = (
            f"{(r.get('upside_pct') or 0) * 100:+.1f}%"
            if r.get("upside_pct") is not None
            else "—"
        )
        lines.append(
            "| "
            + " | ".join(
                [
                    f"**{r['ticker']}**",
                    (r["sector"] or "")[:24],
                    upside,
                    str(r["buy"]),
                    str(r["hold"]),
                    str(r["sell"]),
                    str(r["analysts"]),
                    str(r["tier1_firms"]),
                    str(r["inst_count"]),
                    str(r.get("total_sources") or 0),
                    ", ".join(r["horizons"]) or "—",
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _coverage_snapshot_html(rows: list[dict]) -> str:
    if not rows:
        return "<p><em>(no tickers passed the quality gate this run)</em></p>"
    head = (
        "<thead><tr>"
        "<th>Ticker</th><th>Sector</th>"
        "<th title='Consensus mean target / last close − 1.'>Upside</th>"
        "<th>Buy</th><th>Hold</th><th>Sell</th>"
        "<th title='Total firms covering. Equals Buy + Hold + Sell.'>Analysts</th>"
        "<th title='Distinct tier-1 firms (Goldman, MS, JPM, BofA, …) with an action in the last 90 d.'>Tier-1</th>"
        "<th title='Tracked 13F filers holding the stock.'>Insts</th>"
        "<th title='Distinct named contributors: sell-side firms (90 d) "
        "+ tracked 13F filers (latest quarter) + insider filers (90 d). "
        "Floor = 50.'>Sources</th>"
        "<th>Horizons</th>"
        "</tr></thead>"
    )
    body_rows = []
    for r in rows:
        upside = (
            f"{(r.get('upside_pct') or 0) * 100:+.1f}%"
            if r.get("upside_pct") is not None
            else "—"
        )
        sector = r["sector"] or ""
        sector_html = (
            f"<span class='sector' style='background:{_sector_colour(sector)}'>"
            f"{_html_escape(sector[:24])}</span>"
            if sector
            else ""
        )
        body_rows.append(
            "<tr>"
            f"<td><strong>{_html_escape(r['ticker'])}</strong></td>"
            f"<td>{sector_html}</td>"
            f"<td class='num'>{upside}</td>"
            f"<td class='num ok'>{r['buy']}</td>"
            f"<td class='num'>{r['hold']}</td>"
            f"<td class='num err'>{r['sell']}</td>"
            f"<td class='num'>{r['analysts']}</td>"
            f"<td class='num'>{r['tier1_firms']}</td>"
            f"<td class='num'>{r['inst_count']}</td>"
            f"<td class='num'><strong>{r.get('total_sources') or 0}</strong></td>"
            f"<td>{', '.join(r['horizons']) or '—'}</td>"
            "</tr>"
        )
    return f"<table class='snapshot'>{head}<tbody>{''.join(body_rows)}</tbody></table>"


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


def _sustained_picks(history: list[dict]) -> list[dict]:
    """Top 3 names that appeared on ≥60 % of runs in the last `sustained_days`
    AND carried ≥2 stars (horizon_count ≥ 2) on at least half of those
    appearances. Ranked by mean blended_score."""
    settings = get_settings()
    if not history:
        return []
    # Distinct run timestamps in the window.
    run_ts = sorted({r["_ts"] for r in history})
    if len(run_ts) < 2:
        return []
    n_runs = len(run_ts)

    # Aggregate per ticker (collapse across horizons — best blended_score per run).
    per_ticker: dict[str, list[dict]] = defaultdict(list)
    for r in history:
        per_ticker[r["ticker"]].append(r)

    candidates: list[dict] = []
    for ticker, rows in per_ticker.items():
        present_runs = {r["_ts"] for r in rows}
        appearances = len(present_runs)
        if appearances / n_runs < settings.sustained_min_runs_pct:
            continue
        starred_runs = sum(1 for r in rows if int(r.get("hc") or 1) >= settings.sustained_min_stars)
        if starred_runs / max(1, len(rows)) < 0.5:
            continue
        mean_score = sum(float(r.get("score") or 0) for r in rows) / len(rows)
        max_stars = max(int(r.get("hc") or 1) for r in rows)
        # The horizons on which it actually appeared.
        horizons = sorted({r["h"] for r in rows})
        candidates.append(
            {
                "ticker": ticker,
                "mean_score": mean_score,
                "appearances": appearances,
                "n_runs": n_runs,
                "max_stars": max_stars,
                "horizons": horizons,
            }
        )
    candidates.sort(key=lambda c: c["mean_score"], reverse=True)
    return candidates[:3]


def _history_top3_by_date(history: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """Group last-N days' history into {date_iso: {horizon: [{rank, ticker, score}]}},
    keeping only the most recent run per date / horizon and only ranks 1-3."""
    by_date: dict[str, dict[str, dict[int, dict]]] = defaultdict(lambda: defaultdict(dict))
    # Iterate newest-first; first hit wins (most recent run of the day).
    for r in sorted(history, key=lambda x: x["_ts"], reverse=True):
        if r["rank"] > 3:
            continue
        d = r["_ts"].date().isoformat()
        slot = by_date[d][r["h"]]
        if r["rank"] not in slot:
            slot[r["rank"]] = r
    # Flatten back to lists.
    out: dict[str, dict[str, list[dict]]] = {}
    for d, by_h in by_date.items():
        out[d] = {
            h: [v for _, v in sorted(rows.items())]  # rank 1, 2, 3
            for h, rows in by_h.items()
        }
    return dict(sorted(out.items(), reverse=True))


def _sustained_md(picks: list[dict]) -> str:
    if not picks:
        return "_(no sustained picks yet — needs at least a week of history)_\n"
    settings = get_settings()
    lines = [
        f"| Ticker | Avg blended score | Appearances | Max stars | Horizons | Of {settings.sustained_days} d |",
        "|---|---:|---:|---:|---|---:|",
    ]
    for p in picks:
        hz = ", ".join(p["horizons"])
        lines.append(
            f"| **{p['ticker']}** | {p['mean_score']:.3f} | "
            f"{p['appearances']} | {'★' * p['max_stars']} | {hz} | {p['n_runs']} runs |"
        )
    return "\n".join(lines) + "\n"


def _named_firms_md(snapshot_rows: list[dict]) -> str:
    """A per-ticker list of every named firm with a rating action in the
    last 90 d. Lets you scan UBS / B.Riley / Scotiabank / etc. directly."""
    if not snapshot_rows:
        return "_(no tickers passed the gate)_\n"
    lines = ["| Ticker | Tier-1 firms | Tier-2 firms | Other firms |", "|---|---|---|---|"]
    for r in snapshot_rows:
        firms = r.get("named_firms") or []
        t1 = [f for f, tier in firms if tier == 1]
        t2 = [f for f, tier in firms if tier == 2]
        other = [f for f, tier in firms if tier not in (1, 2)]
        lines.append(
            f"| **{r['ticker']}** "
            f"| {', '.join(t1) or '—'} "
            f"| {', '.join(t2) or '—'} "
            f"| {', '.join(other) or '—'} |"
        )
    return "\n".join(lines) + "\n"


def _all_firms_seen_md(by_tier: dict[int, list[str]]) -> str:
    """Flat list of every distinct firm we've seen in the last 90 d, grouped
    by tier. Stops the 'only Yahoo' misconception cold — these are the
    actual sell-side firms whose calls drive the score."""
    t1, t2, t3, unknown = by_tier.get(1, []), by_tier.get(2, []), by_tier.get(3, []), by_tier.get(0, [])
    total = len(t1) + len(t2) + len(t3) + len(unknown)
    if not total:
        return "_(no analyst actions in the last 90 days yet — first deep crawl will populate this)_\n"
    parts: list[str] = [f"_Total: **{total}** distinct firms with a rating action in the last 90 d._", ""]
    if t1:
        parts.append(f"**Tier-1 ({len(t1)}):** " + ", ".join(t1))
        parts.append("")
    if t2:
        parts.append(f"**Tier-2 ({len(t2)}):** " + ", ".join(t2))
        parts.append("")
    if t3:
        parts.append(f"**Tier-3 ({len(t3)}):** " + ", ".join(t3))
        parts.append("")
    if unknown:
        parts.append(f"_Unclassified ({len(unknown)}):_ " + ", ".join(unknown))
    return "\n".join(parts) + "\n"


def _history_md(by_date: dict[str, dict[str, list[dict]]]) -> str:
    if not by_date:
        return "_(no historical reports stored yet)_\n"
    horizon_short = {"hours": "Hours", "daily": "Daily", "weekly": "Weekly", "monthly": "Monthly"}
    lines = [
        "| Date | " + " | ".join(horizon_short.get(h, h) for h in HORIZONS) + " |",
        "|---|" + "|".join(["---"] * len(HORIZONS)) + "|",
    ]
    for d, by_h in by_date.items():
        cells = []
        for h in HORIZONS:
            picks = by_h.get(h, [])
            if not picks:
                cells.append("—")
            else:
                cells.append(", ".join(f"**{p['ticker']}**" for p in picks))
        lines.append(f"| {d} | " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


# ------------------------------ Markdown ------------------------------


def _build_markdown(as_of: date, n: int) -> str:
    """Concise Markdown: four top-N tables, plus two small history sections
    at the bottom (sustained picks + per-date top-3).

    Per-row star indicators (★★ to ★★★★) flag tickers that appear in more
    than one horizon's top list. The HTML page carries the rich version
    (heartbeat, disclaimer, how-to-read, recent runs); this Markdown view
    stays minimal so it scans in two seconds.
    """
    settings = get_settings()
    by_h = _collect_top_by_horizon(as_of, n)
    # Persist this run's top-N into the history file BEFORE reading it back so
    # the sustained-picks calculation sees the current snapshot too.
    _append_history(by_h, datetime.utcnow())

    parts: list[str] = []
    for h in HORIZONS:
        parts.append(f"## {HORIZON_TITLE.get(h, h)} — top {n}")
        parts.append("")
        parts.append(_md_table(by_h[h]))
        parts.append("")

    # --- Stock coverage snapshot (one row per unique top ticker) ---
    snapshot_rows = _coverage_snapshot_rows(by_h)
    parts.append("## Stock coverage snapshot")
    parts.append("")
    parts.append(
        "_One row per unique ticker that appears in any top list. Same "
        "stock-level facts every horizon would otherwise show — listed once, "
        "sorted by upside._"
    )
    parts.append("")
    parts.append(_coverage_snapshot_md(snapshot_rows))
    parts.append("")

    # --- Named analyst firms backing each pick ---
    parts.append("## Named analyst firms behind each pick (last 90 d)")
    parts.append("")
    parts.append(_named_firms_md(snapshot_rows))
    parts.append("")

    # --- All distinct firms seen across the universe (last 90 d) ---
    parts.append(
        f"## All sell-side firms seen across the universe "
        f"(last 90 d, {_recognised_firms_count()} aliases recognised)"
    )
    parts.append("")
    parts.append(_all_firms_seen_md(_firms_seen_in_window()))
    parts.append("")

    # --- Sustained picks (≥1 week on the list, ≥2 stars mostly) ---
    history_sustained = _load_history(settings.sustained_days)
    parts.append(f"## Sustained picks — top 3 over the last {settings.sustained_days} d")
    parts.append("")
    parts.append(
        "_Tickers that have been on a top list for ≥"
        f"{int(settings.sustained_min_runs_pct * 100)} % of runs in the window "
        f"and carried ≥{settings.sustained_min_stars} stars on a majority of those._"
    )
    parts.append("")
    parts.append(_sustained_md(_sustained_picks(history_sustained)))
    parts.append("")

    # --- Per-date top-3 by horizon (last `history_show_days` days) ---
    history_show = _load_history(settings.history_show_days)
    parts.append(f"## Top 3 by date — last {settings.history_show_days} d")
    parts.append("")
    parts.append(_history_md(_history_top3_by_date(history_show)))
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------- HTML ----------------------------------


def _html_escape(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _html_top_table(rows: list[dict]) -> str:
    if not rows:
        return "<p><em>(no data)</em></p>"
    head = (
        "<thead><tr>"
        "<th>#</th>"
        "<th title='Cross-horizon highlight. ★★ = two horizons; ★★★ = three; ★★★★ = all four.'>★</th>"
        "<th>Ticker</th><th>Name</th><th>Sector</th>"
        "<th title='Final score, z-scored across the universe.'>Blended</th>"
        "<th title='Rule-based score from nine weighted features.'>Composite</th>"
        "<th title='LightGBM predicted forward return (cold-start = composite).'>ML</th>"
        "<th title='Percentile of blended score in this horizon.'>Pctile</th>"
        "<th title='Consensus mean target / last close − 1. Floor = +4 %.'>Upside</th>"
        "</tr></thead>"
    )
    from invest.firms import firm_tier  # local import to keep top-level imports tidy
    body_rows = []
    for i, r in enumerate(rows):
        pct = f"{(r['percentile'] or 0) * 100:.1f}%"
        upside = (
            f"{(r.get('upside_pct') or 0) * 100:+.1f}%"
            if r.get("upside_pct") is not None
            else "—"
        )
        sector = r["sector"] or ""
        sector_html = (
            f"<span class='sector' style='background:{_sector_colour(sector)}'>"
            f"{_html_escape(sector[:22])}</span>"
            if sector
            else ""
        )
        # Analyst firms drawer (now with a Tier column).
        actions = r.get("recent_actions", [])

        def _tier_cell(firm: str | None) -> str:
            t = firm_tier(firm)
            if t == 1:
                return "<td class='tier1'><strong>T1</strong></td>"
            if t == 2:
                return "<td class='tier2'>T2</td>"
            if t == 3:
                return "<td class='tier3'>T3</td>"
            return "<td class='src'>—</td>"

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
        drawer_html = (
            f"<tr class='drawer' id='drawer-{r['ticker']}-{i}' style='display:none'>"
            "<td colspan='10'>"
            "<strong>Recent analyst actions</strong>"
            "<table class='inner'><thead><tr><th>Date</th><th>Tier</th><th>Firm</th>"
            "<th>Action</th><th>From → To</th><th>Target</th><th>Source</th></tr></thead>"
            f"<tbody>{drawer_rows}</tbody></table>"
            "</td></tr>"
            if drawer_rows
            else ""
        )
        toggle = (
            f" onclick=\"var d=document.getElementById('drawer-{r['ticker']}-{i}');"
            "if(d){d.style.display=d.style.display==='none'?'table-row':'none'}\""
            if drawer_rows
            else ""
        )
        hcount = r.get("horizon_count") or 1
        stars = "★" * hcount if hcount >= 2 else ""
        row_cls = "row-main star" if hcount >= 2 else "row-main"
        body_rows.append(
            f"<tr class='{row_cls}' {toggle} style='cursor:pointer'>"
            f"<td>{r['rank']}</td>"
            f"<td class='star'>{stars}</td>"
            f"<td><strong>{_html_escape(r['ticker'])}</strong></td>"
            f"<td>{_html_escape((r['name'] or '')[:60])}</td>"
            f"<td>{sector_html}</td>"
            f"<td class='num'>{r['blended']:.3f}</td>"
            f"<td class='num'>{r['composite']:.3f}</td>"
            f"<td class='num'>{r['ml']:.3f}</td>"
            f"<td class='num'>{pct}</td>"
            f"<td class='num'>{upside}</td>"
            "</tr>"
            + drawer_html
        )
    return f"<table class='top'>{head}<tbody>{''.join(body_rows)}</tbody></table>"


def _html_runs_table(rows: list[dict]) -> str:
    if not rows:
        return "<p><em>(no runs logged)</em></p>"
    body_rows = []
    for r in rows:
        started = r["started"].strftime("%Y-%m-%d %H:%M:%SZ") if r["started"] else ""
        cls = "ok" if r["status"] == "ok" else "err" if r["status"] == "error" else ""
        body_rows.append(
            f"<tr class='{cls}'>"
            f"<td>{_html_escape(r['job'])}</td>"
            f"<td>{_html_escape(r['status'])}</td>"
            f"<td class='num'>{r['rows']}</td>"
            f"<td>{started}</td>"
            f"<td>{_html_escape(r['error'] or '')}</td>"
            "</tr>"
        )
    head = (
        "<thead><tr><th>Job</th><th>Status</th><th>Rows</th>"
        "<th>Started (UTC)</th><th>Error</th></tr></thead>"
    )
    return f"<table>{head}<tbody>{''.join(body_rows)}</tbody></table>"


def _html_columns() -> str:
    items = "".join(
        f"<dt>{_html_escape(name)}</dt><dd>{_html_escape(doc)}</dd>"
        for name, doc in COLUMN_DOCS
    )
    return f"<dl class='columns'>{items}</dl>"


def _heartbeat_badge() -> str:
    """Return an HTML badge showing how long since the most recent successful run.
    Colour-coded so you can tell at a glance if the crawler is alive."""
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
    age = datetime.utcnow() - finished
    mins = int(age.total_seconds() / 60)
    if mins < 30:
        cls, label = "green", f"{mins} min ago"
    elif mins < 120:
        cls, label = "amber", f"{mins} min ago"
    else:
        hours = mins / 60
        cls, label = "red", f"{hours:.1f} h ago"
    iso = finished.isoformat(timespec="seconds")
    title = f"Last successful pipeline run at {iso}Z"
    return f"<span class='badge {cls}' title='{title}'>last crawl: {label}</span>"


def _source_breadth_html() -> str:
    """One-line badge enumerating every data source and its last-success time.
    Stops the "we only use Yahoo" misconception cold."""
    sources_seen = {
        "yfinance": "Yahoo Finance",
        "finnhub": "Finnhub",
        "fmp": "Financial Modeling Prep",
        "stooq": "stooq",
        "edgar.13f": "SEC EDGAR (13F)",
        "edgar.form4": "SEC EDGAR (Form 4)",
    }
    try:
        with session_scope() as s:
            rows = s.execute(
                select(RunLog.job, RunLog.status, RunLog.finished_at)
                .where(RunLog.finished_at.isnot(None))
                .order_by(RunLog.finished_at.desc())
                .limit(500)
            ).all()
    except Exception:
        rows = []
    # Most recent success per source prefix.
    last_ok: dict[str, datetime] = {}
    for job, status, finished in rows:
        if status != "ok":
            continue
        for prefix in sources_seen:
            if job and job.startswith(prefix) and prefix not in last_ok:
                last_ok[prefix] = finished
                break
    parts: list[str] = []
    for prefix, pretty in sources_seen.items():
        finished = last_ok.get(prefix)
        if finished is not None:
            age_min = int((datetime.utcnow() - finished).total_seconds() / 60)
            label = f"{age_min} min" if age_min < 120 else f"{age_min / 60:.1f} h"
            iso = finished.isoformat(timespec="seconds")
            parts.append(
                f"<span class='src-badge ok' title='Last ok: {iso}Z'>"
                f"<strong>{pretty}</strong> ✓ {label}</span>"
            )
        else:
            parts.append(
                f"<span class='src-badge none' title='No successful run yet — key may be missing'>"
                f"{pretty} ⚠</span>"
            )
    return "<p class='src-breadth'>Sources this run: " + " · ".join(parts) + "</p>"


def _build_html(as_of: date, n: int) -> str:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    heartbeat = _heartbeat_badge()
    source_breadth_html = _source_breadth_html()
    by_h = _collect_top_by_horizon(as_of, n)
    starred = sorted(
        {r["ticker"] for rows in by_h.values() for r in rows if r["horizon_count"] >= 2}
    )
    starred_html = (
        "<p class='starred'><strong>High-conviction cross-horizon picks:</strong> "
        + ", ".join(f"<strong>{_html_escape(t)}</strong>" for t in starred)
        + "</p>"
        if starred
        else "<p class='starred muted'>No ticker currently appears in more than one horizon's top list.</p>"
    )
    sections: list[str] = []
    for h in HORIZONS:
        sections.append(
            f"<section>"
            f"<h2>{_html_escape(HORIZON_TITLE.get(h, h))} — top {n}</h2>"
            f"<p class='blurb'>{_html_escape(HORIZON_BLURB.get(h, ''))}</p>"
            f"{_html_top_table(by_h[h])}"
            "</section>"
        )
    snapshot_rows = _coverage_snapshot_rows(by_h)
    sections.append(
        "<section><h2>Stock coverage snapshot</h2>"
        "<p class='blurb'>One row per unique ticker in any top list, sorted "
        "by upside. Stock-level facts (Buy/Hold/Sell/Upside/Analysts) are "
        "the same for a ticker no matter the horizon, so they live here.</p>"
        f"{_coverage_snapshot_html(snapshot_rows)}</section>"
    )
    runs_html = _html_runs_table(_recent_runs_safe())
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Invest — Top {n}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="300">
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
  footer {{ margin-top: 3rem; color: #777; font-size: 0.85rem; }}
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
  .src-breadth {{ font-size: 0.88rem; margin: 0.4rem 0 1rem 0; color: #444; }}
  .src-badge {{ display: inline-block; padding: 0.12rem 0.5rem; border-radius: 4px;
                margin-right: 0.2rem; }}
  .src-badge.ok {{ background: rgba(47,133,90,0.15); color: #1e5d3d; }}
  .src-badge.none {{ background: rgba(127,127,127,0.15); color: #888; }}
</style>
</head>
<body>
<h1>Invest — Top {n} {heartbeat}</h1>
<p class="meta">Generated: <strong>{generated}</strong> · Scores as of: <strong>{as_of.isoformat()}</strong>
 · page auto-refreshes every 5 min · pipeline runs every 2 hours via GitHub Actions.</p>
{source_breadth_html}
{starred_html}

{"".join(sections)}

<section><h2>Recent pipeline runs</h2>{runs_html}</section>

<footer>
  Data: yfinance (prices, consensus, price targets, rating actions), stooq (price backfill),
  SEC EDGAR (13F-HR holdings from ~40 top institutional filers, Form 4 insider activity),
  Finnhub (optional, when an API key is configured).
</footer>
</body>
</html>
"""


def _placeholder() -> tuple[str, str]:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    md = "_(awaiting first crawl)_\n"
    _ = generated  # used only in the HTML placeholder below
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Invest — Top 10</title>
<meta http-equiv="refresh" content="60"></head>
<body style="font-family: -apple-system, Helvetica, sans-serif; max-width: 800px; margin: 3rem auto;">
<h1>Invest — awaiting first crawl</h1>
<p>Generated: <strong>{generated}</strong>. The pipeline has not yet produced any scores.
The GitHub Actions workflow runs every 2 hours — refresh this page later.</p>
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
