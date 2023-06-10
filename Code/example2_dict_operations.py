d = {
    "one": 1,
    "two": 2,
    "three": 3
}
d1 = {
    "four": 4
}

print(len(d))

# UNION
d2 = d1 | d
print(d2)

# ITERATING

students = {"name": "Nick", "age": 19, "course": "Python"}

for i in students:
    print(i)

for i in students.values():
    print(i)

for key, value in students.items():
    print(f"{key} -> {value}")

