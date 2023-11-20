from exercise.main import session
from exercise.models import User
from exercise.query import get_from

del_one = User.query.filter(User.id == 2).one()
session.delete(del_one)
session.commit()
