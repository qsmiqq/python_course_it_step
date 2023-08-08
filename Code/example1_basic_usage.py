file = open('data/hello.txt', 'w')

# try:
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
# import os
#
# with os.scandir(r"C:\Users\Kid\PycharmProjects\pythonProject1\Lesson14") as entries:
#     for entry in entries:
#         print(entry.name, "->", entry.stat().st_size, "bytes")


