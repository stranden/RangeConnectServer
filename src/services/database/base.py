import settings
from sqlalchemy import MetaData, TIMESTAMP, Column, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base(metadata=MetaData(schema=settings.DATABASE_SCHEMA))
metadata = Base.metadata

class AuditMixin(object):
    created_date = Column(TIMESTAMP, server_default=func.now())
    modified_date = Column(TIMESTAMP, server_default=func.now())