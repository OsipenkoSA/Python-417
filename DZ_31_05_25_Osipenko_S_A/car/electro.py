import tesla_car


class ElectroCar(tesla_car.Automobile):
    def __init__(self, brand, model, year, mileage, power):
        super().__init__(brand, model, year, mileage)
        self.power = power

    def print_info(self):
        super().print_info()
        print(f"Этот автомобиль имеет мощность {self.power}%")
