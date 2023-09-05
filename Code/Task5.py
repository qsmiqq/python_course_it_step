"""
Реализуйте базовый класс Figure c атрибутом shape и методом get_square.
Создайте дочерний класс Rectangle, унаследованный от Figure. Задайте атрибут shape
и задайте 2 доплнительных атрибута: length и height. Задать уровень доступа к атрибутам
как private. Реализовать функцию property и сеттеры для приватных атрибутов.
Реализовать функцию расчета площади.
"""


class Figure:
    def __init__(self, shape):
        self.__shape = shape

    def get_square(self):
        pass


class Rectangle(Figure):
    def __init__(self, shape):
        super().__init__(shape)
        self.__length = 0
        self.__height = 0

    def set_length(self, val):
        self.__length = val

    def set_height(self, val):
        self.__height = val

    @property
    def height(self):
        return self.__height

    @property
    def length(self):
        return self.__length

    def get_square(self):
        return self.__length * self.__height


rect = Rectangle("rectangle")
rect.set_length(5)
rect.set_height(7)

# print(rect.height)
# print(rect.length)

print(rect.get_square())
