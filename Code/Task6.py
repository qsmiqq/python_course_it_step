"""Напишите функцию file_n_lines, которая печатает первые n-строка файла.
Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
Не забывайте избавляться от символа переноса строки
К примеру, если бы имелся файл hello.txt со следующим содержимым:

h
he
hel
hell
hello
"""


def file_n_lines(file_name: str, n: int) -> None:
    with open(file_name, 'r') as file:
        for _ in range(n):
            print(file.readline().strip())


# file_n_lines('files/hello.txt', 3)

def file_n_lines_(file_name: str, n: int):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines[:n+1]
