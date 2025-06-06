from . import a_car


class ElCar(a_car.AutoCar):
    def __init__(self, brand, model, year, mileage):
        super().__init__(brand, model, year, mileage)

    def print_info(self):
        super().print_info()
        print("Этот автомобиль имеет мощность 100%")
