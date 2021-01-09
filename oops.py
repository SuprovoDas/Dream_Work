"""class person:
    name = 'A'
    age = 22
    def talk(cls):
        print(cls.name)
        print(cls.age)

p1 = person()
p1.talk()"""

"""class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    
    def talk(self):
        print('My friend is',self.name)
        print('His age is',self.age)
        print('His address is ',self.address)

p1 = Student('Arindam',50,'RoyPara')
p1.talk()
print(id(p1))"""



class sample:
    def __init__(self):
        self.x =10
    def modify(self):
        self.x+=1
s1= sample()
s2=sample()

print('x in s1 = ',s1.x)
print('x in s2 =',s2.x)
s1.modify()
print('x in s1 = ',s1.x)
print('x in s2 =',s2.x)


class sample2:
    x=10
    @ classmethod
    def modify(cls):
        cls.x+=1
s1= sample2()
s2= sample2()
print('\n')
print('x in s1 = ',s1.x)
print('x in s2 = ',s2.x)
s1.modify()
print('x in s1 = ',s1.x)
print('x in s2 = ',s2.x)