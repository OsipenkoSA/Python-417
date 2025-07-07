from sqlalchemy import Column, Integer, String
from models.database import Base


class Buyers(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    automobile = Column(String(250), nullable=False)
    price = Column(Integer)

    def __init__(self, full_name, automobile, price):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.automobile = automobile
        self.price = price

    def __repr__(self):
        return (f"Покупатель (ФИО: {self.surname} {self.name} {self.patronymic}, Купил автомобиль: {self.automobile}, "
                f"Цена: {self.price})")
