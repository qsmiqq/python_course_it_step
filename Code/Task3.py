"""
Реализуйте класс Point (точка). У этого класса должны быть
конструктор, принимающий два числа x и y, координаты точки на плоскости;
атрибуты x и y через которые можно будет получить координаты точки;
метод dist, который принимает еще один объект класса Point
и находит эвклидово расстояние между двумя точками.

Эвклидово рвсстояние
sqrt((x1 - point.x)**2 + (y1 - point.y)**2)

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
p1.dist(p2) == 1
"""
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, point):
        return math.sqrt(pow((self.x - point.x), 2) + pow((self.y - point.y), 2))


p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2))