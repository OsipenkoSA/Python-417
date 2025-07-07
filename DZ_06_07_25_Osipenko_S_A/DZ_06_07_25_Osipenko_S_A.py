import os

from models.database import DATABASE_NAME
from models.database import Session, create_db
from faker import Faker
from models.student import Student


def create_database(load_faker_data=True):
    create_db()
    if load_faker_data:
        _load_faker_data(Session())


def _load_faker_data(session):
    faker = Faker('ru_RU')
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(16, 25)
        ball = faker.random.randint(3, 5)
        students = Student(full_name, age, ball)
        session.add(students)
    session.commit()
    session.close()


if __name__ == '__main__':
    db_is_creator = os.path.exists(DATABASE_NAME)
    if not db_is_creator:
        create_database()
