"""add Stock.cusip for CUSIP-first 13F matching

SEC 13F filings identify securities by CUSIP, which every infoTable entry
already carries — the parser read it and then threw it away, matching on
company NAME instead. 13F legal names ("AMAZON COM INC") rarely equal the
vendor names we store ("Amazon.com, Inc."), so almost every holding failed
to match and `holdings_13f` stayed empty (Insts = 0 for every ticker in the
report).

This adds the column so holdings can be matched on the authoritative
identifier, with name matching kept only as a fallback.

Revision ID: 0003
Revises: 0002
Create Date: 2026-07-12
"""
from alembic import op
import sqlalchemy as sa

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("stocks", sa.Column("cusip", sa.String(12), nullable=True))
    op.create_index("ix_stocks_cusip", "stocks", ["cusip"])


def downgrade() -> None:
    op.drop_index("ix_stocks_cusip", table_name="stocks")
    with op.batch_alter_table("stocks") as batch_op:
        batch_op.drop_column("cusip")
