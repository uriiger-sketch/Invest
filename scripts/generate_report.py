"""Render the integrated ranking to REPORT.md and docs/index.html.

Reads the latest persisted scores, integrated grades and calibration from
SQLite and writes a GitHub-renderable Markdown table plus a self-contained
HTML page (served by GitHub Pages without any runtime fetch). Each HTML row
opens a drawer with the evidence behind the grade: its main drivers, recent
analyst rating AND price-target changes, the latest headlines with their
tone, estimate revisions, earnings and SEC events.
"""
from __future__ import annotations

import hashlib
import json
import math
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from sqlalchemy import desc, func, select

from invest.config import HORIZONS, get_settings
from invest.db import session_scope
from invest.models import (
    AnalystAction,
    Calibration,
    Consensus,
    Grade,
    IntelSnapshot,
    NewsItem,
    Price,
    RunLog,
    Score,
    SecFiling,
    Stock,
)

HERE = Path(__file__).resolve().parent.parent
REPORT_MD = HERE / "REPORT.md"
REPORT_HTML = HERE / "docs" / "index.html"
HISTORY_PATH = HERE / "docs" / "history.jsonl"


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
    candidates = [{"ticker": r.ticker, "sector": r.sector, "_row": r} for r in raw]
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


def _load_payload(raw: str | None) -> dict:
    try:
        d = json.loads(raw or "")
        return d if isinstance(d, dict) else {}
    except (TypeError, ValueError):
        return {}


def _enrichment_for(tickers: list[str]) -> dict[str, dict]:
    """Per-ticker evidence for the table and drawer: last close, consensus,
    rating and target changes, headlines, estimates, events, filings."""
    if not tickers:
        return {}
    from invest.pipeline.features import current_13f_filers

    out: dict[str, dict] = {t: {} for t in tickers}
    now = datetime.now(UTC).replace(tzinfo=None)
    today = date.today()

    with session_scope() as s:
        # Last GOOD close (NULL-close rows are data gaps, seen live on PRX.AS).
        for t in tickers:
            row = (
                s.query(Price.close, Price.date)
                .filter(Price.ticker == t, Price.close.isnot(None))
                .order_by(Price.date.desc())
                .first()
            )
            if row:
                out[t]["last_close"] = row.close

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
                # By construction analysts == buy + hold + sell.
                out[t].update({
                    "buy": buy, "hold": hold, "sell": sell,
                    "strong_buy": c.strong_buy or 0, "strong_sell": c.strong_sell or 0,
                    "analysts": buy + hold + sell, "mean_target": c.mean_target,
                    "high_target": c.high_target, "low_target": c.low_target,
                })
                last = out[t].get("last_close")
                if c.mean_target and last:
                    out[t]["upside_pct"] = c.mean_target / last - 1

        # Rating / target changes, last 45 days, newest first.
        cutoff = today - timedelta(days=45)
        for t in tickers:
            recent = (
                s.query(AnalystAction)
                .filter(AnalystAction.ticker == t, AnalystAction.date >= cutoff)
                .order_by(AnalystAction.date.desc())
                .limit(10)
                .all()
            )
            acts = [
                {
                    "date": a.date, "firm": a.firm, "action": a.action,
                    "from": a.from_grade, "to": a.to_grade,
                    "target": a.target_price, "prior_target": a.prior_target,
                    "target_action": a.target_action, "source": a.source,
                }
                for a in recent
            ]
            out[t]["recent_actions"] = acts
            m30 = [a for a in acts if a["date"] >= today - timedelta(days=30)]
            out[t]["upgrades_30d"] = sum(1 for a in m30 if "up" in (a["action"] or ""))
            out[t]["downgrades_30d"] = sum(1 for a in m30 if "down" in (a["action"] or ""))
            out[t]["target_raises_30d"] = sum(
                1 for a in m30 if a["target"] and a["prior_target"] and a["target"] > a["prior_target"]
            )
            out[t]["target_cuts_30d"] = sum(
                1 for a in m30 if a["target"] and a["prior_target"] and a["target"] < a["prior_target"]
            )

        # Headlines (7 days) and their tone.
        since = now - timedelta(days=7)
        for t in tickers:
            items = (
                s.query(NewsItem)
                .filter(NewsItem.ticker == t, NewsItem.published_at >= since)
                .order_by(NewsItem.published_at.desc())
                .limit(40)
                .all()
            )
            out[t]["news"] = [
                {"title": n.title, "publisher": n.publisher, "url": n.url,
                 "at": n.published_at, "sentiment": n.sentiment}
                for n in items[:6]
            ]
            out[t]["news_count_7d"] = len(items)
            if items:
                w = [(n.relevance or 0.5) for n in items]
                out[t]["news_tone"] = sum(
                    wi * (n.sentiment or 0.0) for wi, n in zip(w, items)
                ) / (sum(w) + 1.0)

        intel = {
            t: _load_payload(p)
            for t, p in s.query(IntelSnapshot.ticker, IntelSnapshot.payload).filter(
                IntelSnapshot.ticker.in_(tickers), IntelSnapshot.kind == "quote"
            )
        }
        for t, p in intel.items():
            eps = (p.get("eps") or {}).get("0y") or {}
            st = p.get("stats") or {}
            sur = (p.get("surprises") or [None])[0]
            out[t]["intel"] = {
                "eps_now": eps.get("cur"), "eps_30d": eps.get("d30"),
                "eps_up30": eps.get("up30"), "eps_dn30": eps.get("dn30"),
                "surprise": sur, "next_earnings": p.get("next_earnings"),
                "fwd_pe": st.get("fpe"), "short_float": st.get("short_float"),
                "target_median": (p.get("targets") or {}).get("median"),
                "rec_trend": p.get("rec_trend") or {},
            }

        filings = (
            s.query(SecFiling)
            .filter(SecFiling.ticker.in_(tickers),
                    SecFiling.filing_date >= today - timedelta(days=90))
            .order_by(SecFiling.filing_date.desc())
            .all()
        )
        for f in filings:
            lst = out[f.ticker].setdefault("filings", [])
            if len(lst) < 6 and not f.form.startswith(("10-", "20-F", "40-F", "SC 13G", "SCHEDULE 13G")):
                lst.append({"date": f.filing_date, "form": f.form, "items": f.items,
                            "desc": f.description})

    holders = current_13f_filers(tickers)
    for t in tickers:
        out[t]["inst_count"] = len(holders.get(t, ()))
    return out


