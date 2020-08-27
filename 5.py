

# smartphone

class Smart():


    def __init__(self,memory_taken):
        self.memory_taken = memory_taken
        self.apps = []
        self.is_on = False
        memory_taken = 0

    def power(self):
        self.is_on = False if self.is_on else True

    def install(self,app,memory):
        a = memory - self.memory_taken
        if self.is_on and a < memory:
            return 'Not enough memory to install {}'.format(app)
        if not self.is_on:
            return 'Turn on your phone to install {}'.format(app)

        self.apps.append(app)
        self.memory_taken += memory


    def status(self):
        a = len(self.apps)
        return 'total apps: {}. Memory left: {}'.format(a,self.memory_taken)

s = Smart(100)
print(s.install('fb',60))
s.power()
print(s.status())

# vet

class Vet():

    animalss = []
    space = 10
    c = 0


    def __init__(self,name):
        self.name = name
        self.animals = []

    def reg(self,names):
        if self.space <= 10:
            self.c +=1
            self.animalss.append(names)
            self.animals.append(names)
            return '{} is registered'.format(names)

        else:
            return 'Not enough space'

    def unreg(self,namess):
        if namess in self.animalss and self.name in self.animals:
            self.animalss.pop(namess)
            self.animals.pop(namess)
            return '{} unregistered'.format(namess)

        else:
            return '{} not in the register'.format(namess)

    def info(self):
        a = len(self.animalss)
        b = len(self.animals)
        tot = self.c
        tot2 = abs(self.space - tot)

        return '{} has {} animals.\n{} space left in the vet.'.format(self.name,tot,tot2)


a = Vet('peter')
print(a.reg('tommy'))
print(a.reg('timi'))
print(a.info())


# glass

class Glass():
    
    cap = 250
    

    def __init__(self):
        self.content = 0
        
    def fill(self,ml):
        self.content += ml
        if self.content < self.cap:     
            return 'glass filled with {} ml'.format(self.content)
        else:
            return 'cannot add more than 250ml, with that last {}ml you atempted to add {}'.format(ml,self.content)

    def empty(self):
        self.content = 0
        return 'glass is now empty'

    def info(self):
        a =abs(self.cap - self.content)
        return '{} ml left'.format(a)

g = Glass()
print(g.fill(100))
print(g.fill(200))
print(g.empty())
print(g.fill(200))
print(g.info())





     


















