
class Student:
    def __init__(self, name):
        self.name = name

    class Laptop:
        def __init__(self, student):
            self.model = "HP"
            self.cpu = "i7"
            self.ram = 16
            self.student = student

        def print_info(self):
            print(f"{self.student.name} => {self.model}, {self.cpu}, {self.ram}")


student1 = Student("Roman")
show1 = student1.Laptop(student1)
show1.print_info()
student2 = Student("Vladimir")
show2 = student2.Laptop(student2)
show2.print_info()
