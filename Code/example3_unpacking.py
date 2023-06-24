def add_mean(x, *data):
    return x + sum(data)/float(len(data))



def handle_info(*person_info, **person_additional_info):
    print(person_info[0], person_info[1],  person_additional_info["sex"], person_additional_info["friends"])

person_info = ('Mike', 35)
person_additional_info = {
    'sex': 'male',
    'friends': ('Kate',)
}

handle_info(*person_info, **person_additional_info)