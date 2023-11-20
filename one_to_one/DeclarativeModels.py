from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from one_to_one.connect import Base, engine


class Teacher(Base):
    """requires two arguments
    firstname: str
    lastname: str"""
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column(String(20), nullable=False)
    lastname: Mapped[str] = mapped_column(String(20), nullable=False)
    contract: Mapped["Contract"] = relationship(back_populates="teacher", uselist=False, cascade="all, delete, "
                                                                                                 "delete-orphan")

    def __repr__(self):
        return f"{__class__.__name__}, firstname: {self.firstname}, lastname: {self.lastname}"


class Contract(Base):
    """requires one argument
    salary: int"""
    __tablename__ = "contracts"
    id: Mapped[int] = mapped_column(primary_key=True)
    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id", ondelete="CASCADE"))
    teacher: Mapped["Teacher"] = relationship(back_populates="contract", single_parent=True)

    def __repr__(self):
        return f"{__class__.__name__}, salary: {self.salary}.00 N"


Base.metadata.create_all(engine)
