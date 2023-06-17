"""
Переменные countries соединяют ряд стран с тремя крупнейшими городами каждой страны.
Программе на вход будет поступать название города в переменную city.
И ваша задача найти какой стране принадлежит введенный город.
Если страна успешно найдена, необходимо вывести сообщение:

INFO: {City} is a city in {Country}
в противном случае

ERROR: Country for {City} not found
Учитывайте, что регистр букв имеет значение
"""
countries = {
    "Belarus": ["Minsk", "Gomel", "Vitebsk"],
    "Sweden": ["Stockholm", "Malmo", "Goteborg"],
    "UK": ["London", "Manchester", "Liverpool"],
    "USA": ["Washington", "New York", "Chicago"]
}

city = input()

for key, val in countries.items():
    if city in val:
        print(f'INFO: {city} is a city in {key}')
        break
else:
    print(f'ERROR: Country for {city} not found')
