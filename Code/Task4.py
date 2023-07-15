"""
На соревнованиях по стрельбе участники получили следующие результаты

grades = [
    {'name': 'Gideon', 'final': 95},
    {'name': 'Mitchel', 'final': 92},
    {'name': 'Ilona', 'final': 98}
    {'name': 'Price', 'final': 99}
]

Используя анонимную функцию отсортируйте словари в порядке возрастания результатов
"""

grades = [
    {'name': 'Gideon', 'final': 95},
    {'name': 'Mitchel', 'final': 92},
    {'name': 'Ilona', 'final': 98},
    {'name': 'Price', 'final': 99}
]

for score in sorted(grades, key=lambda x: x['final']):
    print(score['final'], end=' ')