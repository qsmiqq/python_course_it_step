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
#
#     inner()
#     print(n)
#
#
# outer()


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
