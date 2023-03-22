'''
strings ------------------->
'''
my_string = 'my string'
my_other_string = 'my other string'

print(len(my_string))
print(len(my_other_string))
print(my_string + ' SUP? ' + my_other_string)

my_new_line_string = 'this is an string\nwith a line break' # line break
print(my_new_line_string)

my_tab_string = '\tthis is an string with a line tab' # line tab
print(my_tab_string)

my_scape_string = '\tthis is an string with a \n line scape' # line tab
print(my_scape_string)

'''
formatting ------------------->
'''
name, surname, age = 'John', 'Ruiz', 41

print('My name is {} {} and my age is {}'.format(name, surname, age)) # correct
print('My name is %s %s and my age is %d' %(name, surname, age)) # correct
print('My name is ' + name + ' ' + surname + ' and my age is ' + str(age)) # incorrect
print(f'My name is {name} {surname} and my age is {age}') # the best option


'''
un-packing characters ------------------->
'''
language = 'python'
a, b, c, d, e, f = language
print(a)
print(f)


'''
Division ------------------->
'''
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


'''
Reverse ------------------->
'''
reversed_language = language[::-1]
print(reversed_language)


'''
Functions ------------------->
'''

print(language.capitalize())
print(language.upper())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith('py'))
print('Py' == 'py') # it is not the same
