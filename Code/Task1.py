"""
Дано натуральное число N. Вывести все степени числа 2, не превосходящие N.
Использовать цикл while
"""

n = int(input())
i = 1

while i < n:
    i += 1
    print(2**i)
