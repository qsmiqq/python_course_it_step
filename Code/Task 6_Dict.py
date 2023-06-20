"""
Task6*
Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент.
Добавьте в конец ключ new_key со значением new_value.
Выведите на печать итоговый словарь.
Важно, чтобы словарь остался тем же (имел тот же адрес в памяти)
"""
from collections import OrderedDict


dct = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
id_1 = id(dct)
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)

second = list(dct.items())[1]
del dct[second[0]]

id_2 = id(dct)
print(id_1 == id_2)
