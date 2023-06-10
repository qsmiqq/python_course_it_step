"""
Удалить все записи, ключи которых начинается с буквы а.
names = {
    'arno': 1,
    'john': 2,
    'arni': 3,
    'jane': 4
}
"""
import copy

names = {
    'arno': 1,
    'john': 2,
    'arni': 3,
    'jane': 4
}

# I
# name_keys = list(names.keys())
#
# for name in name_keys:
#     if name.startswith('a'):
#         del names[name]
# print(names)

# II
names_copy = copy.copy(names)

for name in names_copy:
    if name.startswith('a'):
        del names[name]
print(names)
