# UPDATE

students = {"name": "Nick", "age": 19, "course": "Python"}
print(students)
students['surname'] = 'Smith'
print(students)
students.update({'school': 'primary'})
# print(students)

# REMOVE

del students["school"]
# print(students)
# students.setdefault("ages", 20)
# print(students)
# students.clear()
# print(students)

# POP
attr = students.popitem()
attr1 = students.pop('age')
# print(attr)
# print(attr1)


# import collections

dict_obj = {}
i = 1

while True:
    obj = input()
    if obj == '.':
        break
    dict_obj[i] = obj
    i += 1
print(dict_obj)