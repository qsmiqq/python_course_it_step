# two simple functions

def outer():
    n = 5

    def inner():
        nonlocal n
        n = 6
        print(n)

    inner()
    print(n)


outer()


def say_hello(name):
    print(f"Hello {name}")


def say_bye(name):
    print(f"Goodbye {name}")


def greeter(func):
    return func(name="Mike")


greeter(say_bye)