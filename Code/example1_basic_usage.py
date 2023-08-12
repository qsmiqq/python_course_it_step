import os


# try:
#     file = open('files/text.txt', 'r')
#     print('File has been opened')
#     print(file.read())
# except FileNotFoundError as error:
#     print(error)
# finally:
#     file.close()


### ValueError: I/O operation on closed file.

# with open('files/text.txt', 'r') as file:
#     print(file.read())
#
# file.read()






### os.scandir
#
# print(os.path.dirname(__file__))
#
# with os.scandir(os.path.dirname(__file__)) as path:
#     for item in path:
#         print(item.name, '-> ', item.stat().st_size, 'bytes')



class MyContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
