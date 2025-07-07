import os

from models.database import DATABASE_NAME
from models.database import Session, create_db
from faker import Faker
from models.buyers import Buyers


def create_database(load_faker_data=True):
    create_db()
    if load_faker_data:
        _load_faker_data(Session())


def _load_faker_data(session):
    faker = Faker('ru_RU')
    automobile_list = ["Audi", "BMW", "Mercedes", "Volkswagen", "Skoda", "Renault", "Peugeot"]
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        avto = faker.random.choice(automobile_list)
        price = faker.random.randint(15000, 40000)
        buyers = Buyers(full_name, avto, price)
        session.add(buyers)
    session.commit()
    session.close()


if __name__ == '__main__':
    db_is_creator = os.path.exists(DATABASE_NAME)
    if not db_is_creator:
        create_database()
