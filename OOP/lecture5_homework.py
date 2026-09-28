
from abc import ABC, abstractmethod
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [rectangle(6, 23), circle(3.14)]
for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
'''
class employee(ABC):
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    def show_employee(self):
        print(f"Name: {self.name}")
    @abstractmethod
    def calculate_bonus(self):
        return self.salary * 0.1
class Developer(employee):
    def __init__(self, name, salary,lines_of_code):
        super().__init__(name, salary)
        self.lines_of_code = lines_of_code
    def calculate_bonus(self):
        return self.lines_of_code * 0.2
class Salesrep(employee):
    def __init__(self, name, salary,sales_amount):
        super().__init__(name, salary)
        self.sales_amount = sales_amount
    def sales_made(self):
        return self.sales_amount
    def calculate_bonus(self):
        return self.sales_made() * 0.1

dev = Developer("Alice", 80000, 1000)
sales = Salesrep("Bob", 60000, 50000)
dev.show_employee() 
sales.show_employee()
#emptest=Employee("Test", 50000)  # this will raise an error, because employee is an abstract