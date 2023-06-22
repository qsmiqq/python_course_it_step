"""
Имеется список words
Задача создать список кортежей words_with_position, где каждый элемент-кортеж должен содержать два значения:
само слово и его порядковый номер в списке words
Порядковый номер слов необходимо считать с единицы.


words = ['variation', 'random', 'electronics', 'competence', 'collapse']

words_with_position = [('variation', 1),
                       ('random', 2),
                       ('electronics', 3),
                       ('competence', 4),
                       ('collapse', 5)]
"""

words = ['variation', 'random', 'electronics', 'competence', 'collapse']

words_with_position = [(word, num) for num, word in enumerate(words, start=1)]
print(words_with_position)