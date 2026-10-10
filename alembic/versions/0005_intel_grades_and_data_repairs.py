"""company intel tables, integrated grades, and three data repairs

Schema:
  - stocks.cik                       issuer CIK for the SEC filing-stream crawl
  - analyst_actions.prior_target /
    analyst_actions.target_action    per-firm price-target changes
  - news_items, sec_filings, intel_snapshots, grades, calibration

Data repairs (each one a measured defect in the committed database):

1. insider_trades placeholder explosion. Form 4 filings we could not parse
   in detail were stored as placeholder rows with NULL shares/price, and
   SQLite never treats two NULLs as equal, so the unique index added in 0004
   could not deduplicate them: every crawl re-inserted the whole rolling
   ATOM window. Measured: 341,270 placeholder rows for only 5,292 distinct
   (ticker, date) pairs — ~57 MB of an 87 MB database that is committed to
   git on every run and was closing in on GitHub's hard 100 MB file limit
   (at which point every crawl's push would be rejected). Placeholders are
   collapsed to one row each and rewritten with shares = price = 0 so the
   unique index applies to them from now on. They still contribute exactly
   zero to every insider feature.

2. holdings_13f.quarter was derived from the FILING date, not the period of
   report. A Q2 portfolio (period ending 30 Jun) filed in August was labelled
   Q3. Every timely 13F is filed within 45 days of its quarter end, so the
   true period is the quarter before the filing quarter; rows are relabelled
   accordingly (two-step through a temporary prefix so the unique index on
   (filer, ticker, quarter) is never transiently violated).

3. Legacy analyst_actions rows with action = 'reit' (a yfinance spelling
   from before the action map normalised it) are folded into 'reiterate',
   dropping any row that would collide with an existing 'reiterate' twin.

Revision ID: 0005
Revises: 0004
Create Date: 2026-10-07
"""
from datetime import date

