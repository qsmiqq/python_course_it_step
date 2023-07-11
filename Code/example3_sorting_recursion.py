"""
Quick sorting using recursion
"""
import random


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        r = random.choice(nums)
        before = []
        eq = []
        after = []
        for num in nums:
            if num < r:
                before.append(num)
            elif num > r:
                after.append(num)
            else:
                eq.append(num)
        return quick_sort(before) + eq + quick_sort(after)


l = [4, 1, 6, 3, 2, 7, 8]
print(quick_sort(l))



