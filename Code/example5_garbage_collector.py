# Example 1
# x = 1  # one obj reference count equal to 1
# y = x  # one obj reference count equal to 2
#
# y += 1  # two objs reference count equal to 1
# print(x)
# print(y)
#
# x = 2  # Reference count of object 9 becomes 0


# Example 2

# list_ = []
# list_.append(1)
# list_.append(2)
#
# # delete the list from memory or assigning object list_ to None(Null)
# del list_
# # print(list_)
# # list_ = None

# Example 3

# import gc
#
# i = 0
#
#
# # create a cycle and on each iteration x as a dictionary assigned to 1
# def create_cycle():
#     x = {}
#     x[i + 1] = x
#     print(x)
#
#
# # lists are cleared whenever a full collection or collection of the highest generation (2) is run
# collected = gc.collect()  # or gc.collect(2)
# print("Garbage collector: collected %d objects." % (collected))
#
# print("Creating cycles...")
# for i in range(10):
#     create_cycle()
#
# collected = gc.collect()
#
# print("Garbage collector: collected %d objects." % (collected))
