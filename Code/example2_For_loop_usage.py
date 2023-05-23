l = "text_text1_text2"
l_ = [1, 2, 3, "f", True]
# for i in range(len(l)):
#     print(l[i])

# for i in l:
#     print(i)

# for i in l_:
#     print(i)


"""Break-Continue instructions"""
for i in range(10):
    if i == 3:
        print(f"{i} - continue")
        continue
    elif i == 7:
        print(f"{i} - break")
        break
    else:
        print(i)
else:
    print("Fin")
