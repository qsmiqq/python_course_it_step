"""
Создайте функцию average_numbers, которая будет вносить число в список и подсчитывать среднее арифметическое этого списка.

r1 = average_numbers()
print(r1(1)) # 1.0
print(r1(10)) # 5.5
print(r1(100)) # 37.0
print(r1(1000)) # 277.75
print(r1(10000)) # 2222.2
"""


def average_numbers():
    l = []

    def get_average(num):
        l.append(num)
        return sum(l)/len(l)

    return get_average


r1 = average_numbers()
print(r1(1)) # 1.0
print(r1(10)) # 5.5
print(r1(100)) # 37.0
print(r1(1000)) # 277.75
print(r1(10000)) # 2222.2
