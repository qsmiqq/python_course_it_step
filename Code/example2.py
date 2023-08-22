# Метод __setattr__ и __dict__


class A:
    def __init__(self, num):
        self.num = num

    def __setattr__(self, key, value):
        if key == 'num':
            self.__dict__['num'] = value
        else:
            raise AttributeError


first = A(5)
second = A(10)

first.num = 20
first.num = "15"

print(first.num)
# print(first.num1)
print(first.__dict__)
print(second.__dict__)

