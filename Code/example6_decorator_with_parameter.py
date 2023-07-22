import time
from decorators import get_time, debug


def slow_down(rate=1.0):
    def decor_slow_down(func):
        def wrapper(*args):
            time.sleep(rate)
            return func(*args)

        return wrapper
    return decor_slow_down


@debug
@get_time
@slow_down(rate=5.0)
def get_sum(*args):
    return sum(args)


res = get_sum(5, 8, 25, 105)
print(res)