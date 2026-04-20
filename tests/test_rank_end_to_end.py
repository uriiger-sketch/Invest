"""End-to-end smoke test: seed the DB with prices + consensus, run rank_all,
and verify we get a top-N list per horizon with finite blended scores.
"""
from __future__ import annotations

from datetime import date, timedelta

import numpy as np

from invest.db import session_scope
from invest.models import Consensus, Price, Stock
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
            # Consensus snapshot as of today
            s.add(
                Consensus(
                    ticker=t,
                    as_of_date=today,
                    source="yfinance",
                    strong_buy=int(rng.integers(0, 10)),
                    buy=int(rng.integers(0, 10)),
                    hold=int(rng.integers(0, 10)),
                    sell=int(rng.integers(0, 5)),
                    strong_sell=int(rng.integers(0, 5)),
                    mean_target=price * float(rng.uniform(1.05, 1.25)),
                    high_target=price * 1.3,
                    low_target=price * 0.9,
                    num_analysts=20,
                )
            )


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
