def adding(a: int, b: int):
    return a + b


def mult(a: int, b: int):
    return a * b


def div(a: int, b: int):
    if b == 0:
        raise ZeroDivisionError
    return a / b


def sub(a: int, b: int):
    return a - b
