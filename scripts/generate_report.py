"""Render top-20 per horizon to REPORT.md and docs/index.html.

Reads the latest persisted scores from SQLite and writes a human-readable
report that GitHub can render directly (so you don't need to run anything
locally to see the results).
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
    with session_scope() as s:
        row = s.execute(select(Score.as_of).order_by(desc(Score.as_of)).limit(1)).first()
    return row[0] if row else None


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


def _runs_table(rows: list[dict]) -> str:
    if not rows:
        return "_(no runs logged)_\n"
    lines = [
        "| Job | Status | Rows | Started | Error |",
        "|---|---|---:|---|---|",
    ]
    for r in rows:
        started = r["started"].strftime("%Y-%m-%d %H:%M:%SZ") if r["started"] else ""
        err = r["error"] or ""
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
    parts.append(_runs_table(_recent_runs()))
    return "\n".join(parts)


def _build_html(md_body: str) -> str:
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<title>Invest — Top 20</title>
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
         max-width: 1100px; margin: 2rem auto; padding: 0 1rem; color: #111; }}
  h1 {{ margin-bottom: 0; }}
  h2 {{ border-bottom: 1px solid #eee; padding-bottom: 0.25rem; margin-top: 2rem; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 0.95rem; }}
  th, td {{ padding: 0.4rem 0.6rem; border-bottom: 1px solid #eee; text-align: left; }}
  th {{ background: #fafafa; }}
  code {{ background: #f2f2f2; padding: 0.1rem 0.3rem; border-radius: 3px; }}
  blockquote {{ border-left: 3px solid #ccc; margin: 1rem 0; padding: 0.5rem 1rem; color: #444; }}
</style>
</head>
<body>
<pre style=\"display:none\">{md_body[:1]}</pre>
<!-- Rendered markdown below; GitHub will show REPORT.md with its own styles. -->
<article id=\"report\"></article>
<script>
  // Fetch the raw markdown and render it as HTML using a tiny inline converter.
  // For anything richer (Pages), GitHub auto-renders REPORT.md directly.
  fetch('../REPORT.md').then(r => r.text()).then(t => {{
    document.getElementById('report').textContent = t;
  }});
</script>
</body>
</html>
"""


def main() -> None:
    settings = get_settings()
    as_of = _latest_as_of()
    if as_of is None:
        REPORT_MD.write_text(
            "# Invest — Top 20 report\n\n"
            "_No scores have been computed yet. Run `make ingest && make rank`._\n"
        )
        print("no scores yet; wrote placeholder report")
        return

    md = _build_markdown(as_of, settings.top_n)
    REPORT_MD.write_text(md)
    REPORT_HTML.parent.mkdir(parents=True, exist_ok=True)
    REPORT_HTML.write_text(_build_html(md))
    print(f"wrote {REPORT_MD} and {REPORT_HTML}")


if __name__ == "__main__":
    main()
