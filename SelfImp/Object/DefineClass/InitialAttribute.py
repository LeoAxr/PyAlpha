'''
@author: Axoford12
'''
class Person(object):
    def __init__(self,name,sex,birth,**kw):
        self.name = name
        self.sex = sex
        self.birth = birth

        for k, v in kw.iteritems():
            setattr(self, k, v)
            
            
xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job