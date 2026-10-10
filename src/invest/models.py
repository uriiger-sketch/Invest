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
    # SEC Central Index Key of the ISSUER (not a 13F filer), resolved from
    # sec.gov/files/company_tickers.json. Needed to read the company's own
    # filing stream (8-K events, 13D activist stakes, offerings).
    cik: Mapped[str | None] = mapped_column(String(10))
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
    # The firm's PREVIOUS price target and what it did to it ("raises" /
    # "lowers" / "maintains" / "announces"). Most sell-side notes leave the
    # rating unchanged but move the target, so without these an analyst
    # cutting a target from 200 to 150 was stored as a neutral "reiterate".
    prior_target: Mapped[float | None] = mapped_column(Float)
    target_action: Mapped[str | None] = mapped_column(String(16))
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

    __table_args__ = (
        # Each Form 4 filing's ATOM feed entry is re-fetched on every crawl
        # (the feed is a rolling recent-filings window, not a one-time
        # event), so without this constraint the same real transaction would
        # be re-inserted every ~30 minutes and insider_net_buy_90d would
        # inflate by however many times it was re-crawled within the 90-day
        # window. NULL shares/price (the coarse "something happened"
        # fallback row for filings we couldn't parse in detail) are exempt
        # from SQL unique-constraint matching by design — harmless here
        # since those rows always contribute a net-zero signal.
        Index(
            "uq_insider_trades_identity",
            "ticker", "filer", "date", "action", "shares", "price",
            unique=True,
        ),
    )


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


class NewsItem(Base):
    """One headline about one ticker, deduplicated across feeds.

    `id` is a hash of (ticker, normalised title) so the same story syndicated
    by Yahoo and Google News is stored — and counted in the sentiment
    average — once.
    """

    __tablename__ = "news_items"

    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    ticker: Mapped[str] = mapped_column(String(16), index=True)
    published_at: Mapped[datetime] = mapped_column(DateTime, index=True)
    title: Mapped[str] = mapped_column(String(300))
    publisher: Mapped[str | None] = mapped_column(String(80))
    url: Mapped[str | None] = mapped_column(String(400))
    source: Mapped[str] = mapped_column(String(16))
    # Finance-lexicon headline tone in [-1, 1] and how clearly the headline is
    # about THIS company (1 = names it, 0.5 = query hit only).
    sentiment: Mapped[float | None] = mapped_column(Float)
    relevance: Mapped[float | None] = mapped_column(Float)


class SecFiling(Base):
    """Issuer-level SEC filings of interest (8-K events, 13D stakes, offerings)."""

    __tablename__ = "sec_filings"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    accession: Mapped[str] = mapped_column(String(24), primary_key=True)
    form: Mapped[str] = mapped_column(String(24))
    filing_date: Mapped[date] = mapped_column(Date, index=True)
    report_date: Mapped[date | None] = mapped_column(Date)
    items: Mapped[str | None] = mapped_column(String(64))
    description: Mapped[str | None] = mapped_column(String(160))


class IntelSnapshot(Base):
    """Latest parsed company intel per (ticker, kind) — overwritten each crawl.

    Only the LATEST payload is kept: Yahoo already reports the history we
    need inside each payload (EPS estimates now vs 7/30/60/90 days ago,
    recommendation counts now vs 1-3 months ago), so storing every crawl
    would only bloat the committed database.
    """

    __tablename__ = "intel_snapshots"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    kind: Mapped[str] = mapped_column(String(24), primary_key=True)
    as_of: Mapped[datetime] = mapped_column(DateTime, index=True)
    payload: Mapped[str] = mapped_column(Text)


class Grade(Base):
    """Integrated cross-horizon grade per ticker per day (see pipeline/grade.py)."""

    __tablename__ = "grades"

    ticker: Mapped[str] = mapped_column(String(16), primary_key=True)
    as_of: Mapped[date] = mapped_column(Date, primary_key=True)
    grade_score: Mapped[float | None] = mapped_column(Float)
    letter: Mapped[str | None] = mapped_column(String(3))
    percentile: Mapped[float | None] = mapped_column(Float)
    confidence: Mapped[float | None] = mapped_column(Float)
    alpha_1m: Mapped[float | None] = mapped_column(Float)
    p_outperform_1m: Mapped[float | None] = mapped_column(Float)
    alpha_3m: Mapped[float | None] = mapped_column(Float)
    detail_json: Mapped[str | None] = mapped_column(Text)


class Calibration(Base):
    """Per-horizon model calibration (posterior factor ICs, blend weights)."""

    __tablename__ = "calibration"

    as_of: Mapped[date] = mapped_column(Date, primary_key=True)
    horizon: Mapped[str] = mapped_column(String(8), primary_key=True)
    payload: Mapped[str] = mapped_column(Text)


class RunLog(Base):
    __tablename__ = "run_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job: Mapped[str] = mapped_column(String(64), index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(16))  # ok / error / running
    rows_written: Mapped[int] = mapped_column(Integer, default=0)
    error: Mapped[str | None] = mapped_column(Text)
