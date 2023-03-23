'''
tuples ------------------->
'''

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'john', 'ruiz', 'ruiz', 'ruiz')
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('ruiz'))
print(my_tuple.index('john'))
print(my_tuple.index('ruiz'))

# my_tuple[5] = 1.80 'tuple' object does not support item assignment


my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:7])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'coding and rolling'
my_tuple.insert(1, 'green')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined



