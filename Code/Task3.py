"""
Сделайте строку, которая состоит из 25 случайных букв английского алфавита. Запишите ее
в файл random_string.

"""
import string
import random


letters = list(string.ascii_lowercase)
random.shuffle(letters)
random_string = ''.join(letters[:26])

with open('files/random_string.txt', 'a') as file:
    file.write(random_string + '\n')


