"""
Прочтите data.csv файл. Запишите имена колонок в отдельную переменную,
а в другую все остальные строки. Создайте список словарей, где ключами будут имена колонок,
а значениями будут строки. Выполните сериализацию данных в при помощи модуля pickle
Сохраните данные в файл dat.

Для чтения csv используйте метод reader
"""
import csv
import pickle
import json

with open('files/data.csv', 'r') as file:
    reader = csv.reader(file)
    for n, line in enumerate(reader):
        if n == 0:
            continue
        else:
            print(f'{line[0]}: {line[1]} -> {line[2]}')


