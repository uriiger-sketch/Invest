"""The calibrated grading model: statistics, weights, grades."""
from __future__ import annotations

import math
from datetime import date, timedelta

import numpy as np
import pandas as pd
import pytest

from invest.config import FEATURE_NAMES, HORIZONS, PRIOR_IC, get_settings
from invest.pipeline import grade
from invest.pipeline.score import rank_gauss


def test_posterior_is_precision_weighted():
    m, sd = grade.posterior(0.02, 0.02, 0.06, 0.02)  # equal precision -> midpoint
    assert m == pytest.approx(0.04) and sd == pytest.approx(0.02 / math.sqrt(2))
    m, _ = grade.posterior(0.02, 0.02, 0.50, 5.0)    # useless data -> prior
    assert m == pytest.approx(0.02, abs=1e-4)
    assert grade.posterior(0.01, 0.02, None, None) == (0.01, 0.02)


def test_ic_standard_error_accounts_for_overlapping_windows():
    ics = list(np.random.default_rng(0).normal(0.05, 0.1, 60))
    _, se_1d, _ = grade.ic_summary(ics, 1)
    _, se_20d, _ = grade.ic_summary(ics, 20)
    # 60 overlapping 20-day windows hold ~3 independent observations, not 60.
    assert se_20d == pytest.approx(se_1d * math.sqrt(20), rel=1e-6)
    # A suspiciously calm short series cannot claim more precision than the floor.
    _, se_flat, _ = grade.ic_summary([0.05, 0.051, 0.049], 1)
    assert se_flat >= 0.06 / math.sqrt(3) - 1e-12


def test_rank_gauss_is_bounded_tie_aware_and_nan_preserving():
    s = pd.Series([1.0, 2.0, 2.0, 3.0, 1e9, np.nan])
    z = rank_gauss(s)
    assert pd.isna(z.iloc[5])
    assert z.iloc[1] == z.iloc[2], "ties share the mid-rank"
    assert z.iloc[4] < 2.0, "a broken outlier is just the top rank"
    # Without ties the transform is exactly symmetric: mean 0, median -> 0.
    z2 = rank_gauss(pd.Series([1.0, 2.0, 3.0, 4.0, 1e9]))
    assert abs(z2.mean()) < 1e-12 and z2.iloc[2] == pytest.approx(0.0)
    assert (rank_gauss(pd.Series([5.0, 5.0, 5.0])) == 0).all()


def _features(n: int = 60, seed: int = 1) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"ticker": [f"T{i:02d}" for i in range(n)], "dollar_volume_20d": 1e9,
                       "last_price_age_days": 1, "price_history_days": 200,
                       "num_analysts": 20, "total_sources_count": 40, "vol_60d": 0.3,
                       "sector": "Technology"})
    for c in FEATURE_NAMES:
        df[c] = rng.normal(size=n)
    df["consensus_z"] = rng.uniform(0.1, 1.0, n)
    df["upside_z"] = rng.uniform(0.05, 0.5, n)
    return df


def test_weights_follow_prior_ics_when_no_history():
    calib = grade.calibrate(_features(), measured={h: {} for h in HORIZONS}, score_ics={})
    for h in HORIZONS:
        w = calib.weights[h]
        assert abs(sum(abs(v) for v in w.values()) - 1) < 1e-9
        # Signs follow the priors for clearly signed signals.
        if PRIOR_IC[h]["short_interest"] < 0:
            assert w["short_interest"] < 0
        assert w["eps_revision"] > 0
    assert calib.horizon_ic["monthly"]["posterior"] > 0


def test_correlated_duplicate_signals_share_weight():
    """Σ⁻¹·IC: two copies of the same information must not count double."""
    df = _features(200)
    base = grade.calibrate(df, measured={h: {} for h in HORIZONS}, score_ics={}).weights["monthly"]
    dup = df.copy()
    dup["value"] = dup["upside_z"]  # make 'value' a copy of upside
    w = grade.calibrate(dup, measured={h: {} for h in HORIZONS}, score_ics={}).weights["monthly"]
    rel_base = base["upside_z"] + base["value"]
    rel_dup = w["upside_z"] + w["value"]
    assert rel_dup < rel_base, "duplicated information must get less combined weight"


