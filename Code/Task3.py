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


def check_admin(func):
    def wrapper(arg):
        if ACCOUNTS.get(arg) == 'user':
            func(arg)
            print('Access denied')
        elif ACCOUNTS.get(arg) == 'admin':
            func(arg)
            print('Access granted')

    return wrapper

@check_admin
def is_user(name):
    if name in ACCOUNTS:
        print(f'User with name {name} exist')
    else:
        print(f'User with name {name} not registered')


is_user('vaider_dart')