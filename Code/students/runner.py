import performance as p


students = {
    "Mike": [10, 8, 9, 10, 9],
    "Bob": [9, 7, 9, 8, 9],
    "Jane": [9, 8, 8, 9, 7],
    "Lisa": [7, 7, 6, 8, 9],
    "Alex": [6, 5, 7, 5, 6]
}


def main():
    grades = list(students.values())
    return p.get_params(*grades)


min_, max_, avg_ = main()
print(f'Минимальная оценка: {min_}' + '\n' + f'Максимальная оценка: {max_}' + '\n' + f'Средняя оценка: {avg_}')
