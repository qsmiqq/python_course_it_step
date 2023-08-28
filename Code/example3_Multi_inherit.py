"""
Define two classes A and B with parameters a and b respectively.
Define class C inherited from both classes. Try to call parent attributes from child classes
"""

class A:
    pass

class B:
    pass


class C(B, A):
    pass


c = C()
a = A()
# print(a.a)
# print(c.a)
# print(c.a)
