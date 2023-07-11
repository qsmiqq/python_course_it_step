"""
Реализовать функцию calc_factorial(n: int) -> int вычисления факториала числа, используя рекурсию
"""


def calc_factorial(n: int) -> int:
    if n == 1:
        return n
    return n * calc_factorial(n - 1)


print(calc_factorial(3))