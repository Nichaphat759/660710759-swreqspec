from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Text, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Slot(Base):
    """Stores a time slot and remaining capacity. Supports FR-BKG-01 and FR-BKG-06."""
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True)
    slot_date = Column(String, nullable=False)
    start_time = Column(String, nullable=False)
    package_code = Column(String, nullable=False)
    capacity = Column(Integer, nullable=False)
    remaining = Column(Integer, nullable=False)


class Booking(Base):
    """Stores patient booking records without storing national ID. Supports IF-HIS-01."""
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    hn = Column(String, nullable=False)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=False)
    booking_date = Column(String, nullable=False)
    queue_no = Column(String, nullable=True)
    status = Column(String, nullable=False, default="booked")
    created_at = Column(DateTime, nullable=False)


class AuditLog(Base):
    """Tracks access to booking data. Supports DOM-PDPA-01."""
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    actor_id = Column(String, nullable=False)
    action = Column(String, nullable=False)
    hn = Column(String, nullable=False)
    accessed_at = Column(DateTime, nullable=False)
    details = Column(Text, nullable=True)


def upgrade(engine):
    """Create initial schema for slots, bookings, and audit logs."""
    Base.metadata.create_all(bind=engine)
