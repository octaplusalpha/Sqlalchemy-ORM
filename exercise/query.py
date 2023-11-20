from sqlalchemy import desc

from exercise.main import session
from exercise.models import User, Address


def get_from(result):
    for i in result:
        print(i)


# get all users
# all_users = User.query.all()
# for user in all_users:
#     print(all_users)

# get the first user
# first_user = User.query.first()
# print(first_user)

# filtering by specific attribute
# result = User.query.filter_by(id=2).all()
# print(result)

# filtering by filter key word as opposed to the filter_by keyword
# result1 = User.query.filter(User.first_name == 'Bestlife').one()
# print(result1)

# filtering by regular expressions
# gmail_users = User.query.filter(User.email.like('%@gmail.com')).all()
# print(gmail_users)

# the 'ilike' keyword turns all strings to lower case

# two table query based on relationships
# here we find all users who reside in ikwerre lga
# result = User.query.join(User.addresses).filter(Address.local_government_area == 'Ikwerre').all()
# for user in result:
#     print(user)

# ordering query
# order_by_f_name = User.query.order_by(User.first_name).all()
# for user in order_by_f_name:
#     print(user.first_name)

# desc_order = User.query.order_by(desc(User.first_name)).all()
# for user in desc_order:
#     print(user.first_name)

# order by two columns in case the two have the same first name
# orderby2 = User.query.order_by(desc(User.first_name)).order_by(desc(User.last_name)).all()
# for user in orderby2:
#     print(user.first_name, user.last_name)

# get first three records by using limit
# first3 = User.query.limit(3).all()
# get_from(first3)

# using limit after sort
# order_by_f_name = User.query.order_by(User.first_name).limit(2).all()
# get_from(order_by_f_name)

# using offset to pick a start point for a query
# skipped2 = User.query.offset(2).all()
# get_from(skipped2)
# result returns a limit of  -1? why? i only asked for offset. find out!!!

# counting entries
# user_count = User.query.count()
# print(user_count)

session.close()
