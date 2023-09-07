"""O - opening"""
from math import *
from abc import ABC, abstractmethod


# class Figure:
#     def __init__(self, shape, **kwargs):
#         self.shape = shape
#         if self.shape == "rectangle":
#             self.w = kwargs["w"]
#             self.h = kwargs["h"]
#         elif self.shape == "circle":
#             self.r = kwargs["r"]
#         else:
#             pass
#
#     def calculate_area(self):
#         if self.shape == "rectangle":
#             return self.w * self.h
#         elif self.shape == "circle":
#             return pi * pow(self.r, 2)
#
#
# fig1 = Figure("rectangle", w=5, h=6)
# print(fig1.calculate_area())


class Figure(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, w, h):
        super().__init__("rectangle")
        self.w = w
        self.h = h

    def calculate_area(self):
        return self.w * self.h

    def __str__(self):
        return f"{self.shape_name};{self.w};{self.h}"


class Circle(Figure):
    def __init__(self, r):
        super().__init__("circle")
        self.r = r

    def calculate_area(self):
        return pi * pow(self.r, 2)


fig1 = Rectangle(5, 6)

print(fig1)
print(fig1.shape_name)
print(fig1.calculate_area())
