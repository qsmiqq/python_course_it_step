"""
Дано целое положительное число A.
Следует создать и вывести список размера A, содержащий A первых положительных нечётных чисел.
"""

# 1 способ

a = int(input())
l = []
for i in range(a):
  l.append(2*i + 1)
print(l)

# 2 способ

print([2*i + 1 for i in range(int(input()))])

# 3 способ
a = int(input())
lst = []
i = 0

while len(lst) < a:
    if i % 2 != 0:
        lst.append(i)
    i += 1
print(lst)

