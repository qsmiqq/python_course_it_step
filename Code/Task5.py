"""
На вход подаются имена людей. Задача считывать имена в список до тех пор пока не будет введена "." (точка).
Вывести список имен, отсортированный по их длине.
"""
names = []

while True:
    name = input()
    if name == ".":
        break
    names.append(name)
names.sort(key=len)
print(names)
