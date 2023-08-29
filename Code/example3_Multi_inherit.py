"""
Define two classes A and B with parameters a and b respectively.
Define class C inherited from both classes. Try to call parent attributes from child classes
"""


class A:
    def __init__(self):
        self.a = 10


class B:
    def __init__(self):
        self.a = 15


class C(B, A):
    def __init__(self):
        B.__init__(self)
        A.__init__(self)


c = C()
a = A()
print(a.a)
print(c.a)
print(c.a)
