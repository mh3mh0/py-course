'''
modules ------------------->
'''

import my_module # module is other file with functions
my_module.sum_value(1, 2, 2)
my_module.print_value('hi there ='')')

from my_module import sum_value, print_value # module is other file with functions, I can call the function directly.
sum_value(1, 2, 2)
print_value('hi there again ='')')

import math
print(math.pi)
print(math.pow(2, 8))

from math import pi as PI_VALUE
print(PI_VALUE)




