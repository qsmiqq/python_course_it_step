"""
Define class Person - the parent class. Define class Student to be inherited from Person.
Use super() method or Person.__init__(), default values in terms of inheritance
"""


class Person:
    def __init__(self, fname="Joe", lname="Doe", date=2003):
        self.fname = fname
        self.lname = lname
        self.date = date

    def say_name(self):
        return f"My name is {self.fname} {self.lname}"


class Student(Person):
    def __init__(self, spec, fname="Joe", lname="Doe", date=2003):
        super().__init__(fname, lname, date)
        self.spec = spec

    def say_name(self):
        return f"My name is {self.fname} {self.lname}. My specialization is {self.spec}"


person = Person("Joe", "Doe", 1987)
print(person.say_name())
student = Student("Python")
print(student.say_name())
