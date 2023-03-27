'''
loops ------------------->
'''
#while ------------------->

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # it is optional
    print('my condition is greater or equal of 10')

print('the execution continues')

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print('my condition stopped')
        break
    print(my_condition)

print('the execution continues')



#for ------------------->

my_list = [34, 24, 62, 52, 30, 30, 17] # lists save elements one by one in order

for element in my_list:
    print(element)

my_tuple = (35, 1.77, 'john', 'ruiz', 'mh3mh0') # tuples save elements, but cannot be overwrite
for element in my_tuple:
    print(element)

my_set = {'john', 'ruiz', 35} # sets save elements that are not repeated
for element in my_set:
    print(element)

my_dict = {'name':'john', 'surname':'ruiz', 'age':41, 1:'python'} # dictionaries save elements in a way key:value
for element in my_dict:
    print(element)
    if element == 'age':
        break
    print('it executes')
else:
    print('my loop *for* of my dictionary has finished')

print('the execution continues')



for element in my_dict:
    print(element)
    if element == 'age':
      continue
    print('it goes on')
else:
    print('my loop *for* of my dictionary has finished')



