"""initial schema

Revision ID: 0001
Revises:
Create Date: 2026-04-20
"""
from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stocks",
        sa.Column("ticker", sa.String(16), primary_key=True),
        sa.Column("name", sa.String(255)),
        sa.Column("sector", sa.String(64)),
        sa.Column("industry", sa.String(128)),
        sa.Column("market_cap", sa.Float),
        sa.Column("beta", sa.Float),
        sa.Column("in_universe", sa.Boolean, nullable=False, server_default=sa.text("1")),
        sa.Column("updated_at", sa.DateTime),
    )

    op.create_table(
        "prices",
        sa.Column("ticker", sa.String(16), sa.ForeignKey("stocks.ticker"), primary_key=True),
        sa.Column("date", sa.Date, primary_key=True),
        sa.Column("open", sa.Float),
        sa.Column("high", sa.Float),
        sa.Column("low", sa.Float),
        sa.Column("close", sa.Float),
        sa.Column("adj_close", sa.Float),
        sa.Column("volume", sa.Float),
    )

    op.create_table(
        "analyst_actions",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("ticker", sa.String(16), sa.ForeignKey("stocks.ticker"), index=True),
        sa.Column("firm", sa.String(128)),
        sa.Column("analyst", sa.String(128)),
        sa.Column("action", sa.String(32)),
        sa.Column("from_grade", sa.String(64)),
        sa.Column("to_grade", sa.String(64)),
        sa.Column("target_price", sa.Float),
        sa.Column("date", sa.Date, index=True),
        sa.Column("source", sa.String(32)),
    )
    op.create_index("ix_analyst_actions_ticker_date", "analyst_actions", ["ticker", "date"])

    op.create_table(
        "consensus",
        sa.Column("ticker", sa.String(16), sa.ForeignKey("stocks.ticker"), primary_key=True),
        sa.Column("as_of_date", sa.Date, primary_key=True),
        sa.Column("source", sa.String(32), primary_key=True),
        sa.Column("strong_buy", sa.Integer),
        sa.Column("buy", sa.Integer),
        sa.Column("hold", sa.Integer),
        sa.Column("sell", sa.Integer),
        sa.Column("strong_sell", sa.Integer),
        sa.Column("mean_target", sa.Float),
        sa.Column("high_target", sa.Float),
        sa.Column("low_target", sa.Float),
        sa.Column("num_analysts", sa.Integer),
    )

    op.create_table(
        "holdings_13f",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("filer_cik", sa.String(16), index=True),
        sa.Column("filer_name", sa.String(255)),
        sa.Column("ticker", sa.String(16), index=True),
        sa.Column("shares", sa.Float),
        sa.Column("value_usd", sa.Float),
        sa.Column("quarter", sa.String(8)),
        sa.Column("filing_date", sa.Date),
    )
    op.create_index(
        "ix_holdings_13f_filer_ticker_quarter",
        "holdings_13f",
        ["filer_cik", "ticker", "quarter"],
        unique=True,
    )

    op.create_table(
        "insider_trades",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("ticker", sa.String(16), index=True),
        sa.Column("filer", sa.String(255)),
        sa.Column("action", sa.String(16)),
        sa.Column("shares", sa.Float),
        sa.Column("price", sa.Float),
        sa.Column("date", sa.Date, index=True),
    )

    op.create_table(
        "features",
        sa.Column("ticker", sa.String(16), primary_key=True),
        sa.Column("as_of", sa.Date, primary_key=True),
        sa.Column("feature_json", sa.Text, nullable=False),
    )

    op.create_table(
        "scores",
        sa.Column("ticker", sa.String(16), primary_key=True),
        sa.Column("horizon", sa.String(8), primary_key=True),
        sa.Column("as_of", sa.Date, primary_key=True),
        sa.Column("composite_score", sa.Float),
        sa.Column("ml_score", sa.Float),
        sa.Column("blended_score", sa.Float),
        sa.Column("percentile", sa.Float),
    )

    op.create_table(
        "run_log",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("job", sa.String(64), index=True),
        sa.Column("started_at", sa.DateTime, nullable=False),
        sa.Column("finished_at", sa.DateTime),
        sa.Column("status", sa.String(16), nullable=False),
        sa.Column("rows_written", sa.Integer, nullable=False, server_default="0"),
        sa.Column("error", sa.Text),
    )


def downgrade() -> None:
    for tbl in (
        "run_log",
        "scores",
        "features",
        "insider_trades",
        "holdings_13f",
        "consensus",
        "analyst_actions",
        "prices",
        "stocks",
    ):
        op.drop_table(tbl)
