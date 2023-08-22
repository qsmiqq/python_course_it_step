"""
Create class Worker with 3 fields: name, job, salary.
Make salary private. Provide getters and setters for salary attr.

Создать класс Worker с 3 полями: name, job, salary
Сделать salary приватным. Создать геттеры и сеттеры для атрибута salary
"""


class Worker:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    property(get_salary, set_salary)


worker1 = Worker("Misha", "engineer", 1000)
print(worker1.get_salary())
worker1.set_salary(1200)
print(worker1.get_salary())
