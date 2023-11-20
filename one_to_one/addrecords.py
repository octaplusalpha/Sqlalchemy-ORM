from sqlite3 import OperationalError
from sqlalchemy.orm import sessionmaker

from one_to_one.DeclarativeModels import Teacher, Contract
from one_to_one.connect import engine
from one_to_one.models import User, UserProfile

bio = "i am a disk jockey aspiring to entertain the world with music"

Session = sessionmaker(engine)
session = Session()

# user3 = User(username="sparkoblaze", password="finest01")
# profile = UserProfile(bio=bio, user=user3)


# Declarative method data insertion

# teacher3 = Teacher(firstname="Boma", lastname="Greg")
# salary = Contract(salary=10000, teacher=teacher3)
#
# try:
#     session.add(teacher3)
# except OperationalError as e:
#     print(e)
#     session.rollback()
# else:
#     session.commit()

