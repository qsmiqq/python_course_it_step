class Multiplier:
    def __init__(self, a: int):
        self.a = a

    def print_a(self, x):
        print(self.a * x)


class Exponent(Multiplier):
    def print_a(self, x):
        print(self.a ** x)


mul = Multiplier(4)
mul.print_a(2)

exp = Exponent(4)
exp.print_a(2)
