"""
Усовершенствуте предыдущее задание, чтобы функция могла начинать суммировать с определенного значения.
Это значение мы ей будем передавать, но оно является необязательным.

summator_1 = create_accumulator(100)
print(summator_1(1)) # печатает 101
print(summator_1(5)) # печатает 106
print(summator_1(2)) # печатает 108

Во втором примере мы не передали значение и значит сумма по умолчанию должна считаться с нуля.

"""


def create_accumulator(v=0):
    sum_ = v

    def get_sum(num):
        nonlocal sum_
        sum_ += num
        return sum_

    return get_sum


summator_1 = create_accumulator(v=100)
print(summator_1(2))
print(summator_1(4))