def test_measured_ic_moves_the_weight():
    measured = {h: {} for h in HORIZONS}
    n = get_settings().min_ic_dates + 30
    measured["weekly"]["news_sentiment"] = (-0.10, 0.01, n)  # strong, precise, wrong-signed
    calib = grade.calibrate(_features(), measured=measured, score_ics={})
    assert calib.factor_ic["weekly"]["news_sentiment"]["posterior"] < 0
    assert calib.weights["weekly"]["news_sentiment"] < 0


def test_ml_blend_rule():
    a = pd.Series(np.random.default_rng(0).normal(size=100))
    b = a * 0.5 + pd.Series(np.random.default_rng(1).normal(size=100))
    assert grade.ml_blend(a, b, None, 0.03)[:2] == (1.0, 0.0), "no model -> composite only"
    assert grade.ml_blend(a, b, {"val_ic": -0.05, "val_ic_se": 0.01}, 0.03)[1] == 0.0
    _, w_ml, info = grade.ml_blend(a, b, {"val_ic": 0.30, "val_ic_se": 0.001}, 0.01)
    assert w_ml == pytest.approx(get_settings().blend_ml_weight), "capped"
    assert info["posterior"] > 0


def test_factor_ic_measurement_recovers_a_planted_signal():
    """Synthetic history where one feature truly predicts the next-day
    return: the measured IC must come out clearly positive."""
    from invest.db import session_scope
    from invest.models import Price
    from invest.pipeline.features import persist_feature_snapshot

    rng = np.random.default_rng(3)
    tickers = [f"P{i:02d}" for i in range(40)]
    days = 40
    start = date.today() - timedelta(days=days + 5)
    signal = {t: rng.normal(size=days + 2) for t in tickers}
    closes = {t: [100.0] for t in tickers}
    for d in range(days + 1):
        for t in tickers:
            r = 0.01 * signal[t][d] + 0.01 * rng.normal()
            closes[t].append(closes[t][-1] * (1 + r))
    with session_scope() as s:
        for t in tickers:
            for d, c in enumerate(closes[t]):
                s.add(Price(ticker=t, date=start + timedelta(days=d), close=c, adj_close=c, volume=1e6))
    for d in range(days):
        frame = pd.DataFrame({"ticker": tickers})
        for f in FEATURE_NAMES:
            frame[f] = np.nan
        frame["news_sentiment"] = [signal[t][d] for t in tickers]
        persist_feature_snapshot(frame, as_of=start + timedelta(days=d))
    res = grade.measure_factor_ics(lookback_days=days + 10)
    m, se, n = res["hours"]["news_sentiment"]
    assert n >= 30 and m > 0.4 and m / se > 5


def test_realised_score_ic_only_counts_the_current_model_version():
    import json

    from invest.db import session_scope
    from invest.models import Calibration, Score

    d_old, d_new = date.today() - timedelta(days=10), date.today() - timedelta(days=5)
    with session_scope() as s:
        s.add(Score(ticker="X", horizon="hours", as_of=d_old, blended_score=1.0))
        s.add(Score(ticker="X", horizon="hours", as_of=d_new, blended_score=1.0))
        s.add(Calibration(as_of=d_new, horizon="hours",
                          payload=json.dumps({"model_version": grade.GRADING_MODEL_VERSION})))
    assert grade._model_dates(grade.GRADING_MODEL_VERSION) == {d_new}


def test_integrated_grade_is_standardised_and_consistent():
    df = _features(80)
    calib = grade.calibrate(df, measured={h: {} for h in HORIZONS}, score_ics={})
    rng = np.random.default_rng(5)
    common = rng.normal(size=80)
    rows = []
    for h in HORIZONS:
        s = common + 0.5 * rng.normal(size=80)
        s = (s - s.mean()) / s.std()
        rows += [{"ticker": t, "horizon": h, "blended_score": v} for t, v in zip(df["ticker"], s)]
    g = grade.integrated_grades(pd.DataFrame(rows), df, calib)
    assert len(g) == 80
    assert abs(g["grade_score"].std() - 1) < 0.25, "G is ~N(0,1) across the gated pool"
    top, bottom = g.nlargest(1, "grade_score").iloc[0], g.nsmallest(1, "grade_score").iloc[0]
    assert top["letter"] == "A+" and bottom["letter"] == "D"
    assert top["p_outperform_1m"] > 0.5 > bottom["p_outperform_1m"]
    assert top["alpha_1m"] > 0 > bottom["alpha_1m"]
    assert 0 < top["confidence"] <= 1
    assert grade.letter_for(0.99) == "A+" and grade.letter_for(0.5) == "B-"
