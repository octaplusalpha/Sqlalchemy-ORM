from exercise.main import session
from exercise.models import User, Preference, Address, Role
# create a user using  class instantiation
user = User()
user.first_name = 'Bestlife'
user.last_name = 'Ineye'
user.email = 'bestlifeineye@gmail.com'

"""**kwargs can be used like the rest 
user = User(
first_name = 'moses;
last_name = 'adik'
email = mosesadik@gmail.com"""

# the user to preference is a one-to-one relationship where there is no list but a single record on both sides
user.preference = Preference(language='Ijaw', currency='NGN')

# the user to address relationship is a one-to-many which implies that a list
# will be returned for a user so the append keyword is used
user.addresses.append(Address(street='frankfurt ', ward=9, local_government_area='Ikwerre'))

# the roles relationship is a many-to-many which implies that a list can be returned in both direction.
user.roles.append(Role(name='Supervisor', slug= 'Ast-Supol' ))
session.add(user)
session.commit()
