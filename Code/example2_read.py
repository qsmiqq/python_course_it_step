### READ FILE

# with open('files/text.txt', 'r') as file:
#     res = file.read()
#     print(res)


### READ LINE

# with open('files/text.txt', 'rb') as file:
#     print(type(file.readline()))
#     print(file.readline().strip())
#     print(file.readline())


# with open('files/text.txt', 'rb') as file:
#     for i in range(30):
#         print(file.readline())

### READ LINES
# with open('files/text.txt', 'r') as file:
#     data = file.readlines()
#     print(data[1])
#     for line in data:
#         if '?' in line:
#             print('Ok')
#         else:
#             print('Failed')


### SEEK/ TEll

# with open('files/text.txt', 'r') as file:
#     file.seek(4)
#     print(file.seek(4))
#     print(file.readline())
#     print(file.tell())



# file = open('data/hello.txt')
# print(file.tell(), '- Start postion')
# file.readline()
# print(file.tell(), '- New position')
# # file.close()
#
#
# file.seek(0)  # Return to start
# print(file.tell())


# file = open('data/hello.txt', 'rb')
# file.seek(6)
# print(file.readline())


### READ PICTURES
#
with open('files/dogy.avif', 'rb') as pic:
    print(pic.readline(1))