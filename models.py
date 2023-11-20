from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine("mysql+mysqlconnector://root:mistique@127.0.0.1/school", echo=True)

Model = declarative_base()


class Student(Model):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)


Model.metadata.create_all(engine)