def _grades_for(tickers: list[str], as_of: date | None = None) -> dict[str, dict]:
    """Latest integrated grade per ticker (pipeline/grade.py)."""
    if not tickers:
        return {}
    with session_scope() as s:
        if as_of is None:
            as_of = s.execute(select(func.max(Grade.as_of))).scalar()
        if as_of is None:
            return {}
        rows = s.query(Grade).filter(Grade.as_of == as_of, Grade.ticker.in_(tickers)).all()
    return {
        g.ticker: {
            "grade_score": g.grade_score, "letter": g.letter, "grade_pct": g.percentile,
            "confidence": g.confidence, "alpha_1m": g.alpha_1m, "alpha_3m": g.alpha_3m,
            "p_outperform_1m": g.p_outperform_1m, "detail": _load_payload(g.detail_json),
        }
        for g in rows
    }


def _collect_top_by_horizon(as_of: date, n: int) -> dict[str, list[dict]]:
    """Pull top-N rows once per horizon, then annotate every row with the count
    AND labels of horizons in which that ticker also appears."""
    by_h = {h: _top_rows(h, as_of, n) for h in HORIZONS}
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
    """Canonical identity for a (firm, firm_key) row pair."""
    from invest.firms import canonical_firm_key

    return firm_key or canonical_firm_key(firm)


def _total_sources_per_ticker(tickers: list[str]) -> dict[str, int]:
    """Distinct contributors per ticker — IDENTICAL to features.build_features:

        max(covering analysts, named rating-changers in 90 d)
        + tracked 13F filers holding it in a current period
        + insider filers in 90 d

    Any divergence makes the Sources column contradict the gate that
    selected the row (it did once: `Sources = 0` next to picks that had
    cleared a 12-source floor).
    """
    if not tickers:
        return {}
    from invest.models import InsiderTrade
    from invest.pipeline.features import current_13f_filers

    cutoff = date.today() - timedelta(days=90)
    named: dict[str, set[str]] = {}
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
        for t, ifiler in s.execute(
            select(InsiderTrade.ticker, InsiderTrade.filer).where(
                InsiderTrade.ticker.in_(tickers),
                InsiderTrade.date >= cutoff,
                InsiderTrade.filer.isnot(None),
            )
        ).all():
            insiders.setdefault(t, set()).add(ifiler.lower().strip())
    insts = current_13f_filers(tickers)
    covering = _covering_analysts_per_ticker(tickers)
    return {
        t: max(covering.get(t, 0), len(named.get(t, ())))
        + len(insts.get(t, ()))
        + len(insiders.get(t, ()))
        for t in tickers
    }


def _covering_analysts_per_ticker(tickers: list[str]) -> dict[str, int]:
    """Covering-analyst count from the freshest consensus snapshot per ticker:
    the larger of the rating-bucket sum and the feed's own `num_analysts`."""
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
        buckets = sum(v or 0 for v in (r.strong_buy, r.buy, r.hold, r.sell, r.strong_sell))
        n = max(buckets, r.num_analysts or 0)
        prev = best.get(r.ticker)
        if prev is None or r.as_of_date > prev[0]:
            best[r.ticker] = (r.as_of_date, n)
        elif r.as_of_date == prev[0]:
            best[r.ticker] = (prev[0], max(prev[1], n))
    return {t: n for t, (_, n) in best.items()}


