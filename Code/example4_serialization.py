'''
Сериализация - это способ преобразования структуры данных в линейную форму,
которую можно сохранить или передать по сети.
'''

import pickle

l = ["a", 12, 23.5]

with open('data.dat', 'wb') as file:
    pickle.dump(l, file)

with open('data.dat', 'rb') as file:
    data = pickle.load(file)
    print(data)











# import pickle
#
# storage_file = 'storage.data'
# data = ['abc', 123, 456.789]
# with open(storage_file, 'wb') as file_storage:
#     pickle.dump(data, file_storage)
# del data
#
#
# with open(storage_file, 'rb') as file_storage:
#     print(pickle.load(file_storage))