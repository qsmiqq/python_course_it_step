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
    reader = csv.DictReader(file)
    people = []
    for line in reader:
        people.append(line)

# with open('files/data.dat', 'wb') as pickle_file:
#     pickle.dump(people, pickle_file)
#
# with open('files/data.dat', 'rb') as pickle_file:
#     data = pickle.load(pickle_file)


with open('files/data.json', 'w') as json_file:
    json.dump(people, json_file)
# print(data)
