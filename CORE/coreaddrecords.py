from sqlalchemy import insert
from CORE.coreconnect import engine
from coreaddrecord import student, grade

# single insert record
stmt = insert(student).values(first_name='Charles', last_name='Friday')

fktable = insert(grade)
# student.grade.append(grade_level='creche', grade_arm='A',)

# multiple insert records

records = [
    {'first_name': 'Confidence', 'last_name': 'Ubani'},
    {'first_name': 'Michael', 'last_name': 'Onyeaju'},
    {'first_name': 'David', 'last_name': 'Onyeaju'},
    {'first_name': 'Reward', 'last_name': 'Wali'},
    {'first_name': 'Tobi', 'last_name': 'Adewale'},
]
multiple_record_stmt = insert(student).values(records)

if __name__ == "__main__":
    # single data commit to database for persistence
    with engine.connect() as conn:
        ref = conn.execute(fktable)
        print(ref)
