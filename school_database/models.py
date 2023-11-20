from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base
from mysql_url import url_connect

engine = create_engine(url_connect("montessori"))

Model = declarative_base()


class Parent(Model):
    __tablename__: str = "parents"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    address = Column(String(120), nullable=False)


class Teacher(Model):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    address = Column(String(120), nullable=False)


class Student(Model):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)


class GradeLevel(Model):
    __tablename__ = "grade_levels"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


class Subject(Model):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)


Model.metadata.create_all(engine)