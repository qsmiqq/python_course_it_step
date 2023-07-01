# def h():
#     print(12)
#
#
# def f():
#     g(h)
#
#
# def g(a):
#     a()
#
#
# g(f)


stack = []

stack.append('module')
stack.append('func_1')
stack.append('print')

print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
