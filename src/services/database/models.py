import uuid
from enum import Enum as PyEnum, unique

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Enum,
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

class ShootingState(PyEnum):
    SIGHTERS = "sighters"
    MATCH = "match"
    FINISHED = "finished"
    CANCELLED = "cancelled"

class ShootingType(PyEnum):
    SINGLE_SHOT = "single_shot"
    RAPID_FIRE = "rapid_fire"

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
    name = Column(String)
    lanes = Column(Integer)
    first_lane = Column(Integer)
    club = relationship("ShootingClub", secondary=club_range_association, lazy="joined")

class RangeEventShooter(AuditMixin, Base):
    __tablename__ = "range_event_shooter"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String)
    lane_id = Column(Integer)
    range_shooter_id = Column(Integer)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")

class RangeEventTeam(AuditMixin, Base):
    __tablename__ = "range_event_team"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    name = Column(String)
    lane_id = Column(Integer)
    range_shooter_id = Column(Integer)
    shooting_range = relationship("ShootingRange", secondary=range_shooter_association, lazy="joined")
