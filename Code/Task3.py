"""
Дано целое положительное число N. Вывести все числа Фибоначчи до числа, большего N.
Вывод чисел запиши через пробел.
a = 2
b = 3

a, b = b, a
print(a, b)
"""

n = int(input())

fib1, fib2 = 1, 1

print(fib1, fib2, end=" ")

for i in range(n - 1):
    fib2, fib1 = fib1 + fib2, fib2
    print(fib2, end=" ")
