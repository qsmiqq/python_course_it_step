"""
Modify previous class with property decorator on salary attr
"""

class Worker:
    SALARY_MAP = {
        "A": 1000,
        "B": 500,
        "C": 300
    }

    def __init__(self, working_class):
        self.__salary = self.__get_salary(working_class)

    @staticmethod
    def __get_salary(working_class):
        return Worker.SALARY_MAP.get(working_class, 0)

    @property
    def salary(self):
        return self.__salary


worker = Worker("D")
print(worker.salary)
