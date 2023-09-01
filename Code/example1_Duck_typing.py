class Bird:
    def fly(self):
        print("I'm bird and I can fly")


class Airplane:
    def fly(self):
        print("I'm airplane and I can fly")


class Dog:
    def bark(self):
        print("I'm airplane and I can fly")


def call_fly_method(instance):
    instance.fly()


bird = Bird()
plane = Airplane()
dog = Dog()

l = [bird, plane, dog]

for elem in l:
    call_fly_method(elem)
