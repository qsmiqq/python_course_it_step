"""
Create Counter Class with two methods - inc, reset
"""


class Counter:
    def __init__(self, x):
        self.x = x

    def inc(self):
        self.x += 1
        return self.x

    def reset(self):
        self.x = 0
        return self.x


counter = Counter(5)
print(counter.inc())
print(counter.inc())
print(counter.inc())
print(counter.inc())
print(counter.reset())
print(counter.x)
