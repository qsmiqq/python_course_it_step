"""
Есть словарь: d = {'a':3, 'b':0, 'c':4, 'd':-3}. Найти самое большое число из значений словаря
"""
d = {'a':3, 'b':0, 'c':4, 'd':-3}
# I
# print(max(d.values()))

# II
# lst = []
# for i in d.values():
#     lst.append(i)
# print(max(lst))

# III
print(max([x for x in d.values()]))