import uuid
from enum import Enum as PyEnum, unique

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Enum,
    Float,
    ForeignKey,
    Integer,
    Sequence,
    String,
    Table,
    func
)
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from .base import AuditMixin, Base

class FiringType(PyEnum):
    SIGHTERS = "sighters"
    MATCH = "match"
    SINGLE_SHOT = "single_shot"
    RAPID_FIRE = "rapid_fire"
    FINISHED = "finished"
    CANCELLED = "cancelled"

club_country_association = Table("club_country_association", Base.metadata,
    Column("club_id", ForeignKey("shooting_club.id")),
    Column("country_id", ForeignKey("country.id"))
)

club_range_association = Table("club_range_association", Base.metadata,
    Column("club_id", ForeignKey("shooting_club.id")),
    Column("range_id", ForeignKey("shooting_range.id"))
)

range_shooter_association = Table("range_shooter_association", Base.metadata,
    Column("range_id", ForeignKey("shooting_range.id")),
    Column("shooter_id", ForeignKey("range_event_shooter.id"))
)

class Country(Base):
    __tablename__ = "country"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    shortname = Column(String, unique=True)

    def __init__(self, name: str, shortname: str) -> None:
        self.name = name
        self.shortname = shortname

class ShootingClub(AuditMixin, Base):
    __tablename__ = "shooting_club"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True)
    shortname = Column(String, unique=True)
    country = relationship("Country", secondary=club_country_association, lazy="joined")

class ShootingRange(AuditMixin, Base):
    __tablename__ = "shooting_range"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    club = relationship("ShootingClub", secondary=club_range_association, lazy="joined")
    name = Column(String)
    lanes = Column(Integer)
    first_lane = Column(Integer)

class RangeEventShooter(AuditMixin, Base):
    __tablename__ = "range_event_shooter"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")
    range_shooter_id = Column(Integer)
    name = Column(String)
    team = Column(String)
    class_ = Column('class', String)
    lane_id = Column(Integer)

class RangeEventPractice(AuditMixin, Base):
    __tablename__ = "range_event_practice"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")
    range_shooter_id = Column(Integer)
    sequence_number = Column(Integer)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=func.now())
    event_type = Column(Integer)
    practice_sequence_number = Column(Integer)
    shoot_code = Column(Integer)
    practice_code = Column(Integer)
    
class RangeEventGroup(AuditMixin, Base):
    __tablename__ = "range_event_group"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")
    range_shooter_id = Column(Integer)
    sequence_number = Column(Integer)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=func.now())
    event_type = Column(Integer)
    group_ordinal = Column(Integer)
    firing_type = Column(Enum(FiringType), nullable=False, index=True)
    expected_number_of_shots = Column(Integer)
    
class RangeEventShot(AuditMixin, Base):
    __tablename__ = "range_event_shot"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")
    range_shooter_id = Column(Integer)
    sequence_number = Column(Integer)
    timestamp = Column(TIMESTAMP, nullable=False, server_default=func.now())
    shot_id = Column(Integer)
    shot_value = Column(Integer)
    shot_value_decimal = Column(Integer)
    x_coord = Column(Float)
    y_coord = Column(Float)
    shot_timestamp = Column(Integer)
    caliber = Column(Integer)
    shot_attr = Column(Integer)
