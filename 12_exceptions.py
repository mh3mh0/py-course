'''
exceptions handling ------------------->
'''

number_one = 5
number_two = 1
number_two = '1'

# try except

try:
    print(number_one + number_two)
    print('it is not an error')
except:
    # it is still working if an exception is produced.
    print('it is an error')

#try except else finally

try:
    print(number_one + number_two)
    print('it is not an error')
except:
    print('it is an error')
else: # optional
    # it works if an exception is not produced.
    print('it works properly')
finally: # optional
    # it works always
    print('it continues')


# exception by type
try:
    print(number_one + number_two)
    print('it is not an error')
except ValueError:
    print('it is a value-error')
except TypeError:
    print('it is a type-error')



# captured of the info of the exception
try:
    print(number_one + number_two)
    print('it is not an error')
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
