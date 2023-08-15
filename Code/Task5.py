"""
У вас есть список users = [‘Arthur’, ‘Kate’, ‘Alice’, ‘Mike’]. Сделайте список
словарей, в каждом из которых будет ключ name, куда вы подставите имя из списка, и id -
случайное число от 1 до 99. Выполните сериализацию при помощи модуля pickle и запишите данные в
файл в формате dat.
"""
import json
import random


users = ['Arthur', 'Kate', 'Alice', 'Mike']
dict_of_users = dict()

for user in users:
    dict_of_users[user] = random.randint(1, 99)

data = json.dumps(dict_of_users)
print(type(dict_of_users))
print(type(data))
print(data)

with open('tmp.txt', 'w') as inf:
    inf.write(data)

with open('tmp.txt', 'r') as file:
    line = file.read().strip()


json_data = json.loads(line)
print(json_data.get('Kate'))