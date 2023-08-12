# with open('files/test.txt', "w") as file:
#     file.write("1234")

# lst = ['text', 'text1', 'text2']
# with open('files/test.txt', 'w') as file:
#     for i in lst:
#         file.write(i + "\n")


# lst = ['text', 'text1', 'text2']
# with open('files/text.txt', 'a') as file:
#     for i in lst:
#         file.write(i + "\n")


lst = ['text', 'text1', 'text2']
with open('files/test.txt', 'w') as file:
    file.writelines(lst)