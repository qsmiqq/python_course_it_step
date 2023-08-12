"""
Считайте элементы списка names и запишите их в  файл names.txt в формате id) Name

names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']
"""

names = ['Richard', 'Din Esh', 'Erlich', 'Bighead']

with open('files/names.txt', 'w') as file:
    for n, name in enumerate(names, start=1):
        file.write(f'{n}) {name}\n')