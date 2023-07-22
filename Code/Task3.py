"""
Создайте эмулятор предоставления доступа для пользователя.
Используйте декоратор @check_admin для проверки уровня доступа

Если пользователь существует, то программа вернет
`>>> User with name {name} exist`
`>>> Access granted`
"""

ACCOUNTS = {
    "user123": "user",
    "luke23": "user",
    "alex1606": "user",
    "vaider_dart": "admin"
}

