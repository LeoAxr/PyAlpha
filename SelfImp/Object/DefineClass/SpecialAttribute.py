'''
@author: Axoford12
'''
class Person(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
print p.__score