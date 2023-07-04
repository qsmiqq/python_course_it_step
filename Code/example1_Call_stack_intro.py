# def h():
#     print(12)
#
#
# def f():
#     g(h)
#
#
# def g(a):
#     a()
#
#
# g(f)

x = 1


GLOBAL = 99


def func(i):
    global GLOBAL
    GLOBAL = GLOBAL + i
    return GLOBAL

print(func(100))





