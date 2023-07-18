import os

print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(os.path.dirname(__file__))

BASE_DIR = os.path.dirname(__file__)
FILE_NAME = 'mod.py'
NEW_FILE_NAME = 'mod1.py'

PATH = '\\'.join((BASE_DIR, NEW_FILE_NAME))
print(PATH)

# print(help(os))

print(os.mkdir(PATH, mode=0o777))