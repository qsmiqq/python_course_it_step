"""
Сделайте строку, которая состоит из 25 случайных букв английского алфавита. Запишите ее
в файл random_string.

"""
import string
import random


letters = string.ascii_lowercase
lst_letters = list(letters)
random.shuffle(lst_letters)
print((''.join(lst_letters[:26])))

