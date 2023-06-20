"""
В множество  my_set = {'government', 'control', 'winter', 'few', 'generation',
          'service', 'national', 'tradition', 'government'}
добавить в него 4 строковых элемента:

concert
brown
jacket
value
"""
my_set = {
    'government',
    'control',
    'winter',
    'few',
    'generation',
    'service',
    'national',
    'tradition',
    'government'
}
words = ['concert', 'brown', 'jacket', 'value']

for word in words:
    my_set.add(word)
print(my_set)