# ------------------------- history persistence -------------------------


def _append_history(by_h: dict[str, list[dict]], generated_at: datetime,
                    grades: dict[str, dict] | None = None) -> None:
    """Append one JSON line per ranked row to docs/history.jsonl (committed
    alongside the report, so ranking history survives any DB loss)."""
    HISTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    iso = generated_at.replace(microsecond=0).isoformat()
    grades = grades or {}
    lines: list[str] = []
    for h, rows in by_h.items():
        for r in rows:
            rec = {
                "ts": iso,
                "h": h,
                "rank": r["rank"],
                "ticker": r["ticker"],
                "score": round(float(r.get("blended", r.get("blended_score") or 0)), 4),
                "hc": int(r.get("horizon_count") or 1),
            }
            g = grades.get(r["ticker"])
            if g and g.get("letter"):
                rec["g"] = g["letter"]
            lines.append(json.dumps(rec, separators=(",", ":")))
    if lines:
        with HISTORY_PATH.open("a") as f:
            f.write("\n".join(lines) + "\n")


# --------------------------- main table ---------------------------


_HORIZON_LETTER = {"hours": "H", "daily": "D", "weekly": "W", "monthly": "M"}


def main_table_rows(by_h: dict[str, list[dict]]) -> list[dict]:
    """Collapse the four per-horizon lists into ONE ranked table.

    Candidates are the union of the horizons' diversified top lists. They
    are ordered by the INTEGRATED GRADE (pipeline/grade.py) — the
    correlation- and skill-weighted combination of all four horizon scores —
    instead of the old sum of top-list percentiles, which was discontinuous:
    a name ranked 36th on a horizon (just outside its top-35) got zero
    credit for it. Rows without a grade (fresh database) fall back to that
    legacy percentile sum. Capped to `settings.main_table_size`.
    """
    agg: dict[str, dict] = {}
    for h in HORIZONS:
        for r in by_h.get(h, []):
            t = r["ticker"]
            row = agg.setdefault(t, {**r, "horizons": [], "score": 0.0, "best_rank": 99})
            row["horizons"].append(h)
            row["score"] += float(r.get("percentile") or 0.0)
            row["best_rank"] = min(row["best_rank"], int(r.get("rank") or 99))

    rows = list(agg.values())
    tickers = [r["ticker"] for r in rows]
    sources = _total_sources_per_ticker(tickers)
    grades = _grades_for(tickers)
    for r in rows:
        r["sources"] = sources.get(r["ticker"], 0)
        r["analysts"] = r.get("analysts") or 0
        r.update(grades.get(r["ticker"], {}))

    def key(r: dict) -> tuple:
        g = r.get("grade_score")
        has = g is not None and math.isfinite(g)
        return (0 if has else 1, -(g if has else 0.0), -(r["score"]),
                -(r.get("upside_pct") or 0.0), r["best_rank"])

    rows.sort(key=key)
    rows = rows[: get_settings().main_table_size]
    for i, r in enumerate(rows, start=1):
        r["rank"] = i
    return rows


def _timeframe_marks(horizons: list[str]) -> str:
    """Compact H/D/W/M markers — replaces four near-duplicate tables."""
    present = set(horizons)
    return "".join(_HORIZON_LETTER[h] if h in present else "·" for h in HORIZONS)


def _pct(x: float | None, digits: int = 1, signed: bool = True) -> str:
    if x is None or (isinstance(x, float) and not math.isfinite(x)):
        return "—"
    return f"{x * 100:+.{digits}f}%" if signed else f"{x * 100:.{digits}f}%"


def _grade_cell(r: dict) -> str:
    if not r.get("letter"):
        return "—"
    return f"{r['letter']} ({r['grade_score']:+.2f})"


def _opinion_cell(r: dict) -> str:
    """Net 30-day opinion change: ↑ upgrades / ↓ downgrades, ▲ target raises / ▼ cuts."""
    parts = []
    up, dn = r.get("upgrades_30d") or 0, r.get("downgrades_30d") or 0
    tr, tc = r.get("target_raises_30d") or 0, r.get("target_cuts_30d") or 0
    if up or dn:
        parts.append(f"↑{up}/↓{dn}")
    if tr or tc:
        parts.append(f"▲{tr}/▼{tc}")
    return " ".join(parts) or "—"


def _news_cell(r: dict) -> str:
    n = r.get("news_count_7d") or 0
    if not n:
        return "—"
    tone = r.get("news_tone") or 0.0
    mark = "+" if tone > 0.05 else "−" if tone < -0.05 else "0"
    return f"{mark} ({n})"


