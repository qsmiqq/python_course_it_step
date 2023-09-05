"""
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом,
чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение,
состоящее из только что добавленного элемента.

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

"""

import time


class Loggable:

    def log(self, msg):
        """Class for logging"""
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def __init__(self):
        super().__init__()

    def append(self, __object) -> None:
        self.log(f"Append object {__object}")


lst = LoggableList()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append("test")
