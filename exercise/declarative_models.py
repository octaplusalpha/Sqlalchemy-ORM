from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, Relationship

from exercise.base import TimeStampedModel, Model
from exercise.main import session, engine


class Parent(TimeStampedModel):
    __tablename__ = 'parents'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False)
    address: Mapped[str] = mapped_column(String(150), nullable=False)

    # relationships
    students: Mapped['Student'] = Relationship(
        'students', back_populates='parent', cascade='all, delete - orphan')

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"First Name: {self.first_name} "
                f"Last Name: {self.last_name} "
                f"E,mail: {self.emai} "
                f"Phone; {self.phone}")


class Student(TimeStampedModel):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    parent_id: Mapped[int] = mapped_column(ForeignKey('parents.id', ondelete='CASCADE'))
    grade_level_id: Mapped[int] = mapped_column(ForeignKey('grade_level.id', ondelete='CASCADE'))

    # relationships
    parent: Mapped['Parent'] = Relationship('parent', back_populates='students')
    teachers: Mapped['Teacher'] = Relationship('teachers', secondary='students_teachers', back_populates='students')
    grade_level: Mapped['GradeLevel'] = Relationship('grade_level', back_populates='students')
    grade_arm: Mapped['GradeArm'] = Relationship('grade_arm', back_populates='students')
    subject: Mapped['Subject'] = Relationship('subjects', back_populates='students')
    terms: Mapped['Term'] = Relationship('terms', back_populates='students')

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"First Name: {self.first_name} "
                f"Last Name: {self.last_name} ")


class Teacher(TimeStampedModel):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)

    # relationships
    students: Mapped['Student'] = Relationship('students', secondary='students_teachers', back_populates='teachers')
    grade_arms: Mapped['GradeArm'] = Relationship('grade_arm', secondary='TeachersGradeArm', back_populates='teachers')
    grade_levels: Mapped['GradeLevel'] = Relationship('grade_levels', secondary='TeachersGradeLevel',
                                                      back_populates='teachers')
    subjects: Mapped['Subject'] = Relationship('subjects', secondary='TeacherSubjects', back_populates='teachers')
    profile: Mapped['Profile'] = Relationship('profile', back_populates='teachers', uselist=False)

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"First Name: {self.first_name} "
                f"Last Name: {self.last_name} ")


class Profile(Model):
    __tablename__ = 'profiles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    address: Mapped[str] = mapped_column(String(200), nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    qualification: Mapped[str] = mapped_column(String(25), nullable=False)
    designation: Mapped[str] = mapped_column(String(25), nullable=False)
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))

    # relationships
    teacher: Mapped['Teacher'] = Relationship('teacher', back_populates='profile')

    def __repr__(self):
        return (f"{self.__class__.__name__} "
                f"Address: {self.address} "
                f"Phone: {self.phone} "
                f"E,mail: {self.emai} "
                f"Qualification; {self.qualification}"
                f"Designation; {self.designation}")


class GradeLevel(Model):
    __tablename__ = 'grade_level'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    students_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    # relationships
    students: Mapped['Student'] = Relationship('students', back_populates='grade_level')
    teachers: Mapped['Teacher'] = Relationship('teachers', secondary='TeachersGradeLevel',
                                               back_populates='grade_levels')

    def __repr__(self):
        return f"{self.__class__.__name__} First Name: {self.first_name} "


class GradeArm(Model):
    __tablename__ = 'grade_arm'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(2), nullable=False, unique=True)
    students_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    # relationship
    teachers: Mapped['Teacher'] = Relationship('teachers', secondary='TeachersGradeArm', back_populates='grade_arms')
    students: Mapped['Student'] = Relationship('students', back_populates='grade_arm')

    def __repr__(self):
        return f"{self.__class__.__name__} First Name: {self.first_name} "


class Subject(Model):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(35), nullable=False)
    slug: Mapped[str] = mapped_column(String(35), nullable=False, unique=True)
    students_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    # relationships
    students: Mapped['Student'] = Relationship('students', back_populates='subjects')
    teachers: Mapped['Teacher'] = Relationship('teachers', secondary='TeachersSubjects', back_populates='subjects')
    terms: Mapped['Term'] = Relationship('terms', secondary='SubjectsTerms', back_populates='subjects')

    def __repr__(self):
        return f"{self.__class__.__name__} First Name: {self.name} "


class Term(Model):
    __tablename__ = 'terms'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    slug: Mapped[str] = mapped_column(String(15), nullable=False, unique=True)
    students_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    # relationships
    students: Mapped['Student'] = Relationship('students', back_populates='terms')
    subjects: Mapped['Subject'] = Relationship('subjects', secondary='SubjectsTerms', back_populates='terms')

    def __repr__(self):
        return f"{self.__class__.__name__} First Name: {self.name} "


# pivots
class StudentsTeachers(Model):
    __tablename__ = 'students_teachers'
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), primary_key=True)
    students_id: Mapped[int] = mapped_column(ForeignKey('students.id'), primary_key=True)


class TeachersGradeLevel(Model):
    __tablename__ = 'teachers_grade_level'
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), primary_key=True)
    grade_level_id: Mapped[int] = mapped_column(ForeignKey('grade_level.id'), primary_key=True)


class TeachersGradeArm(Model):
    __tablename__ = 'teacher_grade_arm'
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), primary_key=True)
    grade_arm_id: Mapped[int] = mapped_column(ForeignKey('grade_arm.id'), primary_key=True)


class TeachersSubjects(Model):
    __tablename__ = 'teacher_subjects'
    teachers_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'), primary_key=True)
    subjects_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'), primary_key=True)


class SubjectsTerms(Model):
    __tablename__ = 'subjects_terms'
    terms_id: Mapped[int] = mapped_column(ForeignKey('terms.id'), primary_key=True)
    subjects_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'), primary_key=True)


if __name__ == "__main__":
    session.create_all(engine)
