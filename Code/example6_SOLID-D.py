"""D - DIP инверсия зависимостей"""
from abc import ABC, abstractmethod


class Front:
    def __init__(self, data_source):
        self.data_source = data_source

    def show_data(self):
        data = self.data_source.get_data()
        print(data)


class DataSource(ABC):

    @abstractmethod
    def get_data(self):
        pass


class SourceDB(DataSource):

    def get_data(self):
        return "Taking data from db"


class SourceAPI(DataSource):

    def get_data(self):
        return "Taking data from API"


fe = Front(SourceDB())
fe.show_data()
fe1 = Front(SourceAPI())
fe1.show_data()
