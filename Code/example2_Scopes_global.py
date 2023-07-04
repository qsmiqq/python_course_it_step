name = "Iron Man"


def im_the_ironman():
    print(f"I'm the {name}")


def say_hello():
    global name
    name = 'Tony'
    print(f"Hello, {name}")


im_the_ironman()
say_hello()


# ---------LOCAL SCOPE-------------------

# def im_the_ironman():
#     name = "Tony"
#     surname = "Stark"
#     print(f"I'm {name} {surname}")
#

# def say_hello():
#     name = "Thomas"
#     surname = "Anderson"
#     print(f"Hello, {name} {surname}")
#

# im_the_ironman()
# say_hello()


# --------------SHADOW THE OUTER SCOPE-----------------------
# name = "Hulk"
#
#
# def im_the_ironman():
#     global name
#     name = "Tony"
#     print(f"I'm {name}")
#
#
# def say_hello():
#     print(f"Hello, {name}")
#
#
# im_the_ironman()
# say_hello()

# GLOBAL = 99
#
# def func(i):
#     GLOBAL = i
#     return GLOBAL
#
# print(func(100))