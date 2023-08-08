### READ FILE

# file = open('data/sh.txt', 'r', encoding='utf-8')
# data = file.read()
#
# # print(data)
# print(data[:100])


### READ LINE

# file = open('data/sample.txt', 'r')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# for line in range(10000):
#     print(file.readline())
# file.close()


### READ LINES
# with open('data/sample.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         if "?" in line:
#             print(line)  # change char to ?
# # file.close()
# print(lines)

### SEEK/ TEll

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
# with open('data/dog.png', 'rb') as file:
#     print(file.read(1))
#     print(file.read(2))
#     print(file.read(3))
#     print(file.read(4))
#     print(file.read(5))
#     print(file.read(6))
#     print(file.read(7))
#     print(file.read(8))