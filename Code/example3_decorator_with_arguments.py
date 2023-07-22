def my_decorator(func):
    def wrapper(a, b):
        print('---Begin counting---')
        val = func(a, b)
        print('---Counting complete---')
        return val

    return wrapper


@my_decorator
def get_sum(num1, num2):
    return num1 + num2


print(get_sum(5, 3))