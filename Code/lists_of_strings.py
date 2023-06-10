"""
Даны 2 списка строк A1 и A2.
Создай список, состоящий из строк списка A1, которые являются подстроками строк из A2.
"""

A1 = ["thon", "cb", "foo"]
A2 = ["Python", "Acb", "bar", "amogus", "BAcb"]

new = []

for a1 in A1:
    for a2 in A2:
        if a1 in a2:
            new.append(a2)
print(new)