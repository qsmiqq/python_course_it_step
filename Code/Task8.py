"""
Из файла numbers.txt, в котором записаны натуральные числа, найти
количество трехзначных чисел;
сумму двухзначных чисел

В качестве ответа укажите найденные два числа через запятую без других знаков и пробелов.
"""


def count_nums(file):
    count = 0
    sum_ = 0
    with open(file, 'r') as file_:
        for n in file_.readlines():
            if len(n.strip()) == 3:
                count += 1
            if len(n.strip()) == 2:
                sum_ += int(n)
    return count, sum_

