from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

url = f"sqlite:///Enterprise"

engine = create_engine(url, echo=True)

Base = declarative_base()

Base.metadata.create_all(engine)

