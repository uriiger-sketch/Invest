"""Render top-20 per horizon to REPORT.md and docs/index.html.

Reads the latest persisted scores from SQLite and writes a human-readable
report that GitHub can render directly, plus a self-contained HTML page
that GitHub Pages serves without needing any runtime fetch.
"""
from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

from sqlalchemy import desc, select

from invest.config import HORIZONS, get_settings
from invest.db import session_scope
from invest.models import RunLog, Score, Stock

HERE = Path(__file__).resolve().parent.parent
REPORT_MD = HERE / "REPORT.md"
REPORT_HTML = HERE / "docs" / "index.html"


def _latest_as_of() -> date | None:
    try:
        with session_scope() as s:
            row = s.execute(select(Score.as_of).order_by(desc(Score.as_of)).limit(1)).first()
        return row[0] if row else None
    except Exception:
        return None


def _recent_runs_safe(limit: int = 20) -> list[dict]:
    try:
        return _recent_runs(limit)
    except Exception:
        return []


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
        }
        for i, r in enumerate(rows)
    ]


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


def _md_table(rows: list[dict]) -> str:
    if not rows:
        return "_(no data)_\n"
    headers = ["#", "Ticker", "Name", "Sector", "Blended", "Composite", "ML", "Pctile"]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        pct = f"{(r['percentile'] or 0) * 100:.1f}%"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["rank"]),
                    f"**{r['ticker']}**",
                    r["name"][:40],
                    r["sector"][:20],
                    f"{r['blended']:.3f}",
                    f"{r['composite']:.3f}",
                    f"{r['ml']:.3f}",
                    pct,
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


def _build_markdown(as_of: date, n: int) -> str:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    parts: list[str] = [
        "# Invest — Top 20 report",
        "",
        f"_Generated: **{generated}** · Scores as of: **{as_of.isoformat()}**_",
        "",
        "> Not investment advice. Ranks publicly available analyst consensus, price-target upside, "
        "rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a "
        "blended composite + ML score per horizon. See `README.md` for methodology.",
        "",
    ]
    for h in HORIZONS:
        parts.append(f"## {h.capitalize()} horizon")
        parts.append("")
        parts.append(_md_table(_top_rows(h, as_of, n)))
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
        "<th>#</th><th>Ticker</th><th>Name</th><th>Sector</th>"
        "<th>Blended</th><th>Composite</th><th>ML</th><th>Percentile</th>"
        "</tr></thead>"
    )
    body_rows = []
    for r in rows:
        pct = f"{(r['percentile'] or 0) * 100:.1f}%"
        body_rows.append(
            "<tr>"
            f"<td>{r['rank']}</td>"
            f"<td><strong>{_html_escape(r['ticker'])}</strong></td>"
            f"<td>{_html_escape(r['name'][:60])}</td>"
            f"<td>{_html_escape(r['sector'][:30])}</td>"
            f"<td class='num'>{r['blended']:.3f}</td>"
            f"<td class='num'>{r['composite']:.3f}</td>"
            f"<td class='num'>{r['ml']:.3f}</td>"
            f"<td class='num'>{pct}</td>"
            "</tr>"
        )
    return f"<table>{head}<tbody>{''.join(body_rows)}</tbody></table>"


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


def _build_html(as_of: date, n: int) -> str:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    sections: list[str] = []
    for h in HORIZONS:
        sections.append(
            f"<section><h2>{h.capitalize()} horizon</h2>"
            f"{_html_top_table(_top_rows(h, as_of, n))}</section>"
        )
    runs_html = _html_runs_table(_recent_runs_safe())
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Invest — Top 20</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="300">
<style>
  :root {{ color-scheme: light dark; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
         max-width: 1150px; margin: 2rem auto; padding: 0 1rem; line-height: 1.5; }}
  h1 {{ margin-bottom: 0.25rem; }}
  h2 {{ border-bottom: 1px solid rgba(127,127,127,0.25); padding-bottom: 0.25rem; margin-top: 2rem; }}
  .meta {{ color: #666; font-size: 0.9rem; }}
  blockquote {{ border-left: 3px solid #999; margin: 1rem 0; padding: 0.5rem 1rem; color: #555; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.95rem; margin-top: 0.5rem; }}
  th, td {{ padding: 0.4rem 0.6rem; border-bottom: 1px solid rgba(127,127,127,0.2); text-align: left; }}
  th {{ background: rgba(127,127,127,0.08); }}
  td.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
  tr.err td {{ color: #b00; }}
  tr.ok td:nth-child(2) {{ color: #28823a; }}
  footer {{ margin-top: 3rem; color: #777; font-size: 0.85rem; }}
</style>
</head>
<body>
<h1>Invest — Top 20</h1>
<p class="meta">Generated: <strong>{generated}</strong> · Scores as of: <strong>{as_of.isoformat()}</strong>
 · auto-refreshes every 5 min.</p>
<blockquote>
  Not investment advice. Ranks publicly available analyst consensus, price-target upside,
  rating momentum, institutional 13F flow, insider activity, price momentum, and risk into a
  blended composite + ML score per horizon.
</blockquote>
{"".join(sections)}
<section><h2>Recent pipeline runs</h2>{runs_html}</section>
<footer>
  Source: <a href="https://github.com/uriiger-sketch/invest">uriiger-sketch/invest</a> ·
  Pipeline runs every 20 min via GitHub Actions.
</footer>
</body>
</html>
"""


def _placeholder() -> tuple[str, str]:
    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    md = (
        "# Invest — Top 20 report\n\n"
        f"_Generated: **{generated}**_\n\n"
        "The pipeline has not yet produced any scores. The GitHub Actions workflow is "
        "scheduled to run every 20 minutes — the first successful run will populate this file.\n"
    )
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Invest — Top 20</title>
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
