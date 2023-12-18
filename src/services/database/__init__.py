import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models import * # noqa


engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True, future=True) # echo=True to view sql queries in logs

DBSession: Session = sessionmaker(bind=engine, future=True)
