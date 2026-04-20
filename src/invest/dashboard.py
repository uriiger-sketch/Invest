"""Streamlit dashboard. Four pages: Top 20, Drill-down, Sources & freshness, Methodology."""
from __future__ import annotations

from datetime import date, datetime, timedelta

import pandas as pd
import plotly.express as px
import streamlit as st
from sqlalchemy import desc, select

from invest.config import FEATURE_NAMES, HORIZONS, WEIGHTS, get_settings
from invest.db import session_scope
from invest.models import (
    AnalystAction,
    Consensus,
    Holding13F,
    InsiderTrade,
    Price,
    RunLog,
    Score,
    Stock,
)

st.set_page_config(page_title="Invest — Top 20", layout="wide")


@st.cache_data(ttl=60)
def _latest_score_as_of() -> date | None:
    with session_scope() as s:
        row = s.execute(select(Score.as_of).order_by(desc(Score.as_of)).limit(1)).first()
    return row[0] if row else None


@st.cache_data(ttl=60)
def _top_n(horizon: str, n: int, as_of: date) -> pd.DataFrame:
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
    return pd.DataFrame(
        [
            {
                "rank": i + 1,
                "ticker": r.ticker,
                "name": r.name,
                "sector": r.sector,
                "blended": r.blended_score,
                "composite": r.composite_score,
                "ml": r.ml_score,
                "percentile": r.percentile,
            }
            for i, r in enumerate(rows)
        ]
    )


@st.cache_data(ttl=60)
def _run_log(limit: int = 100) -> pd.DataFrame:
    with session_scope() as s:
        rows = (
            s.query(RunLog)
            .order_by(RunLog.started_at.desc())
            .limit(limit)
            .all()
        )
    return pd.DataFrame(
        [
            {
                "id": r.id,
                "job": r.job,
                "started_at": r.started_at,
                "finished_at": r.finished_at,
                "status": r.status,
                "rows": r.rows_written,
                "error": (r.error or "")[:200],
            }
            for r in rows
        ]
    )


@st.cache_data(ttl=60)
def _all_tickers() -> list[str]:
    with session_scope() as s:
        rows = s.execute(select(Stock.ticker).order_by(Stock.ticker)).all()
    return [r[0] for r in rows]


@st.cache_data(ttl=60)
def _prices_for(ticker: str, days: int = 180) -> pd.DataFrame:
    cutoff = date.today() - timedelta(days=days)
    with session_scope() as s:
        rows = (
            s.query(Price)
            .filter(Price.ticker == ticker, Price.date >= cutoff)
            .order_by(Price.date)
            .all()
        )
    return pd.DataFrame([{"date": r.date, "close": r.close} for r in rows])


@st.cache_data(ttl=60)
def _consensus_history(ticker: str) -> pd.DataFrame:
    with session_scope() as s:
        rows = (
            s.query(Consensus)
            .filter(Consensus.ticker == ticker)
            .order_by(Consensus.as_of_date)
            .all()
        )
    return pd.DataFrame(
        [
            {
                "as_of": r.as_of_date,
                "source": r.source,
                "strong_buy": r.strong_buy or 0,
                "buy": r.buy or 0,
                "hold": r.hold or 0,
                "sell": r.sell or 0,
                "strong_sell": r.strong_sell or 0,
                "mean_target": r.mean_target,
                "num_analysts": r.num_analysts,
            }
            for r in rows
        ]
    )


@st.cache_data(ttl=60)
def _actions(ticker: str) -> pd.DataFrame:
    with session_scope() as s:
        rows = (
            s.query(AnalystAction)
            .filter(AnalystAction.ticker == ticker)
            .order_by(AnalystAction.date.desc())
            .limit(60)
            .all()
        )
    return pd.DataFrame(
        [
            {
                "date": r.date,
                "firm": r.firm,
                "action": r.action,
                "from": r.from_grade,
                "to": r.to_grade,
                "target": r.target_price,
                "source": r.source,
            }
            for r in rows
        ]
    )


@st.cache_data(ttl=60)
def _insider_trades(ticker: str) -> pd.DataFrame:
    with session_scope() as s:
        rows = (
            s.query(InsiderTrade)
            .filter(InsiderTrade.ticker == ticker)
            .order_by(InsiderTrade.date.desc())
            .limit(100)
            .all()
        )
    return pd.DataFrame(
        [
            {
                "date": r.date,
                "filer": r.filer,
                "action": r.action,
                "shares": r.shares,
                "price": r.price,
            }
            for r in rows
        ]
    )


@st.cache_data(ttl=60)
def _13f_flow(ticker: str) -> pd.DataFrame:
    with session_scope() as s:
        rows = s.query(Holding13F).filter(Holding13F.ticker == ticker).all()
    if not rows:
        return pd.DataFrame()
    df = pd.DataFrame(
        [{"quarter": r.quarter, "filer": r.filer_name, "shares": r.shares or 0} for r in rows]
    )
    agg = df.groupby("quarter", as_index=False)["shares"].sum().sort_values("quarter")
    return agg


# -------------------------- sidebar --------------------------

