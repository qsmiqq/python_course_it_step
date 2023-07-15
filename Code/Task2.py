"""
В переменную starts_with присвойте lambda функцию, которая принимает строку и возвращает True,
когда переданная строка начинается с буквы W. Во всех остальных случаях нужно возвращать False
"""

starts_with = lambda x: True if x.startswith('W') else False
starts_with_ = lambda x: True if x[0] == 'W' else False
print(starts_with('Windows'))
