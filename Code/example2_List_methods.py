lst = [1, 2, 'a', 'b', True, {'a': 1}, [1, 2, 3]]
lst_ = [5, 6, 7]
# Добавление элементов в список
lst.append(1)
print(lst)
print(lst.count(1))
print(lst.index('a')) # выводит индекс первого вхждения элемента в список

lst.extend(lst_) # расширяет список на указанный элемент
print(lst)

lst.insert(3, 'c') # вставляет элемент по указанному индексу
print(lst)

i = lst.pop() # извлекает последний элемент и возвращает его
print(i)
print(lst)

lst.remove('a') # удаляет первое вхождение элемента в списке
print(lst)

lst.reverse()
print(lst)

names = ['John', 'Michael', 'Sofia']
names.sort(key=len)
print(names)

nums = [1, 5, 3, 4, 2]
nums.sort(reverse=True, key=lambda x: x % 2) # key принимает какую-то функцию
print(nums)

