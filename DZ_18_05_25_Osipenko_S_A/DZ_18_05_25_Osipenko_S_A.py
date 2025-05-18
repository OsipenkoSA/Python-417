
class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def print_info(self):
        print(self.surname, self.name, self.age, end=" ")


class Student(Human):
    def __init__(self, surname, name, age, spec, group, score):
        super().__init__(surname, name, age)
        self.spec = spec
        self.group = group
        self.score = score

    def print_info(self):
        super().print_info()
        print(self.spec, self.group, self.score, end=" ")


class Teacher(Human):
    def __init__(self, surname, name, age, spec, score):
        super().__init__(surname, name, age)
        self.spec = spec
        self.score = score

    def print_info(self):
        super().print_info()
        print(self.spec, self.score)


class Graduate(Student):
    def __init__(self, surname, name, age, spec, group, score, project):
        super().__init__(surname, name, age, spec, group, score)
        self.project = project

    def print_info(self):
        super().print_info()
        print(self.project)


h1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
h1.print_info()
print()
h2 = Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5)
h2.print_info()
print()
h3 = Graduate("Батодалаев", "Даши", 16, "ГК", "Web_011", 5,
              "Защита персональных данных")
h3.print_info()
h4 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
h4.print_info()
h5 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
h5.print_info()
print()
h6 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
h6.print_info()
