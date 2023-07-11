"""
def rec_func_name():
   if(condition)                       # base case
       simple statement without recursion
   else                                # general case
       statement calling rec_func_name()
"""


### Count down
def count_down(n: int):
    if n == 1:
        print(n)
        return n
    print(n)
    return count_down(n - 1)

#count_down(5)

### Sum of natural numbers

def get_sum(n: int):
    if n == 1:
        return n
    return n + (get_sum(n - 1))


print(get_sum(3))


### Tail recursion GCD
# Tail call - recursion is the last operation before return foo(n-1)
# Non tail call contain an expression after recursive function foo(n-1)+1


def get_GCD(a: int, b: int):
    if b == 0:
        return a
    else:
        return get_GCD(b, a % b)


print(get_GCD(48, 30))


### recursion limits
import sys


def func():
    func()


sys.setrecursionlimit(10**4)
func()