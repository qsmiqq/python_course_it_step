# This is a new module

# define some objects here
a = 45
b = 12.5

lst = [1, 2, 3, 4, 5, 25, 68]


def say_hello(name: str):
    return f'Hello {name}'


class MyClass:
    pass


# entrypoint goes here
# if __name__ == "__main__":
#     print(f"File __name__ set to {__name__}")
#     print("This is mod file")
#     print(a, b)


# show the difference between script and import __name__ File __name__ set to {__name__}
print(f"File __name__ set to {__name__}")