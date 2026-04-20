from __future__ import annotations

from datetime import date, timedelta

import numpy as np

from invest.db import session_scope
from invest.models import AnalystAction, Consensus, Price, Stock
from invest.pipeline.features import build_features


def _seed_prices(ticker: str, days: int = 120) -> None:
    today = date.today()
    rng = np.random.default_rng(ord(ticker[-1]))
    with session_scope() as s:
        s.add(Stock(ticker=ticker, name=ticker, sector="Tech", in_universe=True))
        price = 100.0
        for i in range(days):
            d = today - timedelta(days=days - i)
            price *= 1 + float(rng.normal(0, 0.01))
            s.add(
                Price(
                    ticker=ticker,
                    date=d,
                    close=price,
                    adj_close=price,
                    volume=1_000_000,
                )
            )


def test_build_features_emits_one_row_per_ticker_with_zero_fill():
    _seed_prices("AAA")
    _seed_prices("BBB")
    df = build_features(["AAA", "BBB"])
    assert len(df) == 2
    # Every feature column must exist and be numeric.
    for col in ("consensus_z", "upside_z", "rating_mom_7d", "risk_penalty", "price_mom_21d"):
        assert col in df.columns
        assert df[col].notna().all()
    # Volatility should be positive magnitude -> risk_penalty negative.
    assert (df["risk_penalty"] <= 0).all()


def test_build_features_picks_up_consensus_and_actions():
    _seed_prices("AAA")
    today = date.today()
    with session_scope() as s:
        s.add(
            Consensus(
                ticker="AAA",
                as_of_date=today,
                source="yfinance",
                strong_buy=10,
                buy=5,
                hold=2,
                sell=0,
                strong_sell=0,
                mean_target=150.0,
                high_target=170.0,
                low_target=140.0,
                num_analysts=17,
            )
        )
        s.add(
            AnalystAction(
                ticker="AAA",
                firm="Goldman Sachs",
                action="upgrade",
                from_grade="Hold",
                to_grade="Buy",
                date=today - timedelta(days=3),
                source="yfinance",
            )
        )

    df = build_features(["AAA"])
    row = df.iloc[0]
    assert row["consensus_z"] > 0
    # Most recent close in seeded path is near 100-110; target 150 gives positive upside.
    assert row["upside_z"] > 0
    assert row["rating_mom_7d"] >= 1
