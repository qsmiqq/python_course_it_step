def get_average(x, y, *data):
    return x + y + sum(data)/ len(data) + 2


print(get_average(2, 3, 5, 6, 7, 8))


def get_personal_info(*args, **kwargs):
    print(args[0], args[1], kwargs.get('name'), kwargs.get('age'))


person = ('Mike', 35)
person_ = {
    'name': 'John',
    'surname': 'Connor',
    'age': 15
}

get_personal_info(*person, **person_)
