"""
Method Overloading, a way to create multiple methods with the same name but different arguments, is not possible in Python
"""


class MySum:

    def sum(self, a, b):
        return a + b

    def sum(self, a, b, c):
        return a + b + c


# s = MySum()
# print(s.sum(5, 6))


class Base:
    pass