"""
1. Написать класс автомобиля с атрибутами марки, цвета и объема двигателя и
методами: ехать вперед и ехать назад.
2. Написать класс автомобиля, унаследованного от первого класса в пункте 1.
Добавить методы поворота налево и направо.
3. Написать класс самолета, имеющего метод взлетать и атрибут модель самолета.
4. Написать класс, унаследованный  от машины (2 пункт) и от самолета (3 пункт).
Посмотреть что будет.
"""


class BaseCar:
    def __init__(self, brand, color, vol):
        self.brand = brand
        self.color = color
        self.vol = vol

    def move_forward(self):
        return f"The car {self.brand} is moving forward"

    def move_backward(self):
        return f"The car {self.brand} is moving backward"


class Car(BaseCar):
    def __init__(self, brand, color, vol):
        super().__init__(brand, color, vol)

    def turn_right(self):
        return f"The car {self.brand} is turning right"

    def turn_left(self):
        return f"The car {self.brand} is turning left"


class Plane:
    def __init__(self, brand):
        self.brand = brand

    def take_off(self):
        return f"{self.brand} is taking off"


class PlaneCar(Car, Plane):
    def __init__(self, brand, color, vol):
        Car.__init__(self, brand, color, vol)
        Plane.__init__(self, brand)


car = Car("Ford", "blue", 1.6)
print(car.move_backward())
plane = Plane("Embraer")
print(plane.take_off())

what_are_you = PlaneCar("smth", "red", 3.5)
print(what_are_you.take_off())
