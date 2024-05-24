from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            self.radius = 0
            print("Warning: Radius cannot be negative. Setting radius to 0.")
        else:
            self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


try:
    circle = Circle(5)
    shape_info(circle)
except ValueError as e:
    print(e)

try:
    rectangle = Rectangle(4, 6)
    shape_info(rectangle)
except ValueError as e:
    print(e)

try:
    invalid_circle = Circle(-5)
    shape_info(invalid_circle)
except ValueError as e:
    print(e)
