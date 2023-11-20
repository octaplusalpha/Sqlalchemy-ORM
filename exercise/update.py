from exercise.main import session
from exercise.models import Preference, User

"""to update:
query the relevant table then join it to its parent table to effect changes based on its relationship
filter to obtain the required user and store the result in a variable
assign the new value to the answer variable.column then close the connection"""

# user_preference = Preference.query.join(Preference.user).filter(User.email == 'jacksonakwasi@gmail.com').first()
# print(user_preference)
# user_preference.currency = 'GCD'
# session.commit()
# print(user_preference)

# alternatively
# user = User.query.filter(User.last_name == 'Okafor').update({'email': 'gokafor@hotmail.com'})
# session.commit()

user = User.query.filter_by(email='gokafor@hotmail.com').one()
print(user)
session.close()
