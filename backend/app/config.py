import os


def get_database_url() -> str:
    """Read the database URL for the booking system.
    Supports CON-TECH-01 by allowing PostgreSQL in production and SQLite in tests.
    """
    return os.getenv("DATABASE_URL", "sqlite:///./booking.db")
