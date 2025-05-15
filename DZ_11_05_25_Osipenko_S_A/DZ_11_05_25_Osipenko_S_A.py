class Area:
    __count = 0

    @staticmethod
    def s_heron(a, b, c):
        Area.__count += 1
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    @staticmethod
    def s_base_height(a, h):
        Area.__count += 1
        return (a * h) / 2

    @staticmethod
    def s_square(a):
        Area.__count += 1
        return a ** 2

    @staticmethod
    def s_rectangle(a, b):
        Area.__count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.__count


s1 = Area.s_heron(3, 4, 5)
print("Площадь треугольника по формуле Герона:", s1)
s2 = Area.s_base_height(6, 7)
print("Площадь треугольника через основание и высоту:", s2)
s3 = Area.s_square(7)
print("Площадь квадрата:", s3)
s4 = Area.s_rectangle(2, 6)
print("Площадь прямоугольника:", s4)
print("Количество подсчетов площади:", Area.get_count())

