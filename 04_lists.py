'''
lists ------------------->
'''

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [335, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, 'john', 'ruiz']

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname, = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)

my_other_list.append('memento')
print(my_other_list)

my_other_list.insert(1, 'Red')
print(my_other_list)

my_other_list[1] = 'blue'

my_other_list.remove('blue')
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = 'Hi there!!'
print(my_list)
print(type(my_list))