st.sidebar.title("Invest")
page = st.sidebar.radio(
    "Page",
    ("Top 20", "Ticker drill-down", "Sources & freshness", "Methodology"),
)
settings = get_settings()
as_of = _latest_score_as_of()
if as_of is None:
    st.sidebar.warning("No scores yet. Run `make ingest && make rank`.")
else:
    st.sidebar.caption(f"Latest score date: **{as_of.isoformat()}**")


# ---------------------------- Page 1 ----------------------------

if page == "Top 20":
    st.title("Top 20 stocks to invest in")
    if as_of is None:
        st.stop()
    tabs = st.tabs([f"{h} horizon" for h in HORIZONS])
    for tab, h in zip(tabs, HORIZONS):
        with tab:
            df = _top_n(h, settings.top_n, as_of)
            if df.empty:
                st.info(f"No scores for horizon {h}.")
                continue
            st.dataframe(df, use_container_width=True, hide_index=True)
            fig = px.bar(
                df, x="ticker", y="blended",
                color="sector", hover_data=["name", "composite", "ml"],
                title=f"Blended score — {h}",
            )
            st.plotly_chart(fig, use_container_width=True)


# ---------------------------- Page 2 ----------------------------

elif page == "Ticker drill-down":
    st.title("Ticker drill-down")
    tickers = _all_tickers()
    if not tickers:
        st.info("No tickers ingested yet.")
        st.stop()
    ticker = st.selectbox("Ticker", tickers, index=0)
    col1, col2 = st.columns([2, 1])

    with col1:
        prices = _prices_for(ticker)
        if not prices.empty:
            fig = px.line(prices, x="date", y="close", title=f"{ticker} close (180 d)")
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Consensus over time")
        cons = _consensus_history(ticker)
        if not cons.empty:
            melted = cons.melt(
                id_vars=["as_of"],
                value_vars=["strong_buy", "buy", "hold", "sell", "strong_sell"],
                var_name="rating", value_name="count",
            )
            fig = px.bar(melted, x="as_of", y="count", color="rating", barmode="stack")
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Recent analyst actions")
        st.dataframe(_actions(ticker), use_container_width=True, hide_index=True)

    with col2:
        st.subheader("Scores (latest)")
        if as_of is not None:
            with session_scope() as s:
                rows = (
                    s.query(Score)
                    .filter(Score.ticker == ticker, Score.as_of == as_of)
                    .all()
                )
            df = pd.DataFrame(
                [
                    {
                        "horizon": r.horizon,
                        "blended": r.blended_score,
                        "composite": r.composite_score,
                        "ml": r.ml_score,
                        "percentile": r.percentile,
                    }
                    for r in rows
                ]
            )
            st.dataframe(df, use_container_width=True, hide_index=True)

        st.subheader("13F net flow (shares held)")
        flow = _13f_flow(ticker)
        if not flow.empty:
            fig = px.line(flow, x="quarter", y="shares", markers=True)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Insider trades")
        st.dataframe(_insider_trades(ticker), use_container_width=True, hide_index=True)


# ---------------------------- Page 3 ----------------------------

elif page == "Sources & freshness":
    st.title("Sources & freshness")
    df = _run_log(limit=200)
    if df.empty:
        st.info("No runs logged yet.")
        st.stop()

    # Summary: last successful run per job.
    latest = (
        df[df["status"] == "ok"]
        .sort_values("finished_at", ascending=False)
        .groupby("job", as_index=False)
        .head(1)
    )
    st.subheader("Last successful run per job")
    st.dataframe(latest[["job", "finished_at", "rows"]], use_container_width=True, hide_index=True)

    st.subheader("Recent run log")
    st.dataframe(df, use_container_width=True, hide_index=True)

    errors = df[df["status"] == "error"]
    if not errors.empty:
        st.subheader("Recent errors")
        st.dataframe(errors.head(20), use_container_width=True, hide_index=True)


# ---------------------------- Page 4 ----------------------------

elif page == "Methodology":
    st.title("Methodology")
    st.markdown(
        """
**Composite score.** Each feature is z-scored across the universe (clipped to ±5)
then combined with the horizon-specific weights below. The final **blended
score** mixes the composite with an ML ranker (LightGBM) that learns from the
historical relationship between today's features and realised forward returns:

```
blended = blend_composite_weight · z(composite)  +  blend_ml_weight · z(ml)
```

Until enough feature snapshots exist (~60 daily rows), the ML component falls
back to the composite score so the blended number is meaningful from day one.

**Weights (current):**
"""
    )
    w = pd.DataFrame(WEIGHTS).reindex(FEATURE_NAMES)
    st.dataframe(w, use_container_width=True)

    st.markdown(
        f"""
**Blend.** `{settings.blend_composite_weight}` composite +
`{settings.blend_ml_weight}` ML.

**Liquidity gate.** Excludes any stock whose 20-day average dollar volume is
below **${settings.liquidity_min_dollar_volume:,.0f}**.

**Not investment advice.** This tool summarises publicly available data to help
you build a shortlist for further research. It does not execute trades, does not
account for your tax or regulatory situation, and past signal does not predict
future return.
"""
    )
