"""
Напишите функцию exponentiation,
которая принимает на вход целое число и выводит на экран через пробел квадрат и куб этого числа.
"""


def exponentiation(a: int):
    print(pow(a, 2), pow(a, 3))


i = int(input())
exponentiation(i)