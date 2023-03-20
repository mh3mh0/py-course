# variables

my_string_variable = 'My String variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_string_variable = str(my_int_variable)
print(my_int_to_string_variable)
print(type(my_int_to_string_variable))

my_bool_variable = False
print(my_bool_variable)

# concat variables in a print
print(my_string_variable, my_int_to_string_variable, my_bool_variable)
print('this is the value of:', my_bool_variable)

# some functions of the sys
print(len(my_string_variable))

# variables in just one line
name, surname, nickname, age = 'John', 'Carrillo', 'mh3mh0', 41
print('my name is:', name, surname + '.','My age is:', age, 'and my nickname is:', nickname + '!')

# inputs
# comments
'''
name = input('what is your name: ')
age = input('how old are you? ')

print(name)
print(age)
'''

# changing the type
name = 35
age = "mh3mh0"
print(name)
print(age)

# forcing the type¿?
address: str = 'my address'
address = True
address = 5
address = 1.2
print(type(address))

