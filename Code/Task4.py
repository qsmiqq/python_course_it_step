"""
Напишите класс Circle, представляющий круг. У этого класса должны быть:
конструктор принимающий объект класса Point, точку центра круга, и число, радиус круга;
атрибуты center и radius, возвращающие центр и радиус круга соответственно;
метод square, который возвращает площадь круга.

пи * р**2

circ = Circle(Point(0, 3), 4)
circ.radius == 4
circ.center.x == 0

Circle(Point(0, 0), 0).square() == 0
"""

from math import sqrt, pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return sqrt(pow((self.x - point.x), 2) + pow((self.y - point.y), 2))


class Circle:
    def __init__(self, point: Point, radius: int):
        self.center = point
        self.radius = radius

    def get_square(self):
        return pi * pow(self.radius, 2)


circ = Circle(Point(0, 3), 4)
print(circ.radius)
print(circ.center.y)
print(round(circ.get_square(), 2))
