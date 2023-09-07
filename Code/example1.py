"""
Создать класс Point с конструктором в разных системах координат
"""
from enum import Enum
from math import *


class CordinatSystem(Enum):
    DEKART = 0
    POLAR = 1


# class Point:
#     def __init__(self, a, b, system=CordinatSystem.DEKART):
#         if system == CordinatSystem.DEKART:
#             self.x = a
#             self.y = b
#         elif system == CordinatSystem.POLAR:
#             self.x = a * sin(b)
#             self.y = a * cos(b)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_point_dekart(x, y):
        return Point(x, y)

    @staticmethod
    def new_point_polar(x, y):
        return Point(x * sin(y), x * cos(y))

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


pnt = Point(5, 3)
print(pnt)
print(pnt.new_point_dekart(2, 3))
print(pnt.new_point_polar(4, 7))