import sqlalchemy as sa
from alembic import op

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def _prev_quarter_label(d: date) -> str:
    q = (d.month - 1) // 3 + 1
    if q == 1:
        return f"{d.year - 1}Q4"
    return f"{d.year}Q{q - 1}"


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)
    existing = set(insp.get_table_names())

    stock_cols = {c["name"] for c in insp.get_columns("stocks")}
    if "cik" not in stock_cols:
        op.add_column("stocks", sa.Column("cik", sa.String(10), nullable=True))
    action_cols = {c["name"] for c in insp.get_columns("analyst_actions")}
    if "prior_target" not in action_cols:
        op.add_column("analyst_actions", sa.Column("prior_target", sa.Float, nullable=True))
    if "target_action" not in action_cols:
        op.add_column("analyst_actions", sa.Column("target_action", sa.String(16), nullable=True))

    if "news_items" not in existing:
        op.create_table(
            "news_items",
            sa.Column("id", sa.String(40), primary_key=True),
            sa.Column("ticker", sa.String(16), nullable=False),
            sa.Column("published_at", sa.DateTime, nullable=False),
            sa.Column("title", sa.String(300), nullable=False),
            sa.Column("publisher", sa.String(80)),
            sa.Column("url", sa.String(400)),
            sa.Column("source", sa.String(16), nullable=False),
            sa.Column("sentiment", sa.Float),
            sa.Column("relevance", sa.Float),
        )
        op.create_index("ix_news_items_ticker", "news_items", ["ticker"])
        op.create_index("ix_news_items_published_at", "news_items", ["published_at"])
    if "sec_filings" not in existing:
        op.create_table(
            "sec_filings",
            sa.Column("ticker", sa.String(16), primary_key=True),
            sa.Column("accession", sa.String(24), primary_key=True),
            sa.Column("form", sa.String(24), nullable=False),
            sa.Column("filing_date", sa.Date, nullable=False),
            sa.Column("report_date", sa.Date),
            sa.Column("items", sa.String(64)),
            sa.Column("description", sa.String(160)),
        )
        op.create_index("ix_sec_filings_filing_date", "sec_filings", ["filing_date"])
    if "intel_snapshots" not in existing:
        op.create_table(
            "intel_snapshots",
            sa.Column("ticker", sa.String(16), primary_key=True),
            sa.Column("kind", sa.String(24), primary_key=True),
            sa.Column("as_of", sa.DateTime, nullable=False),
            sa.Column("payload", sa.Text, nullable=False),
        )
        op.create_index("ix_intel_snapshots_as_of", "intel_snapshots", ["as_of"])
    if "grades" not in existing:
        op.create_table(
            "grades",
            sa.Column("ticker", sa.String(16), primary_key=True),
            sa.Column("as_of", sa.Date, primary_key=True),
            sa.Column("grade_score", sa.Float),
            sa.Column("letter", sa.String(3)),
            sa.Column("percentile", sa.Float),
            sa.Column("confidence", sa.Float),
            sa.Column("alpha_1m", sa.Float),
            sa.Column("p_outperform_1m", sa.Float),
            sa.Column("alpha_3m", sa.Float),
            sa.Column("detail_json", sa.Text),
        )
    if "calibration" not in existing:
        op.create_table(
            "calibration",
            sa.Column("as_of", sa.Date, primary_key=True),
            sa.Column("horizon", sa.String(8), primary_key=True),
            sa.Column("payload", sa.Text, nullable=False),
        )

    # --- repair 1: collapse insider placeholder rows -----------------------
    bind.execute(
        sa.text(
            """
            DELETE FROM insider_trades
            WHERE (shares IS NULL OR price IS NULL)
              AND id NOT IN (
                SELECT MIN(id) FROM insider_trades
                WHERE shares IS NULL OR price IS NULL
                GROUP BY ticker, filer, date, action
              )
            """
        )
    )
    # A surviving placeholder could collide with an already-zeroed twin.
    bind.execute(
        sa.text(
            """
            DELETE FROM insider_trades
            WHERE (shares IS NULL OR price IS NULL)
              AND EXISTS (
                SELECT 1 FROM insider_trades z
                WHERE z.ticker = insider_trades.ticker
                  AND z.filer IS insider_trades.filer
                  AND z.date = insider_trades.date
                  AND z.action IS insider_trades.action
                  AND z.shares = 0 AND z.price = 0
              )
            """
        )
    )
    bind.execute(
        sa.text(
            "UPDATE insider_trades SET shares = 0, price = 0 "
            "WHERE shares IS NULL OR price IS NULL"
        )
    )

    # --- repair 2: 13F quarter = period of report ---------------------------
    rows = bind.execute(sa.text("SELECT id, filing_date FROM holdings_13f")).fetchall()
    for row_id, fdate in rows:
        if fdate is None:
            continue
        d = fdate if isinstance(fdate, date) else date.fromisoformat(str(fdate)[:10])
        bind.execute(
            sa.text("UPDATE holdings_13f SET quarter = :q WHERE id = :id"),
            {"q": "tmp:" + _prev_quarter_label(d), "id": row_id},
        )
    bind.execute(
        sa.text(
            "UPDATE holdings_13f SET quarter = substr(quarter, 5) WHERE quarter LIKE 'tmp:%'"
        )
    )

    # --- repair 3: legacy 'reit' action spelling ----------------------------
    bind.execute(
        sa.text(
            """
            DELETE FROM analyst_actions
            WHERE action = 'reit'
              AND EXISTS (
                SELECT 1 FROM analyst_actions a
                WHERE a.action = 'reiterate'
                  AND a.ticker = analyst_actions.ticker
                  AND a.firm_key IS analyst_actions.firm_key
                  AND a.date = analyst_actions.date
                  AND a.source = analyst_actions.source
              )
            """
        )
    )
    bind.execute(sa.text("UPDATE analyst_actions SET action = 'reiterate' WHERE action = 'reit'"))


def downgrade() -> None:
    for name in ("calibration", "grades", "intel_snapshots", "sec_filings", "news_items"):
        op.drop_table(name)
    with op.batch_alter_table("analyst_actions") as batch_op:
        batch_op.drop_column("target_action")
        batch_op.drop_column("prior_target")
    with op.batch_alter_table("stocks") as batch_op:
        batch_op.drop_column("cik")
