"""Single-request Yahoo intel: parsing, dead-symbol handling, rate governor."""
from __future__ import annotations

import json
from datetime import UTC, date, datetime, timedelta

import pytest

from invest.db import session_scope
from invest.models import AnalystAction, Consensus, IntelSnapshot, Stock
from invest.sources.base import CrawlAborted, RateGovernor
from invest.sources.yfinance_src import (
    NoDataError,
    YFinanceSource,
    actions_from_history,
    parse_quote_summary,
)


def _epoch(d: date) -> int:
    return int(datetime(d.year, d.month, d.day, tzinfo=UTC).timestamp())


TODAY = date.today()


def _qs() -> dict:
    return {
        "recommendationTrend": {"trend": [
            {"period": "0m", "strongBuy": 8, "buy": 12, "hold": 5, "sell": 1, "strongSell": 0},
            {"period": "-1m", "strongBuy": 6, "buy": 11, "hold": 8, "sell": 1, "strongSell": 0},
            {"period": "-3m", "strongBuy": 5, "buy": 10, "hold": 9, "sell": 2, "strongSell": 0},
        ]},
        "financialData": {
            "currentPrice": {"raw": 100.0, "fmt": "100.00"},
            "targetMeanPrice": 125.0, "targetMedianPrice": 124.0,
            "targetHighPrice": 160.0, "targetLowPrice": 90.0,
            "numberOfAnalystOpinions": 26, "recommendationMean": 1.9,
            "returnOnEquity": 0.21, "operatingMargins": 0.3, "debtToEquity": 45.0,
            "financialCurrency": "USD",
        },
        "upgradeDowngradeHistory": {"history": [
            {"epochGradeDate": _epoch(TODAY - timedelta(days=2)), "firm": "Goldman Sachs",
             "toGrade": "Buy", "fromGrade": "Buy", "action": "main",
             "priceTargetAction": "Raises", "currentPriceTarget": 140.0, "priorPriceTarget": 120.0},
            {"epochGradeDate": _epoch(TODAY - timedelta(days=5)), "firm": "Morgan Stanley",
             "toGrade": "Overweight", "fromGrade": "Equal-Weight", "action": "up",
             "priceTargetAction": "Raises", "currentPriceTarget": 135.0, "priorPriceTarget": 110.0},
            {"epochGradeDate": _epoch(TODAY - timedelta(days=400)), "firm": "Old Firm",
             "toGrade": "Sell", "fromGrade": "Buy", "action": "down"},
        ]},
        "earningsTrend": {"trend": [
            {"period": "0y", "growth": 0.12,
             "epsTrend": {"current": 5.5, "7daysAgo": 5.4, "30daysAgo": 5.0, "60daysAgo": 4.9,
                          "90daysAgo": 4.8},
             "epsRevisions": {"upLast7days": 3, "upLast30days": 10, "downLast30days": 2,
                              "downLast7Days": 0},
             "earningsEstimate": {"avg": 5.5, "numberOfAnalysts": 24}},
            {"period": "+1y", "epsTrend": {"current": 6.5, "30daysAgo": 6.2},
             "epsRevisions": {"upLast30days": 8, "downLast30days": 1},
             "earningsEstimate": {"numberOfAnalysts": 22}},
        ]},
        "earningsHistory": {"history": [
            {"quarter": _epoch(TODAY - timedelta(days=50)), "epsActual": 1.30, "epsEstimate": 1.20,
             "surprisePercent": 0.083},
            {"quarter": _epoch(TODAY - timedelta(days=140)), "epsActual": 1.10, "epsEstimate": 1.15},
        ]},
        "calendarEvents": {"earnings": {"earningsDate": [_epoch(TODAY + timedelta(days=20))]}},
        "defaultKeyStatistics": {"forwardEps": 6.5, "shortPercentOfFloat": 0.031,
                                 "52WeekChange": 0.35},
        "summaryDetail": {"forwardPE": 18.2, "fiftyTwoWeekHigh": 110.0, "fiftyTwoWeekLow": 70.0,
                          "marketCap": 5.0e10, "currency": "USD"},
        "price": {"longName": "Acme Corporation", "currency": "USD"},
        "summaryProfile": {"sector": "Technology", "industry": "Semiconductors"},
    }


def test_parse_quote_summary_extracts_every_intel_family():
    out = parse_quote_summary("ACME", _qs(), TODAY, TODAY - timedelta(days=90))

    c = out["consensus"]
    assert (c["strong_buy"], c["buy"], c["hold"], c["sell"], c["strong_sell"]) == (8, 12, 5, 1, 0)
    assert c["num_analysts"] == 26 and c["mean_target"] == 125.0  # {"raw":..} unwrapped elsewhere too

    acts = out["actions"]
    assert len(acts) == 2, "the 400-day-old action is outside the window"
    gs = next(a for a in acts if a["firm"] == "Goldman Sachs")
    assert gs["action"] == "reiterate"
    assert (gs["prior_target"], gs["target_price"], gs["target_action"]) == (120.0, 140.0, "raises")

    intel = out["intel"]
    assert intel["rec_trend"]["-1m"] == [6, 11, 8, 1, 0]
    assert intel["targets"]["yahoo_price"] == 100.0
    assert intel["eps"]["0y"]["d30"] == 5.0 and intel["eps"]["0y"]["up30"] == 10
    assert intel["surprises"][0]["act"] == 1.30
    assert intel["next_earnings"] == (TODAY + timedelta(days=20)).isoformat()
    assert intel["stats"]["short_float"] == 0.031 and intel["stats"]["fpe"] == 18.2
    assert out["stock"]["sector"] == "Technology" and out["stock"]["name"] == "Acme Corporation"


