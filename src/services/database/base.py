from sqlalchemy import TIMESTAMP, Column, func
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class AuditMixin(object):
    created_date = Column(TIMESTAMP, server_default=func.now())
    modified_date = Column(TIMESTAMP, server_default=func.now())