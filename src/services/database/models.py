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


class Country(Base):
    __tablename__ = "shooting_club"

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, unique=True, index=True, default=uuid.uuid4)
    country = Column(postgresql.UUID(as_uuid=True), ForeignKey("country.id"), nullable=True, index=True)
    name = Column(String, nullable=False)
    shortname = Column(String, nullable=True)