def _main_table_md(rows: list[dict]) -> str:
    if not rows:
        return "_(no picks cleared the quality gates this run)_\n"
    headers = [
        "#", "Ticker", "Name", "Sector", "Grade", "Upside", "Price", "Target",
        "α 1M", "P(beat) 1M", "Conf", "News 7d", "Δ Opinion 30d", "H/D/W/M", "Analysts", "Sources",
    ]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        upside = f"**{_pct(r.get('upside_pct'))}**" if r.get("upside_pct") is not None else "—"
        price = f"{r['last_close']:.2f}" if r.get("last_close") else "—"
        target = f"{r['mean_target']:.2f}" if r.get("mean_target") else "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(r["rank"]),
                    f"**{r['ticker']}**",
                    (r.get("name") or "")[:28],
                    (r.get("sector") or "")[:18],
                    _grade_cell(r),
                    upside,
                    price,
                    target,
                    _pct(r.get("alpha_1m"), 2),
                    _pct(r.get("p_outperform_1m"), 1, signed=False),
                    _pct(r.get("confidence"), 0, signed=False),
                    _news_cell(r),
                    _opinion_cell(r),
                    _timeframe_marks(r["horizons"]),
                    str(r.get("analysts") or 0),
                    str(r.get("sources") or 0),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


_MD_LEGEND = (
    "\n_Grade: integrated cross-horizon score G (≈N(0,1) over gated stocks; letter by percentile). "
    "α 1M: expected excess return vs the universe over ~20 trading days (IC·σ·z). "
    "P(beat): calibrated probability of beating the universe median over that window. "
    "Conf: share of the model's weight backed by observed data. "
    "Δ Opinion: ↑upgrades/↓downgrades, ▲target raises/▼cuts (30 d). "
    "Methodology and data health: see the live page._\n"
)


def _staleness_banner_md(as_of: date) -> str | None:
    """Loud warning when the newest scores are old."""
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
    """ONE ranked main table plus a one-paragraph legend."""
    by_h = _collect_top_by_horizon(as_of, n)
    rows = main_table_rows(by_h)
    _append_history(by_h, datetime.now(UTC).replace(tzinfo=None), {r["ticker"]: r for r in rows})

    parts: list[str] = []
    banner = _staleness_banner_md(as_of)
    if banner:
        parts.append(banner)
        parts.append("")
    parts.append(_main_table_md(rows))
    parts.append(_MD_LEGEND)
    return "\n".join(parts).rstrip() + "\n"


# ---------------------------------- HTML ----------------------------------


