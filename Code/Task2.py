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
        unique_id = random.choices(string.digits) + random.choices(string.ascii_lowercase)
        return "".join(unique_id)


class Soldier(BaseUnit):
    def __init__(self):
        super().__init__()

    @property
    def team(self):
        return self.__team

    @staticmethod
    def follow_the_hero(hero):
        return f"Following my hero - {hero.name}"

    def set_team(self, team):
        self.__team = team


class Hero(BaseUnit):
    def __init__(self, name, team):
        super().__init__()
        self.__name = name
        self.__team = team
        self.__level = 0

    @property
    def team(self):
        return self.__team

    @property
    def name(self):
        return self.__name

    def level_up(self):
        self.__level += 1


def main():
    teams = ["red", "blue"]
    hero1 = Hero("Iron Man", "red")
    print(f"I'm {hero1.name}", hero1.id)
    hero2 = Hero("Cap", "blue")
    print(f"I'm {hero2.name}", hero2.id)
    reds = []
    blues = []

    for i in range(10):
        soldier = Soldier()
        team = random.choice(teams)
        soldier.set_team(team)
        if soldier.team == "red":
            reds.append(soldier)
        else:
            blues.append(soldier)

    if len(reds) > len(blues):
        hero1.level_up()
        print(f"NEW LEVEL! for {hero1.name}")
    else:
        hero2.level_up()
        print(f"NEW LEVEL! for {hero2.name}")

    print("On your feet soldier!")
    sol1 = random.choice(reds)
    print(sol1.follow_the_hero(hero1))
    print(sol1.id)
    print(hero1.id)
    # print(reds)
    # print(blues)


if __name__ == '__main__':
    main()
