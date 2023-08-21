"""
Create class Worker with 3 fields: name, job, salary.
Make salary private. Provide getters and setters for salary attr.

"""

class Worker:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary
