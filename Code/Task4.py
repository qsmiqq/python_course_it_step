"""
Описать рекурсивную функцию double_fact,
которая принимает на вход целое число и вычисляет значение двойного факториала
"""


def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return n * double_fact(n - 2)


print(double_fact(6))
