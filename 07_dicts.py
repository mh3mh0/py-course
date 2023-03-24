'''
dictionaries ------------------->
'''
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'name':'john', 'surname':'ruiz', 'age':41, 1:'python'}

my_dict = {
    'name':'john',
    'surname':'ruiz',
    'age':41,
    'languages': {'python', 'swift', 'kotlin'},
    1:1.67
    }

print(my_other_dict)
print(my_dict)

print(my_dict['name'])

my_dict['name'] = 'marlon'
print(my_dict['name'])

print(my_dict['name'])

print(my_dict[1])

my_dict['street'] = 'ruiz street'
print(my_dict)

del my_dict['street']
print(my_dict)

print('ruiz' in my_dict)
print('surname' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ['name', 1, 'floor']

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(('name', 1, 'floor'))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict, 'mh3mh0')
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(my_new_dict.values()))
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))