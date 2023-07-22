# from decorators import debuger
import functools


def my_decorator(func):
    pass



# @debuger
@my_decorator
def return_name(first_name, last_name):
    pass


# f = my_decorator(return_name)
# fname = input("Enter your name: ")
return_name("John", "Connor")