def test_store_bundle_writes_consensus_actions_intel_and_stock():
    src = YFinanceSource()
    w, acts = src._store_bundle({"ticker": "ACME", "qs": _qs(), "news": []},
                                TODAY, TODAY - timedelta(days=90), "Acme", 101.0)
    assert w >= 2 and len(acts) == 2
    with session_scope() as s:
        assert s.get(Consensus, ("ACME", TODAY, "yfinance")) is not None
        snap = s.get(IntelSnapshot, ("ACME", "quote"))
        assert json.loads(snap.payload)["our_close"] == 101.0
        assert s.get(Stock, "ACME").sector == "Technology"


def test_actions_upsert_keeps_target_changes():
    from invest.sources.base import upsert_analyst_actions

    rows = actions_from_history("ACME", _qs()["upgradeDowngradeHistory"]["history"],
                                TODAY - timedelta(days=90))
    upsert_analyst_actions(rows)
    upsert_analyst_actions(rows)  # re-crawl must not duplicate
    with session_scope() as s:
        stored = s.query(AnalystAction).filter(AnalystAction.ticker == "ACME").all()
    assert len(stored) == 2
    assert {a.prior_target for a in stored} == {120.0, 110.0}


def test_dead_symbol_is_not_retried(monkeypatch):
    """NoDataError (404 / delisted) must short-circuit — the old wrapper
    retried every failure with back-off, ~7 s per dead ticker per run."""
    calls = {"n": 0}

    def fake_qs(self, ticker):
        calls["n"] += 1
        raise NoDataError(ticker)

    monkeypatch.setattr(YFinanceSource, "_quote_summary", fake_qs)
    monkeypatch.setattr(YFinanceSource, "_news", lambda self, t: [])
    out = YFinanceSource()._fetch_bundle("DEAD", want_news=True)
    assert out["error"] == "no_data" and calls["n"] == 1


def test_rate_governor_pauses_then_aborts():
    gov = RateGovernor(threshold=2, cooldown=0.01, max_cooldowns=1)
    gov.on_rate_limit()
    gov.on_rate_limit()          # 1st cool-down
    assert not gov.aborted
    gov.before_request()         # sleeps the short cool-down, then proceeds
    gov.on_success()             # a success resets the streak
    gov.on_rate_limit()
    gov.on_rate_limit()          # 2nd cool-down > max -> abort
    assert gov.aborted
    with pytest.raises(CrawlAborted):
        gov.before_request()


def test_coverage_sweep_survives_mixed_outcomes(monkeypatch):
    """One crashed / rate-limited / dead ticker must never stop the sweep."""
    from invest.sources.base import RateLimitedError

    def fake_qs(self, ticker):
        if ticker == "DEAD":
            raise NoDataError(ticker)
        if ticker == "SLOW":
            raise RateLimitedError("429")
        if ticker == "BOOM":
            raise RuntimeError("unexpected")
        return _qs()

    monkeypatch.setattr(YFinanceSource, "_quote_summary", fake_qs)
    monkeypatch.setattr(YFinanceSource, "_news", lambda self, t: [])
    src = YFinanceSource()
    written, processed = src.ingest_coverage(["ACME", "DEAD", "SLOW", "BOOM", "ZETA"], want_news=True)
    assert processed == 3  # ACME, ZETA stored; DEAD processed (news only)
    with session_scope() as s:
        assert s.get(Consensus, ("ZETA", TODAY, "yfinance")) is not None
    assert src.last_stats.get("rate_limited") == 1
    assert src.last_stats.get("crashed") == 1


def test_quote_summary_request_paths(monkeypatch):
    """Success, 404 (dead symbol, no retry) and an internal-API signature
    change (switches the run to the public-property fallback)."""
    from yfinance.data import YfData

    calls = []

    class _Resp:
        status_code = 404

    class _HTTPError(Exception):
        response = _Resp()

    def ok(self, url, params=None, timeout=30):
        calls.append((url, params["modules"]))
        return {"quoteSummary": {"result": [_qs()]}}

    monkeypatch.setattr(YfData, "get_raw_json", ok)
    src = YFinanceSource()
    res = src._quote_summary("ACME")
    assert res["financialData"]["targetMeanPrice"] == 125.0
    assert calls[0][0].endswith("/quoteSummary/ACME") and "earningsTrend" in calls[0][1]

    def not_found(self, url, params=None, timeout=30):
        calls.append("404")
        raise _HTTPError("404")

    monkeypatch.setattr(YfData, "get_raw_json", not_found)
    n = len(calls)
    with pytest.raises(NoDataError):
        src._quote_summary("GONE")
    assert len(calls) == n + 1, "a 404 is final — never retried"

    def new_signature(self, url):  # e.g. a future yfinance drops kwargs
        raise AssertionError("unreachable")

    monkeypatch.setattr(YfData, "get_raw_json", new_signature)
    monkeypatch.setattr(YFinanceSource, "_quote_summary_fallback", lambda self, t: {"fallback": t})
    assert src._quote_summary("ACME") == {"fallback": "ACME"}
    assert src._internal_api_broken
