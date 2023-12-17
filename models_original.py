import uuid
from enum import Enum as PyEnum

from sqlalchemy import (
    
    Column,
    Enum,
    Float,
    ForeignKey,
    func,
    Integer,
    String,
    Table,
    TIMESTAMP
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .base import AuditMixin, Base, metadata

class SeriesType(PyEnum):
    SIGHT = "sight"
    MATCH = "match"


class Country(Base):
    __tablename__ = "country"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)


class ShootingClub(Base):
    __tablename__ = "shooting_club"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    country = Column(postgresql.UUID(as_uuid=True), ForeignKey("country.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    shortname = Column(String, nullable=True)


class Event(Base):
    __tablename__ = "event"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_club = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_club.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    startdate =  Column(TIMESTAMP, nullable=False)
    enddate =  Column(TIMESTAMP, nullable=False)
    status = Column(Integer, nullable=False, default=0)


class EventRange(Base):
    __tablename__ = "event_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    event = Column(postgresql.UUID(as_uuid=True), ForeignKey("event.id"), nullable=True, index=True)
    shooting_range = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_range.id"), nullable=True, index=True)


class Manufactor(AuditMixin, Base):
    __tablename__ = "manufactor"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)


class ShootingRange(Base):
    __tablename__ = "shooting_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_club = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_club.id"), nullable=True, index=True)
    manufactor = Column(postgresql.UUID(as_uuid=True), ForeignKey("manufactor.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    lanes = Column(Integer, nullable=False)
    first_lane = Column(String, nullable=False)


class ShootingRange(Base):
    __tablename__ = "shooting_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_club = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_club.id"), nullable=True, index=True)
    manufactor = Column(postgresql.UUID(as_uuid=True), ForeignKey("manufactor.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    lanes = Column(Integer, nullable=False)
    first_lane = Column(String, nullable=False)


class RangeEventShooter(AuditMixin, Base):
    __tablename__ = "range_event_shooter"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_range.id"), nullable=True, index=True)
    start_number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    club = Column(String, nullable=True)
    group = Column(String, nullable=True)


class RangeEventShot(AuditMixin, Base):
    __tablename__ = "range_event_shot"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_range.id"), nullable=False, index=True)
    start_number = Column(Integer, nullable=False)
    series_type = Column(Enum(SeriesType), nullable=False)
    shot_id = Column(Integer, nullable=False)
    shot_value = Column(Integer, nullable=False)
    shot_value_decimal = Column(Float, nullable=False)
    x_coord = Column(Float, nullable=False)
    y_coord = Column(Float, nullable=False)

