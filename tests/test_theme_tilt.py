"""Tests for the technology / frontier-tech scoring tilt.

The tilt is a deliberate, small bias toward tech. These tests pin down the
two properties that make it safe: it is applied in the right ORDER relative
to the tilt tiers, and it is small enough to stay a tiebreaker rather than
override the quality gates.
"""
from __future__ import annotations

import contextlib
from datetime import date, timedelta

from invest.config import get_settings
from invest.db import session_scope
from invest.models import Consensus, Price, Stock
from invest.pipeline.rank import _theme_tilts


def _seed_stock(ticker: str, sector: str) -> None:
    with session_scope() as s:
        s.add(Stock(ticker=ticker, name=f"{ticker} Inc", sector=sector, in_universe=True))


def test_frontier_beats_tech_beats_nothing():
    """Three tiers, and frontier must NOT compound with the tech tilt — a
    quantum name gets `theme_tilt_frontier`, not frontier + tech."""
    settings = get_settings()
    _seed_stock("IONQ", "Technology")     # in FRONTIER_TECH
    _seed_stock("PLAINTECH", "Technology")  # tech sector only
    _seed_stock("BANKCO", "Financials")     # neither

    tilts = _theme_tilts(["IONQ", "PLAINTECH", "BANKCO"])
    assert tilts["IONQ"] == settings.theme_tilt_frontier
    assert tilts["PLAINTECH"] == settings.theme_tilt_tech
    assert tilts["BANKCO"] == 0.0
    # Explicitly not additive.
    assert tilts["IONQ"] != settings.theme_tilt_frontier + settings.theme_tilt_tech


def test_tilt_is_small_enough_to_stay_a_tiebreaker():
    """blended_score is in z units (pool spread roughly ±2). A tilt large
    enough to reorder genuinely different-quality names would be a thumb on
    the scale, not the "tiny bit of emphasis" this is meant to be."""
    settings = get_settings()
    assert 0 < settings.theme_tilt_tech <= 0.25
    assert settings.theme_tilt_tech <= settings.theme_tilt_frontier <= 0.35


def test_frontier_set_excludes_name_lookalikes_and_megacaps():
    """Membership is "primary business is quantum / AI infrastructure".
    Companies that merely have "Quantum" in their name, and diversified
    mega-caps with a quantum research arm, must stay out — tilting those
    would tilt the index rather than the theme."""
    from invest.universe import FRONTIER_TECH

    for lookalike in ("QMCO", "QSI"):
        assert lookalike not in FRONTIER_TECH
    for megacap in ("IBM", "GOOGL", "HON", "MSFT"):
        assert megacap not in FRONTIER_TECH
    # ...but the real pure plays are in.
    for real in ("IONQ", "RGTI", "QBTS", "QUBT", "ARQQ"):
        assert real in FRONTIER_TECH


def test_tilt_disabled_returns_empty_without_nan_risk(monkeypatch):
    """With the tilt switched off `_theme_tilts` returns {}, and
    `Series.map({})` yields all-NaN. rank_all must .fillna(0.0) or disabling
    the tilt would silently NaN out every blended_score. This asserts the
    end-to-end score survives, not just that the dict is empty."""
    import pandas as pd

    from invest.config import Settings

    orig = Settings.model_fields["theme_tilt_tech"].default
    assert orig  # sanity: enabled by default

    monkeypatch.setattr(
        "invest.pipeline.rank.get_settings",
        lambda: Settings(theme_tilt_tech=0.0, theme_tilt_frontier=0.0),
    )
    _seed_stock("ZZTOP", "Technology")
    assert _theme_tilts(["ZZTOP"]) == {}

    # The mapping pattern rank_all uses must not produce NaN.
    scores = pd.Series([1.5, -0.5], index=[0, 1])
    tickers = pd.Series(["ZZTOP", "OTHER"])
    tilt = tickers.map(_theme_tilts(["ZZTOP", "OTHER"])).fillna(0.0)
    out = scores + tilt
    assert out.notna().all(), "disabling the tilt must not NaN out blended_score"
    assert list(out) == [1.5, -0.5]


def test_tilt_cannot_rescue_a_gated_out_stock():
    """The tilt is applied to blended_score AFTER the quality gates have
    already filtered the pool, so a bearish or thinly-covered tech name is
    never in the ranking to be tilted in the first place. This is the
    property that keeps 'emphasis on tech' from becoming 'promote bad tech'.
    """
    from invest.pipeline.rank import rank_all

    price = 100.0
    with session_scope() as s:
        # A quantum name with an explicitly BEARISH consensus + negative upside.
        s.add(Stock(ticker="IONQ", name="IonQ Inc.", sector="Technology", in_universe=True))
        for i in range(120):
            s.add(Price(ticker="IONQ", date=date.today() - timedelta(days=120 - i),
                        close=price, adj_close=price, volume=5_000_000))
        s.add(Consensus(ticker="IONQ", as_of_date=date.today(), source="yfinance",
                        strong_buy=0, buy=1, hold=4, sell=10, strong_sell=6,
                        mean_target=price * 0.7, high_target=price,
                        low_target=price * 0.5, num_analysts=21))

    # A total gate wipeout raises by design (RankingProducedNothingError);
    # either way IONQ must not end up scored.
    with contextlib.suppress(Exception):
        rank_all(["IONQ"])

    from invest.models import Score

    with session_scope() as s:
        rows = s.query(Score).filter(Score.ticker == "IONQ").all()
    assert not rows, "a bearish stock must not be scored regardless of theme tilt"
