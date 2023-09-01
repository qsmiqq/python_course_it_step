"""
Реализовать класс Animal, экземпляр которого принимает один аргумент name. Создать метод класса voice, который будет
иметь разное поведение в зависимости от названия животного (выводить на печать например, "Гав!" или "мяу!")

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        if self.name == "Dog":
            return "Bark!"
        elif self.name == "Cat":
            return "Meow"


cat = Animal("Cat")
dog = Animal("Dog")

print(cat.voice())
print(dog.voice())
