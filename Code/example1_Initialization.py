# Initialization through dict(), dict.fromkeys(), dict comprehension

dct = {
    "a": 1,
    "b": 3,
    "c": 4
}

dct1 = {}
dct2 = dict()

dct1['a'] = 1
print(dct1)
dct1['a'] = 100
print(dct1)

dct3 = dict.fromkeys(("a", "b", "c"), 10)
print(dct3)
dct4 = {a: a*2 for a in range(10)}
dct5 = {a: b ** 2 for a, b in enumerate(range(10))}
print(dct4)

# Ключ должен быть уникальным
name_dict = {"name": "Luke", "name": "Obi-Van"}
print(name_dict)

dct6 = {
    1: "1",
    1.0: "1.0",
    True: "bool"
}
print(dct6)










#
# d = {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }
#
# d1 = dict(a=10, b=20)
# d2 = dict([("a", 1), ("b", 4)])
# d3 = dict.fromkeys(("a", "b", "c"), 100)
# d4 = {a: b ** 2 for a, b in enumerate(range(10))}
#
# print(d)
# print(d1)
# print(d2)
# print(d3)
# print(d4)
#
# # Keys must be unique
# names = {"Name": "Luke", "Name": "Obi-Van"}
# print(names)
#
# # >>>> ?
# d5 = {
#     1: "int",
#     1.0: "float",
#     True: "bool"
# }
# # print(d5)
