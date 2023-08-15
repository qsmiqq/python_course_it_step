"""
Напишите функцию create_file_with_numbers, которая принимает на вход одно целое положительное число - n.
Функция должна создать файл с название "range_<number>.txt" и наполнить его целыми числами от 1 до n включительно,
причем каждое число записывается  в отдельной строке
Пример: функция create_file_with_numbers(5) должна создать файл range_5.txt с содержимым

1
2
3
4
5
"""


def create_file_with_numbers(n):
    file = 'range_{}.txt'
    with open(file.format(n), 'w') as f:
        for i in range(1, n + 1):
            f.write(str(i) + '\n')


# create_file_with_numbers(5)

with open('range_6.txt', 'w') as f_:
    f_.writelines([str(i) + '\n' for i in range(1, 6)])
