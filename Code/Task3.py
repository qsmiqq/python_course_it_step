"""
Напишите функцию check_sum, которая принимает произвольное количество аргументов типа int.
Данная функция должна выводить not enough, если сумма всех элементов меньше 50,
в противном случае выводить verification passed
Input: 8 11
Output: not enough

"""


def check_sum(*args):
    if sum(args) < 50:
        print('not enough')
    else:
        print('verification passed')


nums = list(map(int, input().split()))
check_sum(*nums)

