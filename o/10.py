

# person

class Person():

    def __init__(self,name,age):
        self.name = name
        self.age = age


class Child(Person):
    
    def a(self,name,age):
        super().__init__(name,age)


c = Child('lusi',12)
print(c.name)
print(c.age)

# game


class Hero:

    def __init__(self,user,lvl):
        self.user = user
        self.lvl = lvl

    def __repr__(self):
        return '{} of the type {} has level {}'.format(self.user,self.__class__.__name__,self.lvl)



class Elf(Hero):
    pass

class MusicElf(Elf):
    pass

class Wizard(Hero):
    pass

class DarkWizard(Wizard):
    pass

class SoulMaster(Wizard):
    pass

class Knight(Hero):
    pass

class DarkKnight(Knight):
    pass

class BladeKnight(Knight):
    pass




b = Elf('ren',90)
c = MusicElf('lis',1)
d = Wizard('lisi',44)
e = DarkWizard('reeen',33)
f = SoulMaster('reny',22)
g = Knight('wed',222)
h = DarkKnight('ttt',444)
i = BladeKnight('33',55)

print(b)
print(c)
print(d)



