import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base
from exercise.main import session

Model = declarative_base()
Model.query = session.query_property()


class TimeStampedModel(Model):
    __abstract__ = True
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
    updated_at = Column(DateTime, onupdate=datetime.datetime.now(datetime.UTC))
