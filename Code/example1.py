a = {}
print(type(a))
s = set()
print(type(s))
print(s)


s1 = {1, 2, 3, 4, 5}

print(s1)
t = "Hello world"
print(set(t))
l = [1, 2, 3]
# print(hash(t))
# print(hash(l))

s1.add(6)
print(s1)

s1.discard(3)
print(s1)
s1.discard(3)
print(s1)
s1.remove(4)
print(s1)
# s1.remove(4) # Второй вызов метода дает ошибку ключа
s1.pop()
print(s1)
# s1.clear()
s1 = set()
print(s1)
