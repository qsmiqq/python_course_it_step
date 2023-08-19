### Class definition (Class Person, method tell_name)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def tell_name(self):
        return f'My name is {self.first_name} {self.last_name}'


# person = Person(first_name='Will', last_name='Smith')
# print(person.tell_name())
# print(person.first_name)
# print(person.last_name)


class Point:
    def __new__(cls, *args, **kwargs) # new возвращает адрес созданного объекта класса в памяти конструктора
        print("call __new__ method")
        return super().__new__(cls)

    def __init__(self, x=0, y=0): # инициализирует объект с заданными параметрами.
        print("call __init__ method")
        self.x = x
        self.y = y


point = Point(1, 2)
print(point)