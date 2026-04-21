"""Render top-20 per horizon to REPORT.md and docs/index.html.

Reads the latest persisted scores from SQLite and writes a human-readable
report that GitHub can render directly, plus a self-contained HTML page
that GitHub Pages serves without needing any runtime fetch.
"""
from __future__ import annotations

import hashlib
from datetime import date, datetime, timedelta
from pathlib import Path

from sqlalchemy import desc, select

from invest.config import HORIZONS, get_settings
from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Holding13F, Price, RunLog, Score, Stock

HERE = Path(__file__).resolve().parent.parent
REPORT_MD = HERE / "REPORT.md"
REPORT_HTML = HERE / "docs" / "index.html"


# Per-horizon plain-English explainer shown in the report header.
HORIZON_BLURB: dict[str, str] = {
    "days": (
        "5-day holding. Weights analyst rating momentum and short-term price "
        "momentum most; less weight on long-run price-target upside."
    ),
    "weeks": (
        "20-day (~1 month) holding. Balanced mix of consensus, price-target "
        "upside, rating momentum and price trend."
    ),
    "months": (
        "90-day holding. Leans on analyst consensus, price-target upside, and "
        "institutional (13F) flow; actively de-weights short-term price chase."
    ),
}


# Column definitions. Order matches the tables.
COLUMN_DOCS: list[tuple[str, str]] = [
    ("#", "Rank (1 = highest blended score in this horizon)."),
    (
        "★★ / ★★★",
        "Cross-horizon highlight. ★★ = this ticker ranks in two of the three "
        "top-15 lists; ★★★ (rare) = it's in all three. High-conviction names.",
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
        "(analyst consensus, price-target upside, rating momentum 7 d & 30 d, "
        "target revision 30 d, 13F institutional flow, insider net buy 90 d, "
        "21-day price momentum, realised-volatility risk penalty).",
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
    (
        "Upside",
        "Analyst consensus price target / last close − 1. Positive = analysts "
        "think there is room above the current price.",
    ),
    (
        "Buy / Hold / Sell",
        "Aggregated analyst rating counts (most recent consensus snapshot). "
        "Strong Buy + Buy are combined into 'Buy'; Strong Sell + Sell into 'Sell'.",
    ),
    (
        "Firms",
        "Count of distinct sell-side analyst firms that have publicly issued "
        "an action (upgrade / downgrade / reiterate) on this ticker in the "
        "last 90 days — sourced from yfinance's upgrades/downgrades feed and "
        "Finnhub's upgrade-downgrade endpoint when a key is configured. The "
        "Buy / Hold / Sell columns aggregate the ratings of every firm that "
        "publicly covers the stock (typically 10–30 firms for US large caps, "
        "5–15 for small caps, fewer for non-US).",
    ),
    (
        "Insts",
        "Count of tracked institutional 13F filers (Berkshire, BlackRock, "
        "Bridgewater, Renaissance, Citadel, Tiger, ARK …) currently holding "
        "the stock in their most recent 13F-HR.",
    ),
]


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
    today = date.today()
    cutoff_90 = today - timedelta(days=90)

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
                out[t]["buy"] = buy
                out[t]["hold"] = hold
                out[t]["sell"] = sell
                out[t]["mean_target"] = c.mean_target
                last = out[t].get("last_close")
                if c.mean_target and last:
                    out[t]["upside_pct"] = c.mean_target / last - 1

        # Distinct analyst firms (last 90 d) + the ~6 most recent actions for the drawer.
        for t in tickers:
            firms_q = (
                s.query(AnalystAction.firm)
                .filter(
                    AnalystAction.ticker == t,
                    AnalystAction.date >= cutoff_90,
                    AnalystAction.firm.isnot(None),
                )
                .distinct()
                .all()
            )
            out[t]["firm_count"] = len(firms_q)
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
    if not rows:
        return "_(no data)_\n"
    headers = [
        "#", "★", "Ticker", "Name", "Sector",
        "Blended", "Composite", "ML", "Pctile",
        "Upside", "Buy", "Hold", "Sell", "Firms", "Insts",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        pct = f"{(r['percentile'] or 0) * 100:.1f}%"
        upside = f"{(r.get('upside_pct') or 0) * 100:+.1f}%" if r.get("upside_pct") is not None else "—"
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
                    str(r.get("buy") or 0),
                    str(r.get("hold") or 0),
                    str(r.get("sell") or 0),
                    str(r.get("firm_count") or 0),
                    str(r.get("inst_count") or 0),
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
    of horizons in which that ticker also appears (so we can render a ★ / ★★
    cross-horizon highlight)."""
    by_h = {h: _top_rows(h, as_of, n) for h in HORIZONS}
    # Count how many lists each ticker shows up in.
    counts: dict[str, int] = {}
    for rows in by_h.values():
        for r in rows:
            counts[r["ticker"]] = counts.get(r["ticker"], 0) + 1
    for rows in by_h.values():
        for r in rows:
            r["horizon_count"] = counts.get(r["ticker"], 1)
    return by_h


def _build_markdown(as_of: date, n: int) -> str:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    by_h = _collect_top_by_horizon(as_of, n)
    starred = sorted(
        {r["ticker"] for rows in by_h.values() for r in rows if r["horizon_count"] >= 2}
    )
    starred_line = (
        "**High-conviction cross-horizon picks:** "
        + ", ".join(f"**{t}**" for t in starred)
        if starred
        else "_No ticker currently appears in more than one horizon's top list._"
    )
    parts: list[str] = [
        f"# Invest — Top {n} report",
        "",
        f"_Generated: **{generated}** · Scores as of: **{as_of.isoformat()}**_",
        "",
        _heartbeat_md(),
        "",
        "> Not investment advice. Ranks publicly available analyst consensus, price-target "
        "upside, rating momentum, institutional 13F flow, insider activity, price momentum, "
        "and risk into a blended composite + ML score per horizon.",
        "",
        starred_line,
        "",
        "## How to read this",
        "",
        _columns_md(),
    ]
    for h in HORIZONS:
        parts.append(f"## {h.capitalize()} horizon — top {n}")
        parts.append("")
        parts.append(f"_{HORIZON_BLURB[h]}_")
        parts.append("")
        parts.append(_md_table(by_h[h]))
        parts.append("")

    parts.append("## Recent pipeline runs")
    parts.append("")
    parts.append(_runs_md_table(_recent_runs_safe()))
    return "\n".join(parts)


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
        "<th title='High-conviction star: ★★ = ranks in two horizons; ★★★ = all three.'>★</th>"
        "<th>Ticker</th><th>Name</th><th>Sector</th>"
        "<th title='Final score, z-scored across the universe.'>Blended</th>"
        "<th title='Rule-based score from nine weighted features.'>Composite</th>"
        "<th title='LightGBM predicted forward return (cold-start = composite).'>ML</th>"
        "<th title='Percentile of blended score in this horizon.'>Pctile</th>"
        "<th title='Consensus price target / last close − 1.'>Upside</th>"
        "<th title='Strong Buy + Buy count.'>Buy</th>"
        "<th>Hold</th>"
        "<th title='Sell + Strong Sell count.'>Sell</th>"
        "<th title='Distinct analyst firms with actions in the last 90 d.'>Firms</th>"
        "<th title='Tracked 13F filers holding the stock.'>Insts</th>"
        "</tr></thead>"
    )
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
        # Analyst firms drawer.
        actions = r.get("recent_actions", [])
        drawer_rows = "".join(
            "<tr>"
            f"<td>{a['date'].isoformat() if a.get('date') else ''}</td>"
            f"<td>{_html_escape(a.get('firm') or '')}</td>"
            f"<td>{_html_escape((a.get('action') or '').title())}</td>"
            f"<td>{_html_escape((a.get('from') or '') + ' → ' + (a.get('to') or ''))}</td>"
            f"<td class='num'>{a.get('target') or ''}</td>"
            f"<td class='src'>{_html_escape(a.get('source') or '')}</td>"
            "</tr>"
            for a in actions
        )
        drawer_html = (
            f"<tr class='drawer' id='drawer-{r['ticker']}-{i}' style='display:none'>"
            "<td colspan='14'>"
            "<strong>Recent analyst actions</strong>"
            "<table class='inner'><thead><tr><th>Date</th><th>Firm</th>"
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
            f"<td class='num ok'>{r.get('buy') or 0}</td>"
            f"<td class='num'>{r.get('hold') or 0}</td>"
            f"<td class='num err'>{r.get('sell') or 0}</td>"
            f"<td class='num'>{r.get('firm_count') or 0}</td>"
            f"<td class='num'>{r.get('inst_count') or 0}</td>"
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


def _build_html(as_of: date, n: int) -> str:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    heartbeat = _heartbeat_badge()
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
            f"<h2>{h.capitalize()} horizon — top {n}</h2>"
            f"<p class='blurb'>{_html_escape(HORIZON_BLURB[h])}</p>"
            f"{_html_top_table(by_h[h])}"
            "</section>"
        )
    runs_html = _html_runs_table(_recent_runs_safe())
    columns_html = _html_columns()
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
</style>
</head>
<body>
<h1>Invest — Top {n} {heartbeat}</h1>
<p class="meta">Generated: <strong>{generated}</strong> · Scores as of: <strong>{as_of.isoformat()}</strong>
 · page auto-refreshes every 5 min · pipeline runs every 20 min via GitHub Actions.</p>
<blockquote>
  <strong>Not investment advice.</strong> Ranks publicly available analyst consensus, price-target upside,
  rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a blended
  composite + ML score per horizon. Click any row to see the most recent analyst actions for that ticker.
</blockquote>

{starred_html}

<details open>
  <summary>How to read this report</summary>
  {columns_html}
</details>

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
    md = (
        "# Invest — Top 15 report\n\n"
        f"_Generated: **{generated}**_\n\n"
        "The pipeline has not yet produced any scores. The GitHub Actions workflow is "
        "scheduled to run every 20 minutes — the first successful run will populate this file.\n"
    )
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Invest — Top 15</title>
<meta http-equiv="refresh" content="60"></head>
<body style="font-family: -apple-system, Helvetica, sans-serif; max-width: 800px; margin: 3rem auto;">
<h1>Invest — awaiting first crawl</h1>
<p>Generated: <strong>{generated}</strong>. The pipeline has not yet produced any scores.
The GitHub Actions workflow runs every 20 minutes — refresh this page in a few minutes.</p>
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
