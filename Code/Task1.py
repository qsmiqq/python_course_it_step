"""
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
Каждая копилка имеет ограниченную вместимость,
которая выражается целым числом – количеством монет,
которые можно положить в копилку.
Класс должен поддерживать информацию о количестве монет в копилке,
предоставлять возможность добавлять монеты в копилку и узнавать,
можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

Класс должен иметь следующий вид

class MoneyBox:
    def __init__(self, capacity):
        # конструктор с аргументом – вместимость копилки

    def can_add(self):
        # True, если можно добавить v монет, False иначе

    def add(self):
        # положить v монет в копилку

При создании копилки, число монет в ней равно 0.
"""

# TODO: Выполнить проверку можно ли добавить больше монет


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.money_count = 0

    def can_add(self):
        if self.capacity == self.money_count:
            return False
        return True

    def add_coin(self):
        if self.can_add():
            self.money_count += 1
            return 'Coin added'
        else:
            return 'No more space in money box'

    def get_coins_amount(self):
        return self.money_count


mb = MoneyBox(5)
print(mb.can_add())
print(mb.add_coin())
print(mb.add_coin())
print(mb.add_coin())
print(mb.add_coin())
print(mb.get_coins_amount())
print(mb.money_count)
print(mb.add_coin())
print(mb.add_coin())


