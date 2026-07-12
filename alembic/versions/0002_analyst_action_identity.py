"""analyst action identity (firm_key) + de-dupe + unique constraint

Fixes: the same real-world analyst firm was counted as multiple distinct
sources, for two compounding reasons —

1. AnalystAction had no unique constraint and the ingesters (yfinance,
   Finnhub, FMP) blindly INSERTed a new row every crawl. Every feed
   returns a rolling ~90-day window of past actions on every call, so a
   single real action could accumulate into dozens of duplicate rows
   after a few days of scheduled crawling.
2. Different feeds spell the same firm differently ("Goldman Sachs" vs
   "Goldman Sachs & Co." vs "GOLDMAN SACHS GROUP"), and nothing collapsed
   those variants before counting "distinct firms".

This migration adds a canonical `firm_key` column (invest.firms.
canonical_firm_key), backfills it for existing rows, deletes rows that
are now identical under (ticker, firm_key, date, action, source) keeping
the earliest `id`, then adds a unique index on that tuple so duplicate
insertion becomes impossible going forward. Ingesters are updated
separately to upsert against this constraint instead of blind INSERT.

Revision ID: 0002
Revises: 0001
Create Date: 2026-07-12
"""
from alembic import op
import sqlalchemy as sa

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def _canonical_firm_key(name: str | None) -> str:
    """Inlined copy of invest.firms.canonical_firm_key so this migration
    has no import-time dependency on the application package (Alembic
    migrations should be self-contained and stable even if the app's
    normalisation logic changes later)."""
    n = (name or "").lower().strip()
    n = n.replace(".", "").replace(",", "")
    for suf in (
        " group", " securities", " capital markets", " capital", " markets",
        " & co", " and co", " llc", " ltd", " limited", " inc", " incorporated",
        " plc", " ag", " sa", " spa", " nv", " bv", " holdings", " holding",
    ):
        while n.endswith(suf):
            n = n[: -len(suf)].strip()
    return " ".join(n.split())


def upgrade() -> None:
    bind = op.get_bind()

    op.add_column("analyst_actions", sa.Column("firm_key", sa.String(160), nullable=True))

    # Backfill firm_key for existing rows.
    rows = bind.execute(sa.text("SELECT id, firm FROM analyst_actions")).fetchall()
    for row_id, firm in rows:
        key = _canonical_firm_key(firm)
        bind.execute(
            sa.text("UPDATE analyst_actions SET firm_key = :key WHERE id = :id"),
            {"key": key, "id": row_id},
        )

    # De-duplicate: for each (ticker, firm_key, date, action, source) group,
    # keep the row with the smallest id, delete the rest. Runs entirely in
    # SQL so it scales to however many duplicates accumulated in the cache.
    bind.execute(
        sa.text(
            """
            DELETE FROM analyst_actions
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM analyst_actions
                GROUP BY ticker, firm_key, date, action, source
            )
            """
        )
    )

    # Matches the ORM model's __table_args__ exactly (name + columns) so
    # alembic-migrated production DBs and Base.metadata.create_all()-based
    # test/dev DBs end up with an identical schema.
    op.create_index(
        "uq_analyst_actions_identity",
        "analyst_actions",
        ["ticker", "firm_key", "date", "action", "source"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("uq_analyst_actions_identity", table_name="analyst_actions")
    with op.batch_alter_table("analyst_actions") as batch_op:
        batch_op.drop_column("firm_key")