def _html_escape(s: str) -> str:
    return (
        str(s).replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def _safe_url(url: str | None) -> str | None:
    if url and url.startswith(("https://", "http://")):
        return _html_escape(url)
    return None


def _tone_dot(s: float | None) -> str:
    s = s or 0.0
    if s > 0.15:
        return "<span class='tone pos' title='positive tone'>●</span>"
    if s < -0.15:
        return "<span class='tone neg' title='negative tone'>●</span>"
    return "<span class='tone neu' title='neutral tone'>●</span>"


def _drawer_html(r: dict, actions: list[dict]) -> str:
    from invest.firms import firm_tier
    from invest.pipeline.grade import FEATURE_LABELS

    blocks: list[str] = []
    det = r.get("detail") or {}
    if det:
        pos = ", ".join(_html_escape(FEATURE_LABELS.get(f, f)) for f, _ in det.get("drivers_pos", []))
        neg = ", ".join(_html_escape(FEATURE_LABELS.get(f, f)) for f, _ in det.get("drivers_neg", []))
        s_h = det.get("S") or {}
        per_h = " · ".join(f"{_HORIZON_LETTER.get(h, h)} {v:+.2f}" for h, v in s_h.items())
        blocks.append(
            "<div class='why'><strong>Why this grade.</strong> "
            + (f"Supported by {pos}. " if pos else "")
            + (f"Held back by {neg}. " if neg else "")
            + (f"Horizon scores (z): {per_h}. " if per_h else "")
            + (f"Expected excess return: 1M {_pct(r.get('alpha_1m'), 2)}, "
               f"3M {_pct(r.get('alpha_3m'), 2)}; "
               f"P(beat 1M) {_pct(r.get('p_outperform_1m'), 1, signed=False)}; "
               f"data confidence {_pct(r.get('confidence'), 0, signed=False)}."
               if r.get("letter") else "")
            + "</div>"
        )

    if actions:
        def _tgt(a: dict) -> str:
            tp, pp = a.get("target"), a.get("prior_target")
            if tp and pp:
                arrow = "▲" if tp > pp else "▼" if tp < pp else "="
                return f"{pp:g} → {tp:g} {arrow}"
            return f"{tp:g}" if tp else ""

        def _tier(firm: str | None) -> str:
            t = firm_tier(firm)
            return {1: "<td class='tier1'><strong>T1</strong></td>", 2: "<td class='tier2'>T2</td>",
                    3: "<td class='tier3'>T3</td>"}.get(t, "<td class='src'>—</td>")

        trs = "".join(
            "<tr>"
            f"<td>{a['date'].isoformat() if a.get('date') else ''}</td>"
            + _tier(a.get("firm"))
            + f"<td>{_html_escape(a.get('firm') or '')}</td>"
            f"<td>{_html_escape((a.get('action') or '').title())}</td>"
            f"<td>{_html_escape((a.get('from') or '') + ' → ' + (a.get('to') or ''))}</td>"
            f"<td class='num'>{_html_escape(_tgt(a))}</td>"
            "</tr>"
            for a in actions
        )
        blocks.append(
            "<strong>Analyst rating &amp; target changes (45 d)</strong>"
            "<table class='inner'><thead><tr><th>Date</th><th>Tier</th><th>Firm</th>"
            "<th>Action</th><th>Rating</th><th>Target</th></tr></thead>"
            f"<tbody>{trs}</tbody></table>"
        )

    news = r.get("news") or []
    if news:
        items = []
        for n in news:
            when = n["at"].strftime("%b %d") if n.get("at") else ""
            title = _html_escape(n.get("title") or "")
            url = _safe_url(n.get("url"))
            link = f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{title}</a>" if url else title
            pub = _html_escape(n.get("publisher") or "")
            items.append(f"<li>{_tone_dot(n.get('sentiment'))} {link} <span class='src'>{pub} · {when}</span></li>")
        blocks.append("<strong>Latest headlines</strong><ul class='news'>" + "".join(items) + "</ul>")

    intel = r.get("intel") or {}
    facts = []
    if intel.get("eps_now") is not None and intel.get("eps_30d") is not None:
        facts.append(f"FY EPS estimate {intel['eps_30d']:.2f} → {intel['eps_now']:.2f} (30 d)")
    if intel.get("eps_up30") is not None or intel.get("eps_dn30") is not None:
        facts.append(f"EPS revisions 30 d: {int(intel.get('eps_up30') or 0)} up / "
                     f"{int(intel.get('eps_dn30') or 0)} down")
    sur = intel.get("surprise")
    if sur and sur.get("est") not in (None, 0):
        facts.append(f"last quarter EPS {sur['act']:.2f} vs {sur['est']:.2f} est.")
    if intel.get("next_earnings"):
        facts.append(f"next earnings {intel['next_earnings']}")
    if intel.get("fwd_pe"):
        facts.append(f"forward P/E {intel['fwd_pe']:.1f}")
    if intel.get("short_float") is not None:
        facts.append(f"short interest {intel['short_float'] * 100:.1f}% of float")
    if facts:
        blocks.append("<strong>Estimates &amp; events.</strong> " + _html_escape("; ".join(facts)) + ".")

    filings = r.get("filings") or []
    if filings:
        li = "".join(
            f"<li>{f['date'].isoformat()} <strong>{_html_escape(f['form'])}</strong>"
            + (f" items {_html_escape(f['items'])}" if f.get("items") else "")
            + (f" — {_html_escape(f['desc'])}" if f.get("desc") else "")
            + "</li>"
            for f in filings
        )
        blocks.append(f"<strong>SEC filings (90 d)</strong><ul class='news'>{li}</ul>")
    return "".join(f"<div class='blk'>{b}</div>" for b in blocks)


def _main_table_html(rows: list[dict], by_h: dict[str, list[dict]]) -> str:
    """The main table; each row opens a drawer with the evidence behind it."""
    if not rows:
        return "<p><em>(no picks cleared the quality gates this run)</em></p>"

    actions_by_ticker: dict[str, list[dict]] = {}
    for h in HORIZONS:
        for r in by_h.get(h, []):
            actions_by_ticker.setdefault(r["ticker"], r.get("recent_actions") or [])

    head = (
        "<thead><tr>"
        "<th>#</th><th>Ticker</th><th>Name</th><th>Sector</th>"
        "<th title='Integrated cross-horizon grade (letter by percentile; G ≈ N(0,1) over gated stocks).'>Grade</th>"
        "<th title='Consensus price target vs current price.'>Upside</th>"
        "<th>Price</th><th>Target</th>"
        "<th title='Expected excess return vs the universe over ~20 trading days: IC · σ · z.'>α 1M</th>"
        "<th title='Calibrated probability of beating the universe median over ~1 month.'>P(beat)</th>"
        "<th title='Share of the model weight backed by observed data for this stock.'>Conf</th>"
        "<th title='Headline tone (+/0/−) and number of headlines in the last 7 days.'>News</th>"
        "<th title='Last 30 days: ↑upgrades/↓downgrades, ▲target raises/▼cuts.'>Δ Opinion</th>"
        "<th title='Which timeframes rank this name: Hours / Daily / Weekly / Monthly.'>H/D/W/M</th>"
        "<th>Analysts</th>"
        "<th title='Distinct named contributors: sell-side firms, current 13F filers, insider filers.'>Sources</th>"
        "</tr></thead>"
    )
    ncols = 16
    body: list[str] = []
    for i, r in enumerate(rows):
        upside = _pct(r.get("upside_pct")) if r.get("upside_pct") is not None else "—"
        up_cls = "num up-pos" if (r.get("upside_pct") or 0) > 0 else "num"
        price = f"{r['last_close']:.2f}" if r.get("last_close") else "—"
        target = f"{r['mean_target']:.2f}" if r.get("mean_target") else "—"
        sector = r.get("sector") or ""
        sector_html = (
            f"<span class='sector' style='background:{_sector_colour(sector)}'>"
            f"{_html_escape(sector[:22])}</span>"
            if sector
            else ""
        )
        letter = r.get("letter") or ""
        grade_html = (
            f"<span class='grade g{_html_escape(letter[0])}'>{_html_escape(letter)}</span> "
            f"<span class='src'>{r['grade_score']:+.2f}</span>" if letter else "—"
        )
        drawer_html = _drawer_html(r, actions_by_ticker.get(r["ticker"], []))
        drawer = (
            f"<tr class='drawer' id='d-{_html_escape(r['ticker'])}-{i}' style='display:none'>"
            f"<td colspan='{ncols}'>{drawer_html}</td></tr>"
            if drawer_html
            else ""
        )
        toggle = (
            f" onclick=\"var d=document.getElementById('d-{_html_escape(r['ticker'])}-{i}');"
            "if(d){d.style.display=d.style.display==='none'?'table-row':'none'}\""
            if drawer_html
            else ""
        )
        # data-ticker / data-name drive the find-a-stock box (full name here;
        # the visible name is truncated).
        body.append(
            f"<tr class='row-main'{toggle} style='cursor:pointer'"
            f" data-ticker='{_html_escape(r['ticker']).lower()}'"
            f" data-name='{_html_escape(r.get('name') or '').lower()}'>"
            f"<td>{r['rank']}</td>"
            f"<td><strong>{_html_escape(r['ticker'])}</strong></td>"
            f"<td>{_html_escape((r.get('name') or '')[:40])}</td>"
            f"<td>{sector_html}</td>"
            f"<td class='num'>{grade_html}</td>"
            f"<td class='{up_cls}'><strong>{upside}</strong></td>"
            f"<td class='num'>{price}</td>"
            f"<td class='num'>{target}</td>"
            f"<td class='num'>{_pct(r.get('alpha_1m'), 2)}</td>"
            f"<td class='num'>{_pct(r.get('p_outperform_1m'), 1, signed=False)}</td>"
            f"<td class='num'>{_pct(r.get('confidence'), 0, signed=False)}</td>"
            f"<td class='num'>{_html_escape(_news_cell(r))}</td>"
            f"<td class='num'>{_html_escape(_opinion_cell(r))}</td>"
            f"<td class='tf'>{_html_escape(_timeframe_marks(r['horizons']))}</td>"
            f"<td class='num'>{r.get('analysts') or 0}</td>"
            f"<td class='num'>{r.get('sources') or 0}</td>"
            "</tr>" + drawer
        )
    return f"<table class='top'>{head}<tbody>{''.join(body)}</tbody></table>"


def _data_health_html() -> str:
    """Crawl coverage, dormant symbols, recent failures and model calibration."""
    now = datetime.now(UTC).replace(tzinfo=None)
    today = date.today()
    with session_scope() as s:
        universe = s.query(func.count(Stock.ticker)).filter(Stock.in_universe.is_(True)).scalar() or 0
        intel_fresh = s.query(func.count(IntelSnapshot.ticker)).filter(
            IntelSnapshot.kind == "quote", IntelSnapshot.as_of >= now - timedelta(hours=36)
        ).scalar() or 0
        news_7d = s.query(func.count(NewsItem.id)).filter(
            NewsItem.published_at >= now - timedelta(days=7)
        ).scalar() or 0
        news_names = s.query(func.count(func.distinct(NewsItem.ticker))).filter(
            NewsItem.published_at >= now - timedelta(days=7)
        ).scalar() or 0
        sec_names = s.query(func.count(IntelSnapshot.ticker)).filter(
            IntelSnapshot.kind == "sec"
        ).scalar() or 0
        tgt_changes = s.query(func.count(AnalystAction.id)).filter(
            AnalystAction.date >= today - timedelta(days=30), AnalystAction.prior_target.isnot(None)
        ).scalar() or 0
        dormant = (
            s.query(RunLog).filter(RunLog.job == "universe.dormant").order_by(RunLog.id.desc()).first()
        )
        errors = (
            s.query(RunLog).filter(RunLog.status == "error",
                                   RunLog.started_at >= now - timedelta(hours=24))
            .order_by(RunLog.id.desc()).limit(8).all()
        )
        cal_date = s.execute(select(func.max(Calibration.as_of))).scalar()
        cal_rows = (
            s.query(Calibration).filter(Calibration.as_of == cal_date).all() if cal_date else []
        )
    items = [
        f"Yahoo intel refreshed in the last 36 h: <strong>{intel_fresh}</strong> of {universe} tickers",
        f"Headlines in the last 7 days: <strong>{news_7d}</strong> across {news_names} tickers",
        f"SEC filing stream covered: <strong>{sec_names}</strong> tickers",
        f"Analyst price-target changes captured (30 d): <strong>{tgt_changes}</strong>",
    ]
    if dormant is not None and dormant.error:
        items.append("Dormant symbols (no price ≥ 10 d — delisted/renamed, skipped by the crawl): "
                     + _html_escape(dormant.error.replace("dormant: ", "")))
    if errors:
        items.append("Crawl stages that failed in the last 24 h: " + ", ".join(
            _html_escape(f"{e.job} ({(e.error or '')[:80]})") for e in errors))
    else:
        items.append("No crawl stage failed in the last 24 h.")

    cal_html = ""
    if cal_rows:
        trs = []
        for c in sorted(cal_rows, key=lambda c: list(HORIZONS).index(c.horizon)
                        if c.horizon in HORIZONS else 9):
            p = _load_payload(c.payload)
            hic, ml = p.get("horizon_ic") or {}, p.get("ml") or {}
            fac = p.get("factors") or {}
            top = sorted(fac.items(), key=lambda kv: -abs(kv[1].get("weight", 0)))[:4]
            top_s = ", ".join(f"{f} {v.get('weight', 0):+.2f}" for f, v in top)
            real = hic.get("realised")
            real_s = (
                "—" if real is None
                else f"{real:+.3f} ± {hic.get('realised_se') or 0:.3f} (n={hic.get('n_dates', 0)})"
            )
            trs.append(
                f"<tr><td>{_html_escape(c.horizon)}</td>"
                f"<td class='num'>{hic.get('exante', 0):.3f}</td>"
                f"<td class='num'>{real_s}</td>"
                f"<td class='num'>{hic.get('posterior', 0):.3f}</td>"
                f"<td class='num'>{_pct(ml.get('weight', 0.0), 0, signed=False)}</td>"
                f"<td class='src'>{_html_escape(top_s)}</td></tr>"
            )
        cal_html = (
            "<table class='inner'><thead><tr><th>Horizon</th><th>Ex-ante IC</th>"
            "<th>Realised IC (this model)</th><th>Posterior IC</th><th>ML weight</th>"
            "<th>Largest factor weights</th></tr></thead><tbody>" + "".join(trs) + "</tbody></table>"
        )
    return (
        "<section><details><summary>Data health &amp; model calibration</summary>"
        "<ul class='health'>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
        + cal_html + "</details></section>"
    )


_METHOD_HTML = """
<section><details><summary>Methodology</summary>
<p>Every crawl gathers, per company: analyst consensus and its 1–3-month trend, price targets
(mean, median, dispersion), each firm's rating <em>and</em> price-target changes, EPS estimate
revisions and their breadth, the latest earnings surprise and next report date, valuation,
profitability and short interest, headlines from Yahoo Finance and Google News (scored with a
finance-specific lexicon), SEC filings (8-K red-flag items, late-filing notices, 13D activist
stakes, offerings), Form 4 insider trades and 13F institutional positions.</p>
<p>Each signal is rank-normalised to N(0,1) across the universe (partially sector-neutralised for
valuation, profitability, short interest and target upside). Each carries a literature prior for
its information coefficient (IC) per horizon, updated by the IC measured on this system's own
history (precision-weighted Bayes). Weights are Σ⁻¹·IC, so correlated signals share weight
instead of double-counting. A LightGBM ranker joins only in proportion to its purged
out-of-sample IC. The grade combines the four horizon scores weighted by their estimated skill
and correlation; α = IC·σ·z (Grinold) and P(beat) = Φ(IC·z) follow from the same model.
Missing data counts as neutral, never as a fabricated value; the confidence column shows how
much of the model each grade actually rests on.</p>
<p>Honest scale: realistic ICs are 0.02–0.08, so even an A+ carries a probability of beating the
universe of only slightly above 50 % per month. This is a research shortlist, not investment
advice.</p>
</details></section>
"""


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
    now = datetime.now(UTC).replace(tzinfo=None)
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
        "<p class='blurb'>One table across all four timeframes, ordered by the integrated grade. "
        "Upside is the consensus target vs the current price; α and P(beat) are the model's "
        "calibrated 1-month expectations; H/D/W/M shows which timeframes rank the name. "
        "Click a row for the evidence: drivers, analyst rating and target changes, headlines, "
        "estimates, events and filings.</p>"
        f"{_main_table_html(rows, by_h)}</section>"
    )
    try:
        sections.append(_data_health_html())
    except Exception as e:  # noqa: BLE001 — diagnostics must never break the page
        sections.append(f"<section><p class='src'>data health unavailable: {_html_escape(str(e))}</p></section>")
    sections.append(_METHOD_HTML)
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
  .finder {{ margin: 0.75rem 0 0.25rem 0; }}
  .finder input {{ width: 15rem; max-width: 60vw; padding: 0.3rem 0.55rem;
                    font-size: 0.9rem; font-family: inherit; border-radius: 5px;
                    border: 1px solid rgba(127,127,127,0.45); background: transparent;
                    color: inherit; }}
  .finder input:focus {{ outline: 2px solid var(--accent); outline-offset: 1px; }}
  .finder-msg {{ margin-left: 0.6rem; font-size: 0.85rem; color: #666; }}
  /* Search hit. Uses a left border + tinted background so it stays legible
     in both light and dark colour schemes, and outranks the .star row tint. */
  tr.row-main.hit td {{ background: rgba(43,108,176,0.18) !important; }}
  tr.row-main.hit td:first-child {{ box-shadow: inset 3px 0 0 var(--accent); }}
  .grade {{ display: inline-block; min-width: 1.9rem; text-align: center; padding: 0.05rem 0.35rem;
            border-radius: 4px; font-weight: 700; color: #fff; }}
  .grade.gA {{ background: #2f855a; }}
  .grade.gB {{ background: #2b6cb0; }}
  .grade.gC {{ background: #b7791f; }}
  .grade.gD {{ background: #9b2c2c; }}
  .tone.pos {{ color: #2f855a; }}
  .tone.neg {{ color: #c53030; }}
  .tone.neu {{ color: #a0aec0; }}
  ul.news {{ margin: 0.3rem 0 0.2rem 0; padding-left: 1.1rem; }}
  ul.news li {{ margin: 0.15rem 0; }}
  ul.health {{ padding-left: 1.2rem; }}
  div.blk {{ margin: 0.35rem 0 0.6rem 0; }}
  div.why {{ line-height: 1.55; }}
  @media (max-width: 760px) {{
    table.top {{ display: block; overflow-x: auto; white-space: nowrap; }}
  }}
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

<div class="finder">
  <input type="search" id="finder-input" autocomplete="off" spellcheck="false"
         placeholder="Find a stock — ticker or name"
         aria-label="Find a stock in the table by ticker or company name">
  <span class="finder-msg" id="finder-msg"></span>
</div>

{"".join(sections)}

<script>
(function () {{
  // Find-a-stock: highlight matching rows and scroll the first one into view.
  // Searches the whole table (all {len(rows)} rows), matching ticker OR
  // company name, case-insensitively, as a substring.
  var input = document.getElementById("finder-input");
  var msg = document.getElementById("finder-msg");
  if (!input || !msg) return;
  var rows = [].slice.call(document.querySelectorAll("tr.row-main"));

  function clear() {{
    for (var i = 0; i < rows.length; i++) rows[i].classList.remove("hit");
  }}

  function run() {{
    var q = input.value.trim().toLowerCase();
    clear();
    if (!q) {{ msg.textContent = ""; return; }}
    var hits = rows.filter(function (r) {{
      return (r.getAttribute("data-ticker") || "").indexOf(q) !== -1
          || (r.getAttribute("data-name") || "").indexOf(q) !== -1;
    }});
    if (!hits.length) {{
      msg.textContent = "Not in the top " + rows.length + ".";
      return;
    }}
    for (var i = 0; i < hits.length; i++) hits[i].classList.add("hit");
    msg.textContent = hits.length === 1
      ? "Rank " + (hits[0].cells[0] ? hits[0].cells[0].textContent.trim() : "?")
      : hits.length + " matches";
    // Only auto-scroll once the query is specific enough to be meaningful —
    // jumping the page on every single keystroke is disorienting.
    if (q.length >= 2) {{
      hits[0].scrollIntoView({{ behavior: "smooth", block: "center" }});
    }}
  }}

  input.addEventListener("input", run);
  input.addEventListener("search", run);   // fires on the native clear "x"
  input.addEventListener("keydown", function (e) {{
    if (e.key === "Escape") {{ input.value = ""; run(); }}
  }});
}})();
</script>
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
    generated = datetime.now(UTC).replace(tzinfo=None).strftime("%Y-%m-%d %H:%M UTC")
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
