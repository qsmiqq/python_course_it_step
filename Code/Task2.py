"""
Modify previous class with property decorator on salary attr
"""


class Worker:
    SALARY_MAP = {
        "A": 1000,
        "B": 500,
        "C": 300
    }

    def __init__(self, worker_class):
        self.__salary = self.__get_salary(worker_class)

    @property
    def salary(self):
        return self.__salary

    def __get_salary(self, class_):
        return self.SALARY_MAP.get(class_, 0)


worker = Worker("A")
print(worker.salary)
