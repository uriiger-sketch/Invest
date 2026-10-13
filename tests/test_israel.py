"""Israeli coverage: FX-normalised liquidity, the Israel board (graded on the
main distribution without moving it), Israeli-edition news, universe hygiene."""
from __future__ import annotations

import importlib.util
import json
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from sqlalchemy import select

from invest import fx
from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Grade, Holding13F, IntelSnapshot, Price, Score, Stock
from invest.universe import ISRAEL_NEWS_QUERIES, is_tase, israeli_tickers, static_universe

TODAY = date.today()


def _report():
    path = Path(__file__).resolve().parent.parent / "scripts" / "generate_report.py"
    spec = importlib.util.spec_from_file_location("generate_report_israel", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ----------------------------------------------------------------------- FX


def test_tel_aviv_quotes_are_agorot_and_convert_to_dollars():
    assert fx.listing_currency("POLI.TA") == ("ILS", 100.0)
    assert fx.listing_currency("PRX.AS") == ("EUR", 1.0)
    assert fx.listing_currency("AAPL") == ("USD", 1.0)
    rates = {"ILS": 4.0, "EUR": 0.8}
    assert fx.usd_per_quote_unit("POLI.TA", rates) == pytest.approx(1 / 400)
    assert fx.usd_per_quote_unit("PRX.AS", rates) == pytest.approx(1.25)
    assert fx.usd_per_quote_unit("AAPL", rates) == 1.0
    assert fx.to_local_price("POLI.TA", 7319.0) == pytest.approx(73.19)
    # An implausible stored rate falls back to the constant, never to 1:1.
    assert fx.usd_per_quote_unit("POLI.TA", {"ILS": 370.0}) == pytest.approx(
        1 / (100 * fx.FALLBACK_PER_USD["ILS"]))


def _fx_frame(ils: float, eur: float) -> pd.DataFrame:
    idx = pd.to_datetime([TODAY - timedelta(days=1), TODAY])
    cols = pd.MultiIndex.from_product([["ILS=X", "EUR=X"], ["Open", "High", "Low", "Close"]])
    data = [[ils] * 4 + [eur] * 4, [ils] * 4 + [eur] * 4]
    return pd.DataFrame(data, index=idx, columns=cols)


def test_fx_refresh_stores_plausible_rates_and_rejects_the_rest():
    stored = fx.refresh_rates(download=lambda syms, period: _fx_frame(3.65, 0.91))
    assert stored == {"ILS": 3.65, "EUR": 0.91}
    assert fx.load_rates() == {"ILS": 3.65, "EUR": 0.91}
    # A garbage quote (e.g. an agorot-scaled pair) is ignored; the last good rate stays.
    stored = fx.refresh_rates(download=lambda syms, period: _fx_frame(365.0, 0.90))
    assert stored == {"EUR": 0.90}
    assert fx.load_rates()["ILS"] == 3.65


def _prices(s, ticker: str, close: float, volume: float, days: int = 120, seed: int = 0) -> float:
    rng = np.random.default_rng(seed)
    p = close
    for i in range(days):
        p *= 1 + float(rng.normal(0, 0.01))
        s.add(Price(ticker=ticker, date=TODAY - timedelta(days=days - i), open=p, high=p,
                    low=p, close=p, adj_close=p, volume=volume))
    return p


def test_liquidity_of_a_tel_aviv_line_is_measured_in_dollars():
    from invest.pipeline.features import build_features

    with session_scope() as s:
        s.add(IntelSnapshot(ticker="ILS=X", kind="fx", as_of=pd.Timestamp.now().to_pydatetime(),
                            payload=json.dumps({"per_usd": 4.0})))
        for t in ("POLI.TA", "AAPL"):
            s.add(Stock(ticker=t, name=t, sector="Financials", in_universe=True))
        _prices(s, "POLI.TA", 7000.0, 1_000_000)
        _prices(s, "AAPL", 70.0, 1_000_000)
    f = build_features(["POLI.TA", "AAPL"]).set_index("ticker")
    ratio = f.loc["POLI.TA", "dollar_volume_20d"] / f.loc["AAPL", "dollar_volume_20d"]
    # Same price path, 100x the quoted price, but in agorot at 4 ILS/USD.
    assert ratio == pytest.approx(100 / 400, rel=1e-6)


# ---------------------------------------------------------------- the board


def _seed_main(tickers: list[str]) -> None:
    rng = np.random.default_rng(1)
    with session_scope() as s:
        for j, t in enumerate(tickers):
            s.add(Stock(ticker=t, name=t, sector="Technology", in_universe=True))
            last = _prices(s, t, 100.0, 2_000_000, seed=j)
            sb, b, h = (int(x) for x in rng.integers([8, 6, 2], [12, 10, 5]))
            s.add(Consensus(ticker=t, as_of_date=TODAY, source="yfinance", strong_buy=sb, buy=b,
                            hold=h, sell=0, strong_sell=0, mean_target=last * (1.1 + 0.01 * j),
                            high_target=last * 1.4, low_target=last * 1.05,
                            num_analysts=sb + b + h))
            for k in range(15):
                s.add(AnalystAction(ticker=t, firm=f"Firm-{k:02d}", action="upgrade",
                                    from_grade="Hold", to_grade="Buy",
                                    date=TODAY - timedelta(days=k + 1), source="yfinance"))
            for k in range(5):
                s.add(Holding13F(filer_cik=f"{k:010d}", filer_name=f"Filer-{k}", ticker=t,
                                 shares=1000, value_usd=1e6, quarter="2026Q1", filing_date=TODAY))


def _seed_tase(tickers: list[str]) -> None:
    """Liquid Tel Aviv lines with the thin coverage they really have (three
    analysts), so they can never pass the picks table's outlook gate."""
    with session_scope() as s:
        for j, t in enumerate(tickers):
            s.add(Stock(ticker=t, name=t, sector="Financials", in_universe=True))
            last = _prices(s, t, 7000.0, 1_000_000, seed=50 + j)
            s.add(Consensus(ticker=t, as_of_date=TODAY, source="yfinance", strong_buy=1, buy=2,
                            hold=0, sell=0, strong_sell=0, mean_target=last * 1.25,
                            high_target=last * 1.4, low_target=last * 1.1, num_analysts=3))


def _today(model) -> dict[str, tuple]:
    with session_scope() as s:
        if model is Score:
            rows = s.execute(select(Score.ticker, Score.horizon, Score.blended_score,
                                    Score.percentile).where(Score.as_of == TODAY)).all()
            return {(t, h): (b, p) for t, h, b, p in rows}
        rows = s.execute(select(Grade.ticker, Grade.grade_score, Grade.percentile,
                                Grade.letter, Grade.detail_json).where(Grade.as_of == TODAY)).all()
        return {t: (g, p, letter, json.loads(d)["board"]) for t, g, p, letter, d in rows}


def test_israel_board_grades_tel_aviv_names_without_moving_the_picks(monkeypatch):
    from invest.pipeline.rank import rank_all

    main = [f"TKR{i}" for i in range(20)]
    tase = ["POLI.TA", "LUMI.TA", "BEZQ.TA"]
    assert set(tase) <= israeli_tickers()
    _seed_main(main)
    _seed_tase(tase)

    monkeypatch.setenv("ISRAEL_BOARD", "false")
    rank_all(main + tase)
    scores_off, grades_off = _today(Score), _today(Grade)
    assert not set(tase) & set(grades_off), "board off: the gates exclude every TASE line"

    monkeypatch.setenv("ISRAEL_BOARD", "true")
    out = rank_all(main + tase)
    scores_on, grades_on = _today(Score), _today(Grade)

    # The picks universe is untouched: same Score rows, same values.
    assert scores_on.keys() == scores_off.keys()
    for k, v in scores_off.items():
        assert scores_on[k] == pytest.approx(v)
    for t, (g, p, letter, board) in grades_off.items():
        assert grades_on[t][:3] == (pytest.approx(g), pytest.approx(p), letter)
        assert board == grades_on[t][3] == "main"

    # Every TASE line is graded on the board, against the main distribution.
    main_g = np.sort([grades_on[t][0] for t in main])
    for t in tase:
        g, p, letter, board = grades_on[t]
        assert board == "israel"
        assert p == pytest.approx(np.searchsorted(main_g, g, side="right") / len(main_g))
    assert set(out.loc[~out["main"], "ticker"]) == set(tase)


def test_board_rows_never_shift_the_reference_distribution():
    """integrated_grades: R and percentiles come from the gated rows only, so
    an extreme board row changes nothing for them."""
    from invest.config import HORIZONS
    from invest.pipeline import grade

    rng = np.random.default_rng(3)
    tickers = [f"T{i}" for i in range(40)]
    feats = pd.DataFrame({"ticker": tickers + ["X.TA"], "vol_60d": 0.3})
    calib = grade.calibrate(feats, measured={h: {} for h in HORIZONS}, score_ics={})
    rows = []
    for h in HORIZONS:
        for t in tickers:
            rows.append({"ticker": t, "horizon": h, "blended_score": float(rng.normal()), "main": True})
    base = grade.integrated_grades(pd.DataFrame(rows), feats, calib).set_index("ticker")
    rows += [{"ticker": "X.TA", "horizon": h, "blended_score": 9.0 if i % 2 else -9.0, "main": False}
             for i, h in enumerate(HORIZONS)]
    both = grade.integrated_grades(pd.DataFrame(rows), feats, calib).set_index("ticker")
    for col in ("grade_score", "percentile"):
        pd.testing.assert_series_equal(base.loc[tickers, col], both.loc[tickers, col])
    assert both.loc["X.TA", "detail"]["board"] == "israel"
    assert all(d["board"] == "main" for d in both.loc[tickers, "detail"])


def test_israel_mask_skips_the_outlook_gate_but_keeps_data_and_liquidity_floors():
    from invest.pipeline.score import israel_mask

    f = pd.DataFrame({
        "ticker": ["POLI.TA", "LUMI.TA", "BEZQ.TA", "AAPL"],
        "dollar_volume_20d": [2e6, 1e5, 2e6, 9e9],
        "last_price_age_days": [1, 1, 30, 1],
        "price_history_days": [200, 200, 200, 200],
        "num_analysts": [0, 9, 9, 40],
    })
    assert israel_mask(f).tolist() == [True, False, False, False]


def test_focus_list_ignores_israel_board_grades():
    from invest.pipeline.ingest import focus_tickers

    with session_scope() as s:
        s.add(Grade(ticker="POLI.TA", as_of=TODAY, grade_score=3.0,
                    detail_json=json.dumps({"board": "israel"}, separators=(",", ":"))))
        s.add(Grade(ticker="TEVA", as_of=TODAY, grade_score=1.0,
                    detail_json=json.dumps({"board": "main"}, separators=(",", ":"))))
        s.add(Grade(ticker="OLD", as_of=TODAY, grade_score=0.5, detail_json=None))
    assert focus_tickers(10) == ["TEVA", "OLD"]


# --------------------------------------------------------------------- news


def test_israeli_edition_uses_curated_queries_and_names():
    from invest.sources.news_src import GoogleNewsSource

    src = GoogleNewsSource(edition="IL", queries=ISRAEL_NEWS_QUERIES)
    assert src.edition.endswith("ceid=IL:en")
    assert src._query("LUMI.TA", "Bank Leumi le-Israel B.M.") == '"Leumi" when:7d'
    elal = src.match_terms("ELAL.TA")
    assert elal.search("El Al posts record quarter") and elal.search("Israel's EL AL adds Tokyo")
    assert not elal.search("How to watch Al Nassr vs. Neftchi")
    assert not elal.search("Arkia cancels long-awaited direct route to Tokyo")
    assert src.match_terms("SKBN.TA").search("Shikun & Binui wins tender")
    assert not src.match_terms("LUMI.TA").search("Leumit health fund expands")
    # US-listed Israeli names keep the generic query and no strict filter.
    assert src._query("TEVA", "Teva Pharmaceutical") == '"Teva Pharmaceutical" OR "TEVA stock" when:7d'
    assert src.match_terms("TEVA") is None
    assert GoogleNewsSource().edition.endswith("ceid=US:en")


def test_strict_mode_keeps_only_headlines_naming_the_company(monkeypatch):
    from invest.models import NewsItem
    from invest.sources.news_src import GoogleNewsSource

    now = pd.Timestamp.now(tz="UTC").strftime("%a, %d %b %Y %H:%M:%S GMT")
    titles = ["El Al raises fares on Tokyo route - Globes",
              "How to watch Al Nassr vs. Neftchi - Yahoo Sports"]
    xml = ("<rss><channel>" + "".join(
        f"<item><title>{t}</title><pubDate>{now}</pubDate><link>https://x/{i}</link></item>"
        for i, t in enumerate(titles)) + "</channel></rss>").encode()
    src = GoogleNewsSource(edition="IL", queries=ISRAEL_NEWS_QUERIES)
    monkeypatch.setattr(src, "fetch", lambda t, n: xml)
    src.ingest(["ELAL.TA"], {"ELAL.TA": "El Al Israel Airlines Ltd."}, budget_seconds=30)
    with session_scope() as s:
        got = s.execute(select(NewsItem.title, NewsItem.relevance)).all()
    assert got == [("El Al raises fares on Tokyo route", 1.0)]


def test_israel_news_runs_for_every_israeli_name_tel_aviv_first(monkeypatch):
    from invest.pipeline import ingest
    from invest.sources import news_src

    seen: dict = {}

    def fake_run(self, tickers, budget_seconds=None, job="gnews.headlines"):
        seen.update(tickers=list(tickers), job=job, edition=self.edition)
        return 0

    monkeypatch.setattr(news_src.GoogleNewsSource, "run", fake_run)
    ingest._run_israel_news(["AAPL", "TEVA", "POLI.TA", "NICE", "LUMI.TA"])
    assert seen["tickers"] == ["LUMI.TA", "POLI.TA", "NICE", "TEVA"]
    assert seen["job"] == "gnews.israel" and seen["edition"].endswith("IL:en")


# ----------------------------------------------------------------- universe


def test_israeli_universe_is_clean():
    u = static_universe()
    assert len(u) == len(set(u))
    il = israeli_tickers()
    for dead in ("CYBR", "SPNS", "VRNT", "MGIC", "DELT.TA", "PZOL.TA", "ENLT.TA"):
        assert dead not in u
    # Every Tel Aviv line has a curated news query and vice versa.
    assert {t for t in il if is_tase(t)} == set(ISRAEL_NEWS_QUERIES)
    assert len(il) >= 90


# ------------------------------------------------------------------- report


def test_israel_report_shows_shekels_and_hides_insane_upside():
    rep = _report()
    with session_scope() as s:
        for t, name in (("POLI.TA", "Bank Hapoalim"), ("ENLV", "Enlivex")):
            s.add(Stock(ticker=t, name=name, sector="Financials", in_universe=True))
            s.add(Grade(ticker=t, as_of=TODAY, grade_score=1.0, letter="A", percentile=0.95,
                        confidence=0.7, alpha_1m=0.01, p_outperform_1m=0.52,
                        detail_json=json.dumps({"board": "israel"})))
        s.add(Price(ticker="POLI.TA", date=TODAY, close=7319.0))
        s.add(Consensus(ticker="POLI.TA", as_of_date=TODAY, source="yfinance", buy=3,
                        mean_target=9177.0))
        s.add(Price(ticker="ENLV", date=TODAY, close=0.25))
        s.add(Consensus(ticker="ENLV", as_of_date=TODAY, source="yfinance", buy=1, mean_target=80.0))
    rows, ungraded = rep.israel_rows()
    by = {r["ticker"]: r for r in rows}
    assert by["POLI.TA"]["last_close"] == pytest.approx(73.19)
    assert rep._money(by["POLI.TA"], "mean_target") == "₪91.77"
    assert by["POLI.TA"]["market"] == "TASE" and not by["POLI.TA"]["picks"]
    assert by["ENLV"]["upside_pct"] is None and rep._money(by["ENLV"], "mean_target") == "—"
    assert "LUMI.TA" in ungraded
    html = rep._israel_table_html(rows, ungraded)
    assert "₪73.19" in html and "row-il" in html and "data-ticker='poli.ta'" in html
    assert "## Israel" in rep._israel_table_md(rows, ungraded)
