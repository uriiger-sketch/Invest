from __future__ import annotations

from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from .config import get_settings

_engines: dict[str, Engine] = {}
_session_factories: dict[str, sessionmaker[Session]] = {}


def get_engine() -> Engine:
    url = get_settings().db_url
    if url not in _engines:
        _engines[url] = create_engine(
            url,
            future=True,
            connect_args={"check_same_thread": False} if url.startswith("sqlite") else {},
        )
    return _engines[url]


def get_session_factory() -> sessionmaker[Session]:
    url = get_settings().db_url
    if url not in _session_factories:
        _session_factories[url] = sessionmaker(
            bind=get_engine(), expire_on_commit=False, future=True
        )
    return _session_factories[url]


@contextmanager
def session_scope() -> Iterator[Session]:
    Session_ = get_session_factory()
    session = Session_()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init_db() -> None:
    """Create all tables (used in tests; production uses alembic)."""
    from .models import Base

    Base.metadata.create_all(get_engine())
