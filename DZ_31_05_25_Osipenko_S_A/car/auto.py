class Automobile:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def print_info(self):
        print(f"{self.brand} {self.model} {self.year} год {self.mileage} км.")


# class ElectroCar(Automobile):
#     def __init__(self, brand, model, year, mileage, power):
#         super().__init__(brand, model, year, mileage)
#         self.power = power
#
#     def print_info(self):
#         super().print_info()
#         print(f"Этот автомобиль имеет мощность {self.power}%")
