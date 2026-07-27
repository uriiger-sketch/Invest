from __future__ import annotations

from datetime import date, datetime

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Stock(Base):
    __tablename__ = "stocks"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    name: Mapped[str | None] = mapped_column(String(255))
    sector: Mapped[str | None] = mapped_column(String(64))
    industry: Mapped[str | None] = mapped_column(String(128))
    market_cap: Mapped[float | None] = mapped_column(Float)
    beta: Mapped[float | None] = mapped_column(Float)
    # CUSIP is the authoritative security identifier used by SEC 13F filings.
    # Matching holdings on CUSIP instead of company name is what makes the
    # institutional-holder counts actually populate: 13F legal names
    # ("AMAZON COM INC") rarely equal the vendor names we store
    # ("Amazon.com, Inc."), so name matching dropped nearly every holding.
    cusip: Mapped[str | None] = mapped_column(String(12), index=True)
    in_universe: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime)


class Price(Base):
    __tablename__ = "prices"

    ticker: Mapped[str] = mapped_column(
        String(16), ForeignKey("stocks.ticker"), primary_key=True
    )
    date: Mapped[date] = mapped_column(Date, primary_key=True)
    open: Mapped[float | None] = mapped_column(Float)
    high: Mapped[float | None] = mapped_column(Float)
    low: Mapped[float | None] = mapped_column(Float)
    close: Mapped[float | None] = mapped_column(Float)
    adj_close: Mapped[float | None] = mapped_column(Float)
    volume: Mapped[float | None] = mapped_column(Float)


class AnalystAction(Base):
    __tablename__ = "analyst_actions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(16), ForeignKey("stocks.ticker"), index=True)
    firm: Mapped[str | None] = mapped_column(String(128))
    # Canonical identity for `firm` (invest.firms.canonical_firm_key), computed
    # at insert time. "Goldman Sachs" / "Goldman Sachs & Co." / "GOLDMAN SACHS
    # GROUP" all collapse to the same firm_key so the same real analyst desk
    # can never be stored — or counted — as more than one source, regardless
    # of which feed reported it or how that feed spelled the name.
    firm_key: Mapped[str | None] = mapped_column(String(160))
    analyst: Mapped[str | None] = mapped_column(String(128))
    action: Mapped[str | None] = mapped_column(String(32))  # upgrade / downgrade / init / reiterate
    from_grade: Mapped[str | None] = mapped_column(String(64))
    to_grade: Mapped[str | None] = mapped_column(String(64))
    target_price: Mapped[float | None] = mapped_column(Float)
    date: Mapped[date] = mapped_column(Date, index=True)
    source: Mapped[str] = mapped_column(String(32))

    __table_args__ = (
        Index("ix_analyst_actions_ticker_date", "ticker", "date"),
        # The real fix for "same firm counted as multiple sources": without
        # this, every crawl re-inserts the SAME historical action (feeds
        # return a rolling 90-day window each call), so one real Goldman
        # Sachs upgrade could physically exist as dozens of duplicate rows
        # after a few days of scheduled crawling. This constraint makes that
        # impossible at the database level; ingesters upsert against it.
        Index(
            "uq_analyst_actions_identity",
            "ticker", "firm_key", "date", "action", "source",
            unique=True,
        ),
    )


class Consensus(Base):
    __tablename__ = "consensus"

    ticker: Mapped[str] = mapped_column(
        String(16), ForeignKey("stocks.ticker"), primary_key=True
    )
    as_of_date: Mapped[date] = mapped_column(Date, primary_key=True)
    source: Mapped[str] = mapped_column(String(32), primary_key=True)
    strong_buy: Mapped[int | None] = mapped_column(Integer)
    buy: Mapped[int | None] = mapped_column(Integer)
    hold: Mapped[int | None] = mapped_column(Integer)
    sell: Mapped[int | None] = mapped_column(Integer)
    strong_sell: Mapped[int | None] = mapped_column(Integer)
    mean_target: Mapped[float | None] = mapped_column(Float)
    high_target: Mapped[float | None] = mapped_column(Float)
    low_target: Mapped[float | None] = mapped_column(Float)
    num_analysts: Mapped[int | None] = mapped_column(Integer)


class Holding13F(Base):
    __tablename__ = "holdings_13f"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    filer_cik: Mapped[str] = mapped_column(String(16), index=True)
    filer_name: Mapped[str] = mapped_column(String(255))
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    shares: Mapped[float | None] = mapped_column(Float)
    value_usd: Mapped[float | None] = mapped_column(Float)
    quarter: Mapped[str] = mapped_column(String(8))  # e.g. 2025Q4
    filing_date: Mapped[date] = mapped_column(Date)

    __table_args__ = (
        Index("ix_holdings_13f_filer_ticker_quarter", "filer_cik", "ticker", "quarter", unique=True),
    )


class InsiderTrade(Base):
    __tablename__ = "insider_trades"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    filer: Mapped[str | None] = mapped_column(String(255))
    action: Mapped[str | None] = mapped_column(String(16))  # buy / sell
    shares: Mapped[float | None] = mapped_column(Float)
    price: Mapped[float | None] = mapped_column(Float)
    date: Mapped[date] = mapped_column(Date, index=True)


class FeatureSnapshot(Base):
    __tablename__ = "features"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    as_of: Mapped[date] = mapped_column(Date, primary_key=True)
    feature_json: Mapped[str] = mapped_column(Text)


class Score(Base):
    __tablename__ = "scores"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    horizon: Mapped[str] = mapped_column(String(8), primary_key=True)
    as_of: Mapped[date] = mapped_column(Date, primary_key=True)
    composite_score: Mapped[float | None] = mapped_column(Float)
    ml_score: Mapped[float | None] = mapped_column(Float)
    blended_score: Mapped[float | None] = mapped_column(Float)
    percentile: Mapped[float | None] = mapped_column(Float)


class RunLog(Base):
    __tablename__ = "run_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job: Mapped[str] = mapped_column(String(64), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(16))  # ok / error / running
    rows_written: Mapped[int] = mapped_column(Integer, default=0)
    error: Mapped[str | None] = mapped_column(Text)
