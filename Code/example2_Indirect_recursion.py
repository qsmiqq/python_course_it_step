"""
Indirect recursion starts when one function call another function in certain condition
"""


def fun1(n: int):
    if n > 0:
        print(n, end=" ")
        func2(n + 1)


def func2(n: int):
    if n > 1:
        print(n, end=" ")
        fun1(n - 5)


fun1(20)
# func2(20)