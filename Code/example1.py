"""
Define class User with protected (private) attribute name.
Change different access properties to see what's happen.
"""


class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    def set_name(self, name_):
        self.__name = name_

    def __return_age(self):
        return self.__age

    def get_info(self):
        return "Current user: {}, {} years".format(self.get_name(), self.__return_age())

    def get_name(self):
        return self.__name


user1 = User("User1", 25)
print(user1.name)
# print(user1.__name)
# print(User.__ind)
# print(User._User__ind)
user1.set_name("User2")
print(user1.get_name())
print(user1.get_info())

