"""
Дано натуральное число N, вывести все натуральные числа от 1 до N.
"""


def get_numbers(n: int, current=1):
    if current <= n:
        print(current, end=' ')
        get_numbers(n=n, current=current+1)


get_numbers(5)
