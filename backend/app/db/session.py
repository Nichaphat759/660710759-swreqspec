from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_database_url


def get_engine():
    """Create the SQLAlchemy engine using the configured database URL. Supports CON-TECH-01."""
    return create_engine(get_database_url(), future=True)


def get_session_factory():
    """Return a session factory for repository access."""
    return sessionmaker(bind=get_engine(), autoflush=False, autocommit=False, future=True)
