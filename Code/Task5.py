"""
Дано натуральное число N, вывести все натуральные числа от 1 до N.
"""


def get_numbers(n: int, current=1):
    if n == 1:
        return n
    return get_numbers(n=n, current=current-1)


print(get_numbers(5))
