"""
lambda arg1: expression
"""


### Base usage (mult by 2)
def f(n):
    return n * 2

f_ = lambda x: x * 2
# print(f(5))
# print(f_(5))
# print(type(f_))
# print(type(f))


### Compare the ordinary function and lambda


### Error handling
def zero_div(n: int):
    return n / 0


f1 = lambda x: x / 0
# print(zero_div(6))
# print(f1(6))

### Immediately Invoked Function Expression
# print((lambda x, y: x * y)(3, 5))
# print((lambda *x: x * 2)(4, 5, 6))

### arguments

func = lambda x, y=10: x + y
# print(func(1, 12))
# print((lambda *args: sum(args))(1, 2, 3))
func_ = lambda **kwargs: sum(kwargs.values())
# print(func_(one=1, two=2, three=3))

### lambda with map and filter
# map
l = ['3', '45', '87']

# l1 = list(map(int, input().split()))
l2 = list(map(lambda x: int(x)**2, l))
#
# print(l1)
# print(l2)

#filter
l = [1, 2, -5, 10, -50, 3, 5]
l3 = ['abra-cadabra', 'foo', 'bar']
# print(list(filter(lambda x: len(x) > 5, l3)))


### lambda with sort
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
nums = [1, 2, -5, 10, -50, 3, 5]
# print(sorted(ids, key=lambda x: int(x[2:])))
# print(sorted(ids, key=lambda x: len(x), reverse=True))
# print(sorted(nums, key=lambda x: x % 2 == 0))


friends = [
    {"name": "Jane", "age": 25},
    {"name": "Bob", "age": 17},
    {"name": "Alex", "age": 17},
    {"name": "Mike", "age": 30}
]

print(sorted(friends, key=lambda x: (x['age'], x['name'])))




