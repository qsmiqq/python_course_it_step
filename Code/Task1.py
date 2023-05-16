"""
Программа принимает на вход три символа через пробел в одну строку.
Необходимо вывести код каждого символа при помощи функции ord в определенном формате.
Значение Х равно Y

> F 6 j
> Значение F равно 70
> Значение 6 равно 54
> Значение j равно 106
"""

symbols = input().split()
output = "Значение {} равно {}"

print(f"Значение {symbols[0]} равно {ord(symbols[0])}")
print(output.format(symbols[0], ord(symbols[0])))
print(output.format(symbols[1], ord(symbols[1])))
print(output.format(symbols[2], ord(symbols[2])))
