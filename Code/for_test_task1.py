"""
Счастливым билетом называют такой билет с шестизначным номером (иногда и с незначащими нулями),
где сумма первых трех цифр равна сумме последних трех.
Программа получает на вход последовательность чисел и должна вывести «YES»,
если билет с номером N счастливый и «NO» в противном случае.
Вход: 385916
Выход: YES
"""

ticket_num = input()

if len(ticket_num) % 2 != 0:
    print('NO')
else:
    mid = int(len(ticket_num) / 2)
    first = sum(list(map(int, ticket_num[:mid])))
    second = sum(list(map(int, ticket_num[mid:])))
    print('YES') if first == second else print('NO')

