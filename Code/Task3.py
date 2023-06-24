"""
Пусть надо написать программу, вычисляющую площади разных фигур.
Пользователь указывает, площадь какой фигуры он хочет вычислить.
После этого вводит исходные данные.
Например, длину и ширину в случае прямоугольника.
Чтобы разделить поток выполнения на несколько ветвей, следует использовать оператор if-elif-else
Methods: if-else, input, functions
Input: "1-прямоугольник, 2-треугольник, 3-круг:" 1
        "Ширина: " 2
        "Высота: " 6
Output: "Площадь: " 12
"""


def rectangle(a: int, b: int) -> int:
    return a * b


def triangle(a: int, b:int, c: int) -> int:
    return a * b * c


def circle(radius: int, pi=3.14) -> float:
    return pi * radius * radius


def main(option: int):
    if option == 1:
        a, b = int(input('Wight')), int(input('Height'))
        return rectangle(a, b)
    if option == 2:
        a, b, c = int(input('Side 1 ')), int(input('Side 2 ')), int(input('Side 3 '))
        return triangle(a, b, c)
    if option == 3:
        radius = int(input('Radius: '))
        return circle(radius)
    if option not in [1, 2, 3]:
        return 'No such option'


i = int(input("Enter your option: 1-Rectangle, 2-Triangle, 3-Circle: "))
print(main(option=i))
