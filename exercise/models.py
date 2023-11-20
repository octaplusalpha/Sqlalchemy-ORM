from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Relationship
from exercise.base import TimeStampedModel, Model
from exercise.main import engine


# create the user
class User(TimeStampedModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False, unique=True)

    preference = Relationship('Preference', back_populates='user', uselist=False, passive_deletes=True)
    addresses = Relationship('Address', back_populates='user', passive_deletes=True)
    roles = Relationship('Role', secondary='users_roles', back_populates='user', passive_deletes=True)

    def __repr__(self):
        return f'{self.__class__.__name__}, first name: {self.first_name}, last name: {self.last_name} email:{self.email}'


# one-to-one relationship with user
class Preference(TimeStampedModel):
    __tablename__ = 'preferences'
    id = Column(Integer, primary_key=True, autoincrement=True)
    language = Column(String(20), nullable=False)
    currency = Column(String(3), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), index=True, unique=True, nullable=False)

    user = Relationship('User', back_populates='preference')

    def __repr__(self):
        return f'{self.__class__.__name__}, Language: {self.language}, Currency: {self.currency}'


# one-to-many relationship
class Address(TimeStampedModel):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    street = Column(String(80), nullable=False)
    ward = Column(Integer, nullable=False)
    local_government_area = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), index=True, nullable=False)

    user = Relationship('User', back_populates='addresses')

    def __repr__(self):
        return f'{self.__class__.__name__}, Street: {self.street}, Ward: {self.ward}, L.G.A: {self.local_government_area}'


# many-to-many relationship which requires a pivot table
class Role(Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    slug = Column(String(20), unique=True, nullable=False)

    user = Relationship('User', secondary='users_roles', back_populates='roles', passive_deletes=True)

    def __repr__(self):
        return f'{self.__class__.__name__}, Slug: {self.slug}'


class UsersRoles(TimeStampedModel):
    __tablename__: str = 'users_roles'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id', ondelete='CASCADE'), primary_key=True)


if __name__ == "__main__":
    Model.metadata.create_all(engine)
