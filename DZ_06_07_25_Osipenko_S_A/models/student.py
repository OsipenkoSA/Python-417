from sqlalchemy import Column, Integer, String
from models.database import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    ball = Column(Integer)

    def __init__(self, full_name, age, ball):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.ball = ball

    def __repr__(self):
        return (f"Студент (ФИО: {self.surname} {self.name} {self.patronymic}, Возраст: {self.age}, "
                f"Средний балл: {self.ball})")
