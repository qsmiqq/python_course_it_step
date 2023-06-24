"""
Напишите программу которая принимае последовательность слов, разделенных запятой. Выведите на консоль
все уникальные слова в отсортированном виде

Вход:  red, white, black, red, green, black
Выход: black green red white
"""


def sort_words(lst: list) -> list:
    return sorted(set(lst))


l = input().split()
print(sort_words(l))
