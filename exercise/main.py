import os

from sqlalchemy import create_engine, Engine, event
from sqlalchemy.orm import scoped_session, sessionmaker

Base_DIR = os.path.dirname(os.path.abspath(__file__))

engine = create_engine(f'sqlite:///{Base_DIR}/Enterprise2', echo=True)

session = scoped_session(sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
))


@event.listens_for(Engine, 'connect')
def set_sql_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()

