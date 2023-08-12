'''
Сериализация - это способ преобразования структуры данных в линейную форму,
которую можно сохранить или передать по сети.
'''

import pickle
import json

data = dict(a="1", b="2", c="3")
print(type(json.dumps(data)))

with open('files/data.json', 'w') as file:
    json.dump(data, file)
#
#     file.write(str(d))


with open('files/data.json', 'rb') as file:
    print(type(json.load(file)))








# import pickle
#
# storage_file = 'storage.data'
# data = ['abc', 123, 456.789]
# with open(storage_file, 'wb') as file_storage:
#     pickle.dump(data, file_storage)
# # del data
# #
# #
# with open(storage_file, 'rb') as file_storage:
#     print(pickle.load(file_storage))