"""
Method Overloading, a way to create multiple methods with the same name but different arguments, is not possible in Python
"""


class MySum:
    def get_sum(self, a, b):
        return a + b

    def get_sum(self, a, b, c):
        return a + b + c


s = MySum()
# print(s.get_sum(5, 6, 5))


class Base:
    def __init__(self, a):
        self.a = a

    def calculate(self, mult=True, square=True):
        if mult and not square:
            return self.a * 2
        elif not mult and square:
            return self.a ** 2
        elif mult and square:
            return (self.a * 2) ** 2
        else:
            return self.a


base = Base(5)
print(base.calculate(mult=True, square=True))
