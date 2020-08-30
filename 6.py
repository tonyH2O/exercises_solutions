
import math


# point

class Point():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def x2(self,newx):
       self.newx = 1 + self.x
        

    def y2(self,newy):
        self.newy = 1+self.y
        

    def dc(self,x,y):
        a = x - self.newx
        b = y - self.newy
        d = math.sqrt(a**2 + b**2)
        return d

p = Point(2,4)
p.x2(3)
p.y2(5)
print(p.dc(10,2))

# circle

class Circle():

    pi = 3.14

    def __init__(self,rad):
        self.rad = rad

    def newr(self,newr):
        self.newr = newr

    def area(self):
        a = self.pi*(self.newr**2)
        return a

    def c(self):
        c = 2*self.pi*self.newr
        return c

cc = Circle(10)
cc.newr(12)
print(cc.area())
print(cc.c())

# account

class Account():

    def __init__(self,idd,name,bal):
        self.idd = idd
        self.name = name
        self.bal = bal

    def credit(self,amount1):
        self.bal += amount1
        return self.bal

    def  debit(self,amount2):
         if amount2 <= self.bal:
             self.bal -= amount2
             return self.bal
         else:
             return 'amount is bigger than the balance'

    def info(self):
        return 'User {} with account id: {} has a balance of: {}'.format(self.name,self.idd,self.bal)


a = Account(1,'ren',1000)
print(a.credit(500))
print(a.debit(1500))
print(a.info())

# employee

class Emp():

    def __init__(self,idd,first,last,salary):
        self.idd = idd
        self.first = first
        self.last = last
        self.salary = salary

    def name(self):
        return '{} {}'.format(self.first,self.last)

    def r(self,x):
        self.x = x
        self.x += self.salary
        return self.x

    def pay(self):
        a = self.x*12
        return a

e = Emp(1,'ren','busi',1000)
print(e.name())
print(e.r(500))
print(e.pay())

 

