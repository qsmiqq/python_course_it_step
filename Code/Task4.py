"""
Напишите функцию create_actor, которая принимает произвольное количество именованных аргументов
и возвращает словарь с характеристиками актера. Если функции create_actor не передавать никаких аргументов,
то она должна возвращать базовый словарь с ключами name, surname, age. Вот так он выглядит:

create_actor() -> {
        'name': 'string',
        'surname': 'string',
        'age': 0,
    }
Если передавать именованные параметры, которые отсутствуют в базовом словаре, они дополняются к этому словарю

create_actor(height=190, movies=['Дедпул', 'Главный герой']) => {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']
}
Если передавать именованные параметры, которые совпадают с ключами базового словаря,
то значения в словаре должны заменяться переданными значениями:

create_actor(name='Jack', age=20) -> {
        'name': 'Jack',
        'surname': 'Рейнольдс',
        'age': 20,
    }
"""


def create_actor(**kwargs):
    base_actor = {
        'name': 'string',
        'surname': 'string',
        'age': 0
    }
    for key, value in kwargs.items():
        if key in base_actor:
            base_actor[key] = value
        else:
            base_actor.setdefault(key, value)

    return base_actor


print(create_actor(name='Rayan', surname='Nicolson', age=75, height=190, movies=['Дедпул', 'Главный герой']))