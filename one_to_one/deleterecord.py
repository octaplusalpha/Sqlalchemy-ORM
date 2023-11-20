from sqlalchemy.exc import NoResultFound

from one_to_one.addrecords import session
from one_to_one.models import User

result = session.query(User).where(User.id >= 13).all()
try:
    session.delete(result)
except NoResultFound as e:
    print(e)
    session.rollback()
else:
    session.commit()