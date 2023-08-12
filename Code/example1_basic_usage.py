import os

#

# try:
#     file = open('data/hello.txt', 'w')
#     print(file.read())
# except Exception as error:
#     print(error)
# finally:
#     file.close()



# with file:
#     file.write("Hello world")

### ValueError: I/O operation on closed file.
# with file:
#     file.write("Hello world")



### os.scandir
#


with os.scandir(os.path.dirname(__file__)) as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")


