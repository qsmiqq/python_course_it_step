"""
Написать класс автомобиля с атрибутами марки, цвета и объема двигателя и
методами: ехать вперед и ехать назад.

Все методы - это просто команда печати, например print(“Drive forward”)
"""


class Car:
    def __init__(self, brand, colour, vol):
        self.brand = brand
        self.colour = colour
        self.vol = vol

    def ride_forward(self):
        return f'{self.brand} rides forward'

    def ride_backward(self):
        return f'{self.brand} rides backward'

