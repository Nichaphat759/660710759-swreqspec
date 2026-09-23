import importlib.util
import os
from pathlib import Path

from sqlalchemy import inspect
from sqlalchemy import create_engine

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app.config import get_database_url


def load_migration_module():
    module_path = Path(__file__).resolve().parents[1] / "app" / "db" / "migrations" / "001_init.py"
    spec = importlib.util.spec_from_file_location("migration_001_init", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_database_url_reads_env():
    assert get_database_url() == "sqlite:///:memory:"


def test_upgrade_creates_required_tables():
    engine = create_engine("sqlite:///:memory:")
    migration = load_migration_module()

    migration.upgrade(engine)

    inspector = inspect(engine)
    tables = set(inspector.get_table_names())

    assert {"slots", "bookings", "audit_logs"}.issubset(tables)
    assert inspector.get_columns("bookings")
    assert inspector.get_columns("audit_logs")
