"""insider trade identity + unique constraint

Fixes: Form 4 ingest previously wrote one placeholder row per filing with no
transaction detail (filer="(aggregated form-4 activity)", shares/price=None),
which was harmless to duplicate re-insertion because the feature that reads
it always computed a net-zero signal regardless. Now that `ingest_insider`
parses real per-transaction data (real filer name, buy/sell, shares, price),
duplicate re-insertion on every ~30-minute crawl of the SAME historical
filing (the ATOM feed is a rolling recent-filings window, not a one-time
event) would inflate `insider_net_buy_90d` by however many times a
transaction was re-crawled within its 90-day relevance window.

This migration de-duplicates existing rows under
(ticker, filer, date, action, shares, price) — keeping the earliest id — then
adds a unique index on that tuple so duplicate insertion becomes impossible
going forward. NULL shares/price rows (the coarse fallback for filings that
couldn't be parsed in detail) are exempt from SQL unique-constraint matching,
which is fine since those rows always contribute a net-zero signal.

Revision ID: 0004
Revises: 0003
Create Date: 2026-08-02
"""
from alembic import op
import sqlalchemy as sa

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()

    # SQLite treats NULL as distinct from every other NULL for uniqueness
    # purposes, so this only needs to de-duplicate rows where every key
    # column is non-NULL (the real, individually-parsed transactions) —
    # placeholder rows with NULL shares/price are left untouched.
    bind.execute(
        sa.text(
            """
            DELETE FROM insider_trades
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM insider_trades
                GROUP BY ticker, filer, date, action, shares, price
            )
            """
        )
    )

    op.create_index(
        "uq_insider_trades_identity",
        "insider_trades",
        ["ticker", "filer", "date", "action", "shares", "price"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("uq_insider_trades_identity", table_name="insider_trades")
