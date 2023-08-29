"""
Разработайте программу по следующему описанию.
В некой игре-стратегии есть солдаты и герои.
У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде.
У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой".
У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним.
Выведите на экран идентификационные номера этих двух юнитов.
"""
import random
import string


class BaseUnit:
    def __init__(self):
        self.__id = self.set_id()
        self.__team = ""

    @property
    def team(self):
        return self.__team

    @property
    def id(self):
        return self.__id

    @staticmethod
    def set_id():
        uniqe_id = random.choices(string.digits) + random.choices(string.ascii_lowercase)
        return "".join(uniqe_id)


class Soldier(BaseUnit):
    def __init__(self):
        super().__init__()

    @staticmethod
    def follow_the_hero(hero):
        return f"Following my hero - {hero.name}"


class Hero(BaseUnit):
    def __init__(self, name, team):
        super().__init__()
        self.__name = name
        self.__team = team

    @property
    def team(self):
        return self.__team


sol = Soldier()
hero = Hero('Iron Man', "red")
print(hero.team)
print(sol.id)