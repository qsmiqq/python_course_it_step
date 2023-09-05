"""
Написать класс DataInterface, у которого будет защищенный атрибут - объект класса
TextLoader и публичный метод process_text. Метод принимает список строк в цикле и обрабатывает
каждый элемент, очищая его от знаков пунктуации.

Определите внутренний класс TextProcessor для обработки текстовых данных. У класса должен
быть публичный метод get_clean_string, который удалит все знаки препинания, метод is_punctuation
- возвращает True/False, проверяя символы на пунктуацию

DataInterface связан с TextProcessor через класс TextLoader

Данные для тестов

["Python, Java!, Gol,ang, C+?", "Pyt@hon, Java!, Gol,ang, C+?"]
"""
import string


class TextProcessor:
    def __init__(self):
        self.__punctuation = string.punctuation

    def __is_punctuation(self, char):
        return char in self.__punctuation

    def get_clean_string(self, txt: str) -> str:
        result = ""
        for i in txt:
            if self.__is_punctuation(i):
                continue
            else:
                result += i
        return result


class TextLoader:
    def __init__(self):
        self.__processor = TextProcessor()
        self.__clean_string = None

    def clear_string(self, string_: str):
        self.__clean_string = self.__processor.get_clean_string(string_)

    @property
    def clean_string(self):
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__loader = TextLoader()

    def process_text(self, list_of_string: list):
        for item in list_of_string:
            self.__loader.clear_string(item)
            print(self.__loader.clean_string)


if __name__ == '__main__':
    lst = ["Python, Java!, Gol,ang, C+?", "Pyt@hon, Java!, Gol,ang, C+?"]
    interface = DataInterface()
    interface.process_text(lst)

