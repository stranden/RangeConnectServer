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
    SHOOTOFF = "shootoff"


class RangeEventShooter(AuditMixin, Base):
    __tablename__ = "range_event_shooter"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range_id = Column(postgresql.UUID(as_uuid=True), primary_key=True, nullable=False, index=True)
    firing_point = Column(String, nullable=False)
    start_number = Column(String, nullable=False)
    name = Column(String, nullable=False)
    club = Column(String, nullable=True)
    group = Column(String, nullable=True)


class RangeEventShot(AuditMixin, Base):
    __tablename__ = "range_event_shot"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range_id = Column(postgresql.UUID(as_uuid=True), primary_key=True, nullable=False, index=True)
    firing_point = Column(String, nullable=False)
    start_number = Column(String, nullable=False)
    series_type = Column(Enum(SeriesType), nullable=False)
    shot_id = Column(Integer, nullable=False)
    shot_value = Column(Float, nullable=False)
    shot_value_decimal = Column(Float, nullable=False)
    x_coord = Column(Float, nullable=False)
    y_coord = Column(Float, nullable=False)

