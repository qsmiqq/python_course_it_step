### Topic 20 Files

#### Task 1
Откройте файл `files_HW/unsorted_names.txt` в папке данных. Сортируйте имена и 
записывайте их в новый файл `sorted_names.txt` Каждое имя должно начинаться с новой строки, 
как в следующем примере:
```python
Adele
Adrienne
...
Willodean
Xavier
```

#### Task2
Реализовать функцию поиска наиболее распространенных слов в файле. 
Используйте файл `files_HW/lorem_ipsum.txt`. ПРИМЕЧАНИЕ: Помните о точках, запятых, заглавных 
буквах и т.д.

```python
def most_common_words(filepath, number_of_words=3):
    pass

print(most_common_words('lorem_ipsum.txt'))
>>> ['donec', 'etiam', 'aliquam']
```

#### Task 3*
Файл `files_HW/students.csv` хранит информацию о студентах в формате CSV: имена 
студентов, возраст и среднюю отметку.
1. Реализуйте функцию, которая получает путь к файлу и возвращает имена лучших 
учеников

```python
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))
>>> ['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia', 'Joseph Head']
```   

2. Реализуйте функцию, которая получает путь к файлу с информацией srudents и записывает 
информацию о студенте в новый файл csv в порядке убывания возраста. Результат:
```python
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27

```
#### Task 4*

Текстовый файл `in.csv` (текстовые данные, разделенные запятой) содержит 
некоторую последовательность строк с любым числом элементов в каждой строке. Пусть 
начальный элемент любой строки имеет индекс 0. Его значение определяет индекс элемента в 
строке, с которым вы должны работать. 
1. Рассчитайте сумму элементов, определяемых нулевыми элементами. Выведите этот результат 
в консоли. Формат вывода приведен в примерах ниже. 
2. Вывести количество строк с "ошибками"
```python
Input:                              Input:
3,qw,4,5.2,2.7                      3,qw,4,-3.1,2.7
15,,,k,5                            1,-1,fgh,5
1,-3.14,fgh,5
0,,e1,2,3
2.3,a,b,c
b,b,e

Output:                             Output:
Result (5.2 - 3.14 + 0.0) = 2.06    Result (-3.1 - 1) = -4.1
error-lines = 3 error-lines = 0

```
