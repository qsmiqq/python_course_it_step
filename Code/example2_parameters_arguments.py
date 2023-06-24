def compute_surface(radius, pi=3.14159):
    return pi * radius * radius

# print(compute_surface(5))
### ARGUMENTS WRONG POSITION
# def compute_surface_(radius=1, pi):
#     return pi * radius * radius


s = compute_surface(10, pi=3.14)
# s_ = compute_surface(pi=3.14, 10)
s1 = compute_surface(10)
# print(s)
# print(s1)


def get_sum(a, b, c, d):
    return sum([a, b, c, d])

sum_ = get_sum(b=1, a=2, c=6, d=4)
# sum_ = get_sum(b=1, a=2, c=6, 1, 3, 5) # SyntaxError
# print(sum_)

### *args
def get_sum_(*args):
    return sum(*args)

nums = (1, 2, 3, 4)
# print(get_sum_(nums))


### kwargs
dict_ = {
    "a": 1,
    "b": 2,
    "c": 3
}

def get_another_sum(f, e, **d):
    sum = 0
    for k, v in d.items():
       sum += v
    return sum + f + e

print(get_another_sum(4, 5, a=1, b=2, c=3))


### PEP 570

def some_function(a, b, c=3, /):
    return a + b + c

#
# print(some_function(1, 2))