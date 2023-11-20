from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from one_to_one.connect import engine

Base = declarative_base()


class User(Base):
    """requires two arguments
    username: str
    password: str"""
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    profile = relationship("UserProfile", back_populates="user", uselist=False, cascade="all, delete, delete-orphan")

    def __repr__(self):
        return f"{__class__.__name__}, Username: {self.username}, Password: {self.password}"


class UserProfile(Base):
    """requires one argument
    bio: str  - a brief description of the user
    """
    __tablename__ = "userprofiles"
    id = Column(Integer, primary_key=True)
    bio = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id",  ondelete="CASCADE"))
    user = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"{__class__.__name__}, bio: {self.bio}"


Base.metadata.create_all(engine)
