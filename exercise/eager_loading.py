"""Simplifies joins and other functions on a query"""
from sqlalchemy.orm import joinedload, subqueryload, contains_eager

from exercise.models import User, Address
from exercise.query import get_from

# joinedload in options
# users = User.query.options(joinedload(User.addresses)).all()
# get_from(users)
# for user in users:
#     for i in user.addresses:
#         print(f"Name: {user.first_name}, Street: {i.street}")

#subqueryload in options
# users = User.query.options(subqueryload(User.preference)).all()
# for user in users:
#     print(f"{user.first_name} {user.preference}")

"""the preference object cannot be iterated on because of the uselist=False constraint"""

# contains eager
# used when the join has been explicitly stated

# users = User.query.join(User.addresses).options(contains_eager(User.addresses)).all()
# for user in users:
#     for u in user.addresses:
#         print(F"First Name: {user.first_name}, Street: {u.street}")

users = User.query.join(User.addresses).filter(
    Address.local_government_area == 'Jos South').options(contains_eager(User.addresses)).all()
for user in users:
    print(user.addresses)

"""filters are case sensitive beware!!!"""
