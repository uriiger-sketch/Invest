"""APScheduler jobs. All cadences configured here."""
from __future__ import annotations

import logging
from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from .config import get_settings

logger = logging.getLogger(__name__)

ET = pytz.timezone("US/Eastern")

_scheduler: BackgroundScheduler | None = None


def _job_ingest_prices() -> None:
    from .pipeline.ingest import ingest_prices_only

    logger.info("scheduler: ingest_prices starting")
    ingest_prices_only()


def _job_ingest_all() -> None:
    from .pipeline.ingest import ingest_all

    logger.info("scheduler: ingest_all starting")
    ingest_all()


def _job_compute_scores() -> None:
    from .pipeline.rank import rank_all
    from .universe import current_universe

    logger.info("scheduler: rank_all starting")
    rank_all(current_universe())


def _job_train_ml() -> None:
    from .pipeline.ml_rank import train_all

    logger.info("scheduler: train_all starting")
    train_all()


def _job_refresh_universe() -> None:
    from .universe import refresh_universe

    logger.info("scheduler: refresh_universe")
    refresh_universe()


def start_scheduler() -> BackgroundScheduler:
    global _scheduler
    if _scheduler is not None:
        return _scheduler
    if not get_settings().run_scheduler:
        logger.info("RUN_SCHEDULER=false; scheduler disabled")
        return BackgroundScheduler(timezone=ET)

    sch = BackgroundScheduler(timezone=ET)

    # Intraday prices: every 30 min during RTH, Mon–Fri.
    sch.add_job(
        _job_ingest_prices,
        CronTrigger(day_of_week="mon-fri", hour="9-16", minute="*/30", timezone=ET),
        id="ingest_prices",
        max_instances=1,
        coalesce=True,
    )

    # Ratings / fundamentals / EDGAR — light pull every 6 h.
    sch.add_job(
        _job_ingest_all,
        IntervalTrigger(hours=6),
        id="ingest_all_6h",
        max_instances=1,
        coalesce=True,
        next_run_time=datetime.now(ET),
    )

    # Daily scoring + training at 18:30 and 19:00 ET.
    sch.add_job(
        _job_compute_scores,
        CronTrigger(hour=18, minute=30, timezone=ET),
        id="compute_scores_daily",
        max_instances=1,
        coalesce=True,
    )
    sch.add_job(
        _job_train_ml,
        CronTrigger(hour=19, minute=0, timezone=ET),
        id="train_ml_daily",
        max_instances=1,
        coalesce=True,
    )

    # Weekly universe refresh Sunday 03:00 ET.
    sch.add_job(
        _job_refresh_universe,
        CronTrigger(day_of_week="sun", hour=3, minute=0, timezone=ET),
        id="refresh_universe_weekly",
        max_instances=1,
    )

    sch.start()
    logger.info("scheduler started with %d jobs", len(sch.get_jobs()))
    _scheduler = sch
    return sch
