"""
Напишите программу, которая распечатает все натуральные числа кратные 5 от 195 до 6785 включительно в порядке убывания.
"""

a = 195
b = 6785

while b >= a:
    if b % 5 == 0:
        print(b)
    b -= 1
