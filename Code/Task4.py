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
    pass


class Circle:
    pass


# circ = Circle(Point(0, 3), 4)
# print(circ.radius)
# print(circ.center.x)
# print(circ.get_square())