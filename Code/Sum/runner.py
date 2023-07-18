import sys
import mod as m


def main(nums):
    sum_ = m.get_sum(*nums)
    return sum_


if __name__ == '__main__':
    list_nums = tuple(map(int, sys.argv[1:]))
    print(list_nums)
    print(main(list_nums))
