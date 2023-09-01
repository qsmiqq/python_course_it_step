"""
Доработаем класс Circle.
Добавьте ему метод is_intersect, который будет принимать другой объект класса Circle
и возвращать True или False в зависимости от того, пересекаются круги или нет.

Круги пересекаются, если эвклидово расстояние (метод dist) между центрами меньше суммы двух радиусов
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

    def is_intersect(self, circle):
        sum_radius = self.radius + circle.radius
        return self.center.dist(circle.center) < sum_radius


circ1 = Circle(Point(0, 3), 4)
circ2 = Circle(Point(1, 3), 1)
# print(circ1.radius)
# print(circ1.center.dist(circ2.center))
print(circ1.is_intersect(circ2))
