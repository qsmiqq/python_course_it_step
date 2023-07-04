# def outer():
#     n = 5
#
#     def inner():
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()

# -------------------------------

# def outer():
#     n = 5
#
#     def inner():
#         n = 25
#         print(n)
#         print(locals())
#
#     inner()
#     print(n)
#     print(locals())
#
#
# outer()
# print(locals())


# -----------------------------

# def outer():
#     n = 5
#
#     def inner():
#         nonlocal n
#         n = 25
#         print(n)
#
#     inner()
#     print(n)
#
#
# outer()

# x = 'global'
#
#
# def f1():
#     x = 'enclosing'
#
#     def f2():
#         nonlocal x
#         x = 'inner'
#         print(x)
#
#     f2()


# f1()