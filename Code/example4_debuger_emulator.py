# debug emulator function
from decorators import debug


@debug
def get_GCD(a, b):
    if b == 0:
        return a
    return get_GCD(b, a % b)


# get_GCD(55, 30)

@debug
def some_function(*args, **kwargs):
    """
    This is simple function
    :param args:
    :param kwargs:
    :return:
    """
    return sum(args)


some_function(5, 8, 12, 6, a=2)
print(some_function.__name__)
print(some_function.__doc__)