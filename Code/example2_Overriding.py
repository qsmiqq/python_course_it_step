class Multiplier:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_calc(self):
        return self.a * self.b

    def __str__(self):
        return f"I'm inside class"

    def __add__(self):
        return self.a + self.b


class Exponent(Multiplier):
    def __init__(self, a, b):
        super().__init__(a, b)

    def do_calc(self):
        return self.a ** self.b


m = Multiplier(2, 3)
exp = Exponent(2, 3)
print(m.__add__())
print(m.do_calc())
print(exp.do_calc())
