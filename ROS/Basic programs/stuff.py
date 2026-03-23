from math import pi

class Square:
    def __init__(self, side_value=6):
        self.side = side_value
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return self.side * 4
    def __str__(self):
        return f"Square with side {self.side}:\n - Area: {self.area():.2f}\n - Perimeter: {self.perimeter():.2f}"
class Circle:
    def __init__(self, radius=4):
        self.radius = radius
    def area(self):
        return pi * self.radius**2    
    def perimeter(self):
        return 2 * pi * self.radius     
    def __str__(self):
        return f"Circle with radius {self.radius}:\n - Area: {self.area():.2f}\n - Circumference: {self.perimeter():.2f}"
s1 = Circle(3)
print(s1)
s2 = Square(5)
print(s2)