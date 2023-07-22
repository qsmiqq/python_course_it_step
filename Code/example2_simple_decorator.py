def my_decorator(func):
    def wrapper():
        print('---Begin---')
        func()
        print('---End---')

    return wrapper




@my_decorator
def say_hello():
    print(f'Hello world')


# func_decorated = my_decorator(say_hello) # вызов декоратора как функции
# func_decorated()
