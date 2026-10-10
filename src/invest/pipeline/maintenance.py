"""Keep the committed SQLite database bounded.

`data/invest.db` is committed to git by every crawl (it is the pipeline's
state between runs), and GitHub hard-rejects files over 100 MB. It had
reached 87 MB — 57 MB of it duplicate insider placeholder rows (fixed in
migration 0005) — so the history tables that only feed rolling-window
calculations are pruned to their useful windows and the file is VACUUMed.
"""
from __future__ import annotations

import logging
import os
from datetime import date, datetime, timedelta

from sqlalchemy import text

from ..config import get_settings
from ..db import get_engine

logger = logging.getLogger(__name__)


def prune_and_vacuum() -> dict[str, int]:
    settings = get_settings()
    today = date.today()
    now = datetime.utcnow()
    plan = [
        ("features", "as_of < :cut", today - timedelta(days=settings.feature_retention_days)),
        ("scores", "as_of < :cut", today - timedelta(days=settings.score_retention_days)),
        ("grades", "as_of < :cut", today - timedelta(days=settings.score_retention_days)),
        ("calibration", "as_of < :cut", today - timedelta(days=settings.score_retention_days)),
        ("news_items", "published_at < :cut", now - timedelta(days=settings.news_retention_days)),
        ("run_log", "started_at < :cut", now - timedelta(days=settings.run_log_retention_days)),
        ("sec_filings", "filing_date < :cut", today - timedelta(days=settings.filing_retention_days)),
        # Consensus snapshots older than a year are never read (the longest
        # look-back is the 30-day target revision); keep a year for audit.
        ("consensus", "as_of_date < :cut", today - timedelta(days=400)),
        # Insider rows outside the 90-day feature window + slack.
        ("insider_trades", "date < :cut", today - timedelta(days=200)),
    ]
    deleted: dict[str, int] = {}
    engine = get_engine()
    with engine.begin() as conn:
        tables = {r[0] for r in conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))}
        for table, where, cut in plan:
            if table not in tables:
                continue
            res = conn.execute(text(f"DELETE FROM {table} WHERE {where}"), {"cut": cut})
            deleted[table] = int(res.rowcount or 0)
    if engine.url.get_backend_name() == "sqlite":
        with engine.connect() as conn:
            conn.execution_options(isolation_level="AUTOCOMMIT").execute(text("VACUUM"))
        path = engine.url.database
        if path and path != ":memory:" and os.path.exists(path):
            mb = os.path.getsize(path) / 1e6
            log = logger.warning if mb > settings.db_size_warn_mb else logger.info
            log("database size after maintenance: %.1f MB (warn above %.0f MB)",
                mb, settings.db_size_warn_mb)
    logger.info("maintenance pruned: %s", deleted)
    return deleted
