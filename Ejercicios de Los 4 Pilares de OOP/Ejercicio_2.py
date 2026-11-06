from abc import ABC, abstractmethod
import math
from turtle import shape # importamos la biblioteca math para usar funciones matemáticas como pi.

class Shape(ABC):
   
    @abstractmethod # indica que el método area es abstracto y debe ser implementado por las subclases
    def calculate_area(self):
        pass

    @abstractmethod # indica que el método perimeter es abstracto y debe ser implementado por las subclases
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self): 
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(5)
print("Circle Area:", circle.calculate_area())
print(f"Circle Perimeter: {circle.calculate_perimeter()}\n")

square = Square(4)
print("Square Area:", square.calculate_area())
print(f"Square Perimeter: {square.calculate_perimeter()}\n")

rectangle = Rectangle(3, 6)
print("Rectangle Area:", rectangle.calculate_area())
print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}\n")