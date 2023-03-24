'''
sets ------------------->
'''
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # initially it is a dictionary

my_other_set = {'john', 'ruiz', 41}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('mh3mh0')

print(my_other_set) # a set is not tidy structure

my_other_set.add('mh3mh0') # a set does not admit repeat data

print(my_other_set)

print('ruiz' in my_other_set)
print('ruins' in my_other_set)

my_other_set.remove('ruiz')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {'john', 'ruiz', 41}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'kotlin', 'swift', 'python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({'javascript', 'c#'}))

print(my_new_set.difference(my_set))