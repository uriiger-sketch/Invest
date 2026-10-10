"""EDGAR filing stream + 13F periods, ML validation metadata, report contracts."""
from __future__ import annotations

import importlib.util
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

from invest.db import session_scope
from invest.sources.edgar_src import EdgarSource

TODAY = date.today()


def _report():
    path = Path(__file__).resolve().parent.parent / "scripts" / "generate_report.py"
    spec = importlib.util.spec_from_file_location("generate_report_edgar_ml", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------ EDGAR


def test_issuer_filings_keep_forms_of_interest_in_window():
    d = (TODAY - timedelta(days=10)).isoformat()
    old = (TODAY - timedelta(days=500)).isoformat()
    subs = {"filings": {"recent": {
        "form": ["8-K", "4", "SC 13D", "10-Q", "8-K", "S-3"],
        "filingDate": [d, d, d, d, old, d],
        "accessionNumber": ["a1", "a2", "a3", "a4", "a5", "a6"],
        "reportDate": [d, "", "", d, old, ""],
        "items": ["2.02,9.01", "", "", "", "4.02", ""],
        "primaryDocDescription": ["8-K", "", "SC 13D", "10-Q", "", "S-3"],
    }}}
    rows = EdgarSource.parse_issuer_filings("ACME", subs, TODAY - timedelta(days=200))
    assert [r["form"] for r in rows] == ["8-K", "SC 13D", "10-Q", "S-3"]
    assert rows[0]["items"] == "2.02,9.01"


def test_recent_13f_prefers_originals_and_uses_period_of_report(monkeypatch):
    src = EdgarSource()
    subs = {"filings": {"recent": {
        "form": ["13F-HR/A", "13F-HR", "13F-HR", "4"],
        "filingDate": ["2026-09-01", "2026-08-14", "2026-05-15", "2026-08-01"],
        "accessionNumber": ["0001-26-3", "0001-26-2", "0001-26-1", "0001-26-0"],
        "reportDate": ["2026-06-30", "2026-06-30", "2026-03-31", ""],
    }, "files": []}}
    monkeypatch.setattr(src, "_filer_submissions", lambda cik: subs)
    got = src._recent_13f_filings("0000000001")
    assert got == [
        ("000126" + "2", date(2026, 8, 14), date(2026, 6, 30)),
        ("000126" + "1", date(2026, 5, 15), date(2026, 3, 31)),
    ], "the original Q2 13F-HR wins over its later amendment"
    assert src._quarter_label(got[0][2]) == "2026Q2"
    assert EdgarSource._period_before(date(2026, 2, 14)) == date(2025, 12, 31)


def test_13f_values_are_dollars_after_2023(monkeypatch):
    from invest.models import Holding13F, Stock

    with session_scope() as s:
        s.add(Stock(ticker="AMZN", name="Amazon.com, Inc.", cusip="023135106", in_universe=True))
    src = EdgarSource()
    monkeypatch.setattr("invest.sources.edgar_src.TOP_FILERS", (("F", "0000000009"),))
    monkeypatch.setattr(src, "_recent_13f_filings",
                        lambda cik: [("ACC", date(2026, 8, 14), date(2026, 6, 30))])
    monkeypatch.setattr(src, "_download_13f_infotable", lambda cik, acc: b"<x/>")
    # Parser multiplies <value> by 1000 (pre-2023 convention): 5,000,000 -> 5e9.
    monkeypatch.setattr(src, "_parse_infotable", lambda xml: [
        {"cusip": "023135106", "name_of_issuer": "AMAZON COM INC", "shares": 10.0, "value_usd": 5e9}])
    src.ingest_13f(["AMZN"])
    with session_scope() as s:
        h = s.query(Holding13F).one()
    assert h.value_usd == 5e6 and h.quarter == "2026Q2"


# --------------------------------------------------------------------- ML


def test_model_without_matching_metadata_is_ignored(tmp_path, monkeypatch):
    from invest.pipeline import ml_rank

    monkeypatch.setattr(ml_rank, "MODEL_DIR", tmp_path)
    (tmp_path / "lgb_daily.txt").write_text("not a model")
    assert ml_rank._load_model("daily") is None, "no metadata -> never used"
    (tmp_path / "lgb_daily.json").write_text(json.dumps({"features": ["old", "list"]}))
    assert ml_rank.model_meta("daily") is None, "trained on a different feature list"


def test_training_uses_purged_split_and_records_oos_ic(tmp_path, monkeypatch):
    from invest.config import FEATURE_NAMES
    from invest.pipeline import ml_rank

    monkeypatch.setattr(ml_rank, "MODEL_DIR", tmp_path)
    monkeypatch.setattr(ml_rank, "COLD_START_MIN_DAYS", 1)
    rng = np.random.default_rng(0)
    dates = pd.date_range(end=pd.Timestamp(TODAY), periods=60, freq="D")
    rows = []
    for d in dates:
        x = rng.normal(size=40)
        for i in range(40):
            rec = {"ticker": f"T{i}", "date": d, "fwd": 0.02 * x[i] + 0.01 * rng.normal()}
            rec.update({f: np.nan for f in FEATURE_NAMES})
            rec["eps_revision"] = x[i]
            rows.append(rec)
    panel = pd.DataFrame(rows)
    panel["y"] = ml_rank._gauss_rank_by_date(panel, "fwd")
    monkeypatch.setattr(ml_rank, "_labelled_panel", lambda h: panel)
    path = ml_rank.train("daily")
    assert path is not None
    meta = ml_rank.model_meta("daily")
    assert meta["embargo_dates"] == 5
    assert meta["val_ic"] > 0.3, "a real signal must show up out-of-sample"
    assert meta["val_ic_se"] > 0


# ----------------------------------------------------------------- report


def test_main_table_orders_by_integrated_grade():
    from invest.models import Grade

    with session_scope() as s:
        s.add(Grade(ticker="LOWPCT", as_of=TODAY, grade_score=2.5, letter="A+", percentile=1.0,
                    confidence=0.8, alpha_1m=0.01, p_outperform_1m=0.53))
        s.add(Grade(ticker="HIGHPCT", as_of=TODAY, grade_score=-0.5, letter="C", percentile=0.3,
                    confidence=0.8, alpha_1m=-0.002, p_outperform_1m=0.49))
    by_h = {
        "hours": [
            {"ticker": "HIGHPCT", "name": "H", "sector": "Tech", "percentile": 1.0, "rank": 1},
            {"ticker": "LOWPCT", "name": "L", "sector": "Tech", "percentile": 0.5, "rank": 2},
        ],
    }
    rows = _report().main_table_rows(by_h)
    assert [r["ticker"] for r in rows] == ["LOWPCT", "HIGHPCT"], (
        "the integrated grade, not the top-list percentile sum, decides the order"
    )
    assert rows[0]["letter"] == "A+"


def test_drawer_escapes_headlines_and_drops_unsafe_urls():
    rows = [{
        "rank": 1, "ticker": "EVL", "name": "Evil Co", "sector": "Tech", "horizons": ["hours"],
        "news": [{"title": "<img src=x onerror=alert(1)> beats estimates", "publisher": "<b>x</b>",
                  "url": "javascript:alert(1)", "at": None, "sentiment": 0.5}],
    }]
    html = _report()._main_table_html(rows, {})
    assert "<img src=x" not in html and "&lt;img" in html
    assert "javascript:" not in html
    assert "<b>x</b>" not in html
