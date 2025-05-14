class Automobile:
    def __init__(self, model, year, company, power, color, price):
        self.__model = model
        self.__year = year
        self.__company = company
        self.__power = power
        self.__color = color
        self.__price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print("Название модели:", self.__model)
        print("Год выпуска:", self.__year)
        print("Производитель:", self.__company)
        print("Мощность двигателя:", self.__power, "Л.С.")
        print("Цвет машины:", self.__color)
        print("Цена:", self.__price)
        print("=" * 40)

    def set_model(self, model):
        if isinstance(model, str):
            self.__model = model
        else:
            print("Модель должна быть строковым значением")

    def get_model(self):
        return self.__model

    def set_year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            print("Год должен быть числом")

    def get_year(self):
        return self.__year

    def set_company(self, company):
        if isinstance(company, str):
            self.__company = company
        else:
            print("Название производителя должно быть строковым значением")

    def get_company(self):
        return self.__company

    def set_power(self, power):
        if isinstance(power, int):
            self.__power = power
        else:
            print("Мощность должна быть числом")

    def get_power(self):
        return self.__power

    def set_color(self, color):
        if isinstance(color, str):
            self.__color = color
        else:
            print("Цвет должен быть строковым значением")

    def get_color(self):
        return self.__color

    def set_price(self, price):
        if isinstance(price, (int, float)):
            self.__price = price
        else:
            print("Цена должна быть числом")

    def get_price(self):
        return self.__price


auto = Automobile("X7 M50i", 2021, "BMW", 530, "white", 10790000)
auto.print_info()
