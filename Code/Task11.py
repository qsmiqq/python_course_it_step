"""
Прочитайте строку.
Если это положительное целое число, то умножьте его на два.
Если это любая другая строка, то повторите её два раза.
"""

s = input()
# print(int(s) * 2) if s.isdigit() else print(s * 2)

if s.isdigit() and int(s) > 0:
    print(int(s) * 2)
else:
    print(s * 2)