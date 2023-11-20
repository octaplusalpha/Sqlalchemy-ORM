from sqlalchemy.exc import NoResultFound

from one_to_one.DeclarativeModels import Teacher, Contract
from one_to_one.addrecords import session
from one_to_one.models import User

# try:
#     result = session.query(User).filter(User.id == 1).all()
# except NoResultFound as e:
#     print(e)
#     session.rollback()
# else:
#     print(result)

# try:
#     result = session.query(Contract).filter(Contract.salary == 10000).one()
# except NoResultFound as e:
#     print(e)
#     session.rollback()
# else:
#     print(result)

# getting a user by id use...

teacher = session.get(Teacher, 1)
print(teacher)

