"""
Define class my_list inherited from List. Add new method is_even_length.
"""


class MyList(list):
    """This is a new class"""
    def is_even_length(self):
        return len(self) % 2 == 0


lst = MyList([1, 2, 3])
print(lst.is_even_length())