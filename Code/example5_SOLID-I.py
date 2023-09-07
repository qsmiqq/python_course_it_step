"""I - Interface separated principle разделение интерфейсов (ISP)"""


from abc import ABC, abstractmethod


# class BasePrinter(ABC):
#     def __init__(self, document):
#         self.document = document
#
#     @abstractmethod
#     def print_(self):
#         return f"Print {self.document}"
#
#     @abstractmethod
#     def fax(self):
#         return f"Send {self.document} by fax"
#
#     @abstractmethod
#     def scan(self):
#         return f"Scan this {self.document}"

class Printer(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def print_(self):
        pass


class Fax(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def fax(self):
        pass


class Scaner(ABC):
    def __init__(self, document):
        self.document = document

    @abstractmethod
    def scan(self):
        pass


class OldPrinter(Printer):
    def __init__(self, document):
        super().__init__(document)

    def print_(self):
        return f"Print {self.document}"


class NewPrinter(Printer, Fax, Scaner):
    def __init__(self, document):
        super().__init__(document)

    def print_(self):
        return f"Print {self.document}"

    def fax(self):
        return f"Send {self.document} by fax"

    def scan(self):
        return f"Scan this {self.document}"

