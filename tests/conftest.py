"""Shared pytest fixtures: use an in-memory SQLite DB for every test."""
from __future__ import annotations

import os

os.environ.setdefault("INVEST_DB_URL", "sqlite:///:memory:")
os.environ.setdefault("FINNHUB_API_KEY", "")
os.environ.setdefault("SCRAPE_OK", "false")

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from invest import db as db_mod
from invest.models import Base


@pytest.fixture(autouse=True)
def _fresh_db(monkeypatch):
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        future=True,
    )
    Base.metadata.create_all(engine)
    factory = sessionmaker(bind=engine, expire_on_commit=False, future=True)
    monkeypatch.setattr(db_mod, "_engine", engine)
    monkeypatch.setattr(db_mod, "_SessionFactory", factory)
    yield
    engine.dispose()
