# Initialization through dict(), dict.fromkeys(), dict comprehension

d = {
    "one": 1,
    "two": 2,
    "three": 3
}

d1 = dict(a=10, b=20)
d2 = dict([("a", 1), ("b", 4)])
d3 = dict.fromkeys(("a", "b", "c"), 100)
d4 = {a: b ** 2 for a, b in enumerate(range(10))}

print(d)
print(d1)
print(d2)
print(d3)
print(d4)

# Keys must be unique
names = {"Name": "Luke", "Name": "Obi-Van"}
print(names)

# >>>> ?
d5 = {
    1: "int",
    1.0: "float",
    True: "bool"
}
# print(d5)
