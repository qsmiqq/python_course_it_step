"""
Напишите программу, которая печатает словарь alphabet,
где ключи  - строчные английские символы, а значения - порядковые номера букв в алфавите начиная с 1.
Начало вашего словаря должны быть таким {"a": 1, "b": 2 ... }
В качестве ответа распечатайте полученный словарь alphabet
"""
import string


alphabet = {key: value for value, key in enumerate(string.ascii_lowercase, start=1)}
print(alphabet)
