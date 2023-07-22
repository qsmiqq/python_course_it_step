"""
Напишите декоратор @timer к функции нахождения факториала числа и выведите время выполнения кода
"""
import time


def timer(func):
    def wrapper(*args):
        start_at = time.perf_counter_ns()
        val = func(*args)
        print(f'Estimated time: {round(time.perf_counter_ns() - start_at, 2)} nsec')
        return val

    return wrapper


@timer
def fact(i):
    if i == 1:
        return i
    return i * fact(i - 1)



res = fact(5)
print(res)