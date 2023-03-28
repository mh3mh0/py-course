'''
classes ------------------->
'''

#class MyEmptyPerson:
    #print(MyEmptyPerson)
    #print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'no alias'):
        self.full_name = f'{name} {surname} ({alias})' # public
        self.__name = name # private

    def  get_name (self):
        return self.__name

    def walk (self):
        print(f'{self.full_name} is walking')

my_person = Person('john', 'ruiz')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person('john', 'ruiz', 'mh3mh0')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'James (bond)!!'
my_other_person.full_name = 23
print(my_other_person.full_name)


