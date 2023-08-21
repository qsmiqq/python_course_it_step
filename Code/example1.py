"""
Define class User with protected (private) attribute name.
Change different access properties to see what's happen.
"""


class User:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.getter
    def name(self):
        return self.__name


user = User("John")
# print(user.__name)
# print(user._User__name)
# user.name = "Bob"
print(user.name)



class User2:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    property(get_name, set_name)
