"""
Напишите декоратор repeater, который дважды вызывает декорированную функцию

multiply(2, 7) # после этого распечатается две строки со значением 14
"""


def repeater(func):
    def wrapper(*args):
        res = func(*args)
        print(res)
        print(res)

    return wrapper


@repeater
def multiply(num1, num2):
    return num1 * num2


@repeater
def say_hello(name):
    return f'Hello, {name}'


multiply(3, 5)
say_hello('Jack')
