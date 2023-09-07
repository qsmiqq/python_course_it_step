"""
У компании имеется поезд, который перевозит грузы.
Поля для класса Train: load_capacity и общий массив для грузов - cargo.
Виды транспортировки грузов:
– стандартные прямоугольные контейнеры для однородного твердого материала (масса на основе плотности материала,
 параметров контейнера и массы самого вагона-контейнера);
– платформы для любого груза (масса на основе массы груза; платформа является частью поезда, т.е. ее масса принимается равной 0);
– стандартные цилиндрические цистерны для жидкости (масса на основе плотности жидкости, параметров цистерны и массы самой цистерны).

Спроектировать объектную модель.
1) В раннере создать необходимые объекты (ничего не вводить).
2) Вывести содержимое общего массива.
3) Отсортировать содержимое массива по видам транспортировки грузов (сначала тяжелые).
4) Вывести содержимое общего массива.
5) Определить, может ли перевезти поезд заданные грузы c учетом, что все вагоны запонены полностью.
"""

