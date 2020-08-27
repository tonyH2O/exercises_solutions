



# single inherit

class Animal():
    
    def eat(self):
        return 'eating..'


class Dog(Animal):
    
    def bark(self):
        return 'barking..'


class Cat(Animal):
    def m(self):
        return 'meaww...'



# multi-inherit

class Person():
    def sleep(self):
        return 'sleeping...'

class Emp():
    def fired(self):
        return 'fired..'

class Teacher(Person,Emp):
    def teach(self):
        return 'teaching..'

d = Dog()
c = Cat()
t = Teacher()
print(t.sleep())
print(t.fired())
print(t.teach())

print(d.eat())
print(d.bark())
print(c.m())
print(c.eat())



# reusing

class Random(list):
    
    def element(self):
        i = 0
        return self.pop(i)
    



r = Random()
[r.append(x) for x in range(15)]
print(r.element())
print(r)

























