"""
Напишите программу, которая будет превращать натуральное число, вводимое из консоли, в строку,
заменяя все цифры в числе на слова: zero, one, two, three, four, five, six, seven, eight, nine.
numbers = {0: "Zero",
           1: "One",
           2: "Two",
           3: "Three",
           4: "Four",
           5: "Five",
           6: "Six",
           7: "Seven",
           8: "Eight",
           9: "Nine"}
"""
numbers = {0: "Zero",
           1: "One",
           2: "Two",
           3: "Three",
           4: "Four",
           5: "Five",
           6: "Six",
           7: "Seven",
           8: "Eight",
           9: "Nine"}

num = input()
text_num = ''

for n in num:
    text_num += numbers.get(int(n)) + ' '
print(text_num)
