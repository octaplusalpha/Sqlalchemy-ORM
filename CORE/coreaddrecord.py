from sqlalchemy import Table, Column, String, Integer, ForeignKey
from CORE.coreconnect import mdo, engine

student = Table(
    'students',
    mdo,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(20), nullable=False),
    Column('last_name', String(20), nullable=False),

)


grade = Table(
    'grade',
    mdo,
    Column('id', Integer, primary_key=True),
    Column('grade_level', String(20), nullable=False),
    Column('grade_arm', String(2), nullable=False),
    Column('student_id', ForeignKey('students.id')),

)

if __name__ == "__main__":
    mdo.create_all(engine)