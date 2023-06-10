d = {
    "one": 1,
    "two": 2,
    "three": 3
}
d1 = {
    "four": 4
}

# print(len(d))

# UNION
d2 = d | d1
d.update(d1)
# print(d2)
# print(d)

# ITERATING
# for key, value in d2.items():
#     print(f'{key} -> {value}')
#
# for key in d2:
#     print(key)
#
# for _, value in d2.items():
#     print(value)

# Как достать значение?

print(d2['one'])
print(d2.get('one', {}))


d3 = {}
d3.setdefault('a', 1)
print(d3)