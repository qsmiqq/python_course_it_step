str_1 = "abc"
str_2 = "cdef"
# str_1 = str_1 + str_2
# print(str_1, str_2, sep="-")
# print(str_1, "\t", str_2)




# Unicode
unicode_txt = '\u043f\u0440\u0438\u0432\u0435\u0442'
CHESS_KNIGHT = '\u265E'
roman_nine = '\u2168'
# print(unicode_txt)
# print(CHESS_KNIGHT)
# print(roman_nine)


# docstring in action (__doc__)


# immutability mechanism

# mylist = ["apple", "banana", "cherry"]
#
# b = mylist
#
# b.append(1)
# print(b)
# print(mylist)


# <<<SLICES (Task2)>>>

some_string = "I like Python"

# print(some_string[2:])
# print(some_string[0:6])
# print(some_string[-1])
# print(some_string[-6:])
# print(some_string[:])
# print(some_string[::-1])


# <<<OPERATORS>>>

str_3 = "IT-Step "
str_4 = "Programming"

# print(str_3 * 20)
# print("Hello" * -1)
#
# for i in str_4:
#     print(i, end="")

# print("m" in str_4)
# print(len(str_4))


# <<<FORMATTING>>>

name = "Nikolai"
# print('Hello, %s' % name)

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)

# Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

# print(txt.format(13800000000))

# Use "e" to convert a number into scientific number format (with a lower-case e):

txt4 = "We have {:e} chickens."
# print(txt4.format(5))

# print(txt1)
# print(txt2)
# print(txt3)

# literals

name_ = "John"
surname = "Smith"

# print(f"My name is {name_} {surname}")
# print(r"C:\User\user1\PycharmProj")
# print(b"PycharmProj")
# print(type(b"PycharmProj"))

# <<< METHODS Task3 >>>

txt6 = "I like Python"
mylist = ["apple", "banana", "cherry"]

# print("/".join(mylist))
# print(txt6.replace("Python", "Java").replace("like", "don't like").replace("I", "We"))
# print(txt6.replace("Java", "Python"))
# print(str_4.count("m"))

# print(name.lower())
# print(name.upper())
# print(name.isupper())
# print(name.islower())


# print(txt6.endswith("Python"))
# print(txt6.endswith("python"))
name1 = "mike"
# print(name1.title())



