"""End-to-end smoke test: seed the DB with prices + consensus, run rank_all,
and verify we get a top-N list per horizon with finite blended scores.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np

from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Holding13F, Price, Stock
from invest.pipeline.rank import rank_all, top_n


def _seed(tickers: list[str], days: int = 120) -> None:
    today = date.today()
    rng = np.random.default_rng(0)
    with session_scope() as s:
        for t in tickers:
            s.add(Stock(ticker=t, name=t, sector="Tech", in_universe=True))
        for t in tickers:
            price = 100.0
            for i in range(days):
                d = today - timedelta(days=days - i)
                price *= 1 + float(rng.normal(0, 0.01))
                s.add(
                    Price(
                        ticker=t,
                        date=d,
                        open=price,
                        high=price * 1.01,
                        low=price * 0.99,
                        close=price,
                        adj_close=price,
                        volume=2_000_000,
                    )
                )
            # Consensus snapshot as of today — strictly bullish + ≥ 4 % upside
            # so the quality gate is satisfied.
            sb = int(rng.integers(8, 12))
            b = int(rng.integers(6, 10))
            h = int(rng.integers(2, 5))
            s.add(
                Consensus(
                    ticker=t,
                    as_of_date=today,
                    source="yfinance",
                    strong_buy=sb,
                    buy=b,
                    hold=h,
                    sell=0,
                    strong_sell=0,
                    mean_target=price * 1.20,
                    high_target=price * 1.30,
                    low_target=price * 1.10,
                    num_analysts=sb + b + h,
                )
            )
            # Seed enough distinct contributors so the ≥ 50-sources gate
            # is satisfied: 30 sell-side firms + 25 13F filers.
            for k in range(30):
                s.add(AnalystAction(
                    ticker=t, firm=f"Firm-{k:02d}", action="upgrade",
                    from_grade="Hold", to_grade="Buy",
                    date=today - timedelta(days=(k % 80)), source="yfinance",
                ))
            for k in range(25):
                s.add(Holding13F(
                    filer_cik=f"{k:010d}", filer_name=f"Filer-{k:02d}",
                    ticker=t, shares=1000, value_usd=1e6,
                    quarter="2026Q1", filing_date=today,
                ))


def test_rank_all_produces_top_n_per_horizon():
    tickers = [f"TKR{i}" for i in range(20)]
    _seed(tickers)

    df = rank_all(tickers)
    assert not df.empty
    # blended_score is finite for every row
    assert df["blended_score"].notna().all()
    assert np.isfinite(df["blended_score"]).all()

    tops = top_n(n=5)
    for h, sub in tops.items():
        assert not sub.empty, f"no rows for horizon {h}"
        assert len(sub) <= 5
        # ranks must be consecutive starting from 1
        assert list(sub["rank"]) == list(range(1, len(sub) + 1))
