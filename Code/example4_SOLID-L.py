"""L - Liskov principle"""
from abc import ABC, abstractmethod


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def calculate_area(self):
#         return self.w * self.h
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#     def __setattr__(self, key, value):
#         super().__setattr__(key, value)
#         if key in ("w", "h"):
#             self.__dict__["w"] = value
#             self.__dict__["h"] = value


# square = Square(5)
# print(vars(square))
# square.w = 6
# print(vars(square))
# square.h = 7
# print(vars(square))


class Figure(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Figure):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def calculate_area(self):
        return self.w * self.h


class Square(Figure):
    def __init__(self, a):
        self.a = a

    def calculate_area(self):
        return pow(self.a, 2)


def get_total_area(figs):
    return sum([fig.calculate_area() for fig in figs])


if __name__ == '__main__':
    print(get_total_area([Rectangle(5, 6), Square(3)]))
