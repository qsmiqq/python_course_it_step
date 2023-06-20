"""
Напишите программу, которая принимает последовательность слов, разделенных запятой. Выведите на консоль
все уникальные слова в отсортированном виде

Вход:  red, white, black, red, green, black
Выход: black green red white
"""

words = input().split(', ')
for word in sorted(list(set(words))):
    print(word, end=' ')
