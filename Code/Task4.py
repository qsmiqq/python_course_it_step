"""
Перед вами располагается словарь address
Давайте проверим наличие следующих ключей:
zip_code
id
post_code
street_name
country
Программа должна проверить наличие ключей и вывести True, если ключ имеется, или False, если ключ отсутствует.
address = {
  "id": 7973,
  "uid": "42f2ce1d-90ab-4345-9595-0d9f42e6c085",
  "city": "East Monteland",
  "zip_code": "58611",
  "zip": "01667",
  "postcode": "00563",
  "country": "Mali",
  "country_code": "MH",
  "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715"
}
"""

address = {
  "id": 7973,
  "city": "East Monteland",
  "zip_code": "58611",
  "zip": "01667",
  "postcode": "00563",
  "country": "Mali",
  "country_code": "MH",
  "full_address": "Apt. 982 4820 Leena Rest, Lake Giannaville, MN 09265-3715"
}

lst = [
    'zip_code',
    'id',
    "post_code",
    'street_name',
    'country'
]

for item in lst:
    print(item in address)