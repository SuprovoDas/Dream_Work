"""class father:
    def height(self):
        print('height is 6 feet')
class mother:
    def color(self):
        print('color is dark')

class child(father,mother):
    pass

c = child()

c.height()
c.color()"""

class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()

        
class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()


class D(object):
    def __init__(self):
        self.d = 'd'
        print(self.d)
        super().__init__()

class E(object):
    def __init__(self):
        self.e = 'e'
        print(self.e)
        super().__init__()



class C(A,B,D,E):
    def __init__(self):
        super().__init__()
        self.c = 'c'
        print(self.c)
        

o = C()
print(C.mro())
#MRO = Method Resolution Order)
""" polymorphism :- If a variable,object,method exhibit deffent in diffent context then it is called polymorphism.
