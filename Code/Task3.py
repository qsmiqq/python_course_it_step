"""
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
"""


def reverse_seq(l: list) -> None:
    if len(l) >= 1:
        print(l.pop(), end=' ')
        reverse_seq(l)


i = int(input())
lst = list(map(int, input().split()))[:i]
reverse_seq(lst)
