"""
На вход программе поступает список из целых чисел. Ваша задача найти в данном списке наименьшее положительное значение.
В случае, если положительных значений нет, выведите строку "Empty"
[5, 4, -3, 0, -15]
"""

nums = list(map(int, input().split()))
min = nums[0]

for elem in nums:
    if elem < 0 and elem == 0:
        continue
    if elem > 0:
        if min > elem:
            min = elem

print("Empty" if min < 0 else min)
