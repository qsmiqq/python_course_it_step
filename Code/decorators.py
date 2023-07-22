# add your decorators here
import functools
import time


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        lst_args = [str(arg) for arg in args]
        lst_kwargs = [f'{key}:{value}' for key, value in kwargs.items()]
        params = ', '.join(lst_args + lst_kwargs)
        print(f'Calling function {func.__name__} with parameters {params}')
        result = func(*args, **kwargs)
        print(f'Function {func.__name__} returned {result}')

    return wrapper


def get_time(func):
    def wrapper(*args, **kwargs):
        start_at = time.time()
        val = func(*args, **kwargs)
        print(f'Estimated time: {time.time() - start_at}')
        return val

    return wrapper