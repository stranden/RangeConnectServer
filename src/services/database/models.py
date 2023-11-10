import uuid
from enum import Enum as PyEnum

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    func
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .base import AuditMixin, Base

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
    staus = Column(Integer, nullable=False, default=0)


class EventRange(Base):
    __tablename__ = "event_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    event = Column(postgresql.UUID(as_uuid=True), ForeignKey("event.id"), nullable=True, index=True)
    shooting_range = Column(postgresql.UUID(as_uuid=True), ForeignKey("shooting_range.id"), nullable=True, index=True)


class RangeManufactor(AuditMixin, Base):
    __tablename__ = "manufactor"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
