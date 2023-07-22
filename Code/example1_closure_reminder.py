# two simple functions

def say_hello(name):
    print(f"Hello {name}")


def say_bye(name):
    print(f"Goodbye {name}")


def greeter(func):
    return func("Mike")


greeter(say_hello)

