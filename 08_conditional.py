'''
conditionals ------------------->
'''

my_condition = False

if my_condition: # it is the same as if my_condition == True:
    print('it executes the if condition')


my_condition = 5 * 5

if my_condition == 10:
    print('it executes condition of the second if')

if my_condition > 10 and my_condition < 20:
    print('it is greater-than of 10 and less-than 20')
elif my_condition == 25:
    print('it is equal to 25')
else:
    print('it is less-than or equal of 10 or greater or equal of 20 or different of 25')

print('the execute continues')


my_string = ''

if not my_string:
    print('my string of text is empty')

if my_string == 'my string of text is longer':
    print('these string of texts are equals')

