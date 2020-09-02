


# Car

class Car():

    def __init__(self,name,model,en):
        self.name = name
        self.model = model
        self.en = en

    def info(self):

        return 'this is {} {} with en {}'.format(self.name,self.model,self.en)

c = Car('kia','rio','123')
print(c.info())

# shop

class Shop():

    a = []
    def __init__(self,name,a):
        self.name = name
        self.a = a

    def items(self):
        return len(self.a)

s = Shop('name', ['one','two'])
print(s.items())


# hero

class Hero():

    def __init__(self,n,h):
        self.n = n
        self.h = h

    def deff(self,dmg):
        self.h -= dmg
        if self.h <=0:
            self.h = 0
            return '{} is a goner'.format(self.n)

    def heal(self,amount):
        self.h += amount
        

h = Hero('me', 100)
print(h.deff(50))
h.heal(50)
print(h.deff(99))
print(h.deff(1))


# 4 steam

class Steam():

    games = []
    h = 0

    def __init__(self,user,games):
        self.user = user
        self.games = games


    def play(self,game,hours):
        if game in self.games:
            self.h += hours
            return '{} is playing {} currently'.format(self.user,game)
        else:
            self.games.append(game)
            self.h += hours
            return '{} plays a new game: {}'.format(self.user,game)


    def buy(self,game):
        if game in self.games:
            return '{} is already here!'.format(game)
        else:
            self.games.append(game)
            return '{} got the game: {}'.format(self.user,game)

    def stats(self):
        a = len(self.games)
        return '{} has {} games. Total play time: {}'.format(self.user,a,self.h)


u = Steam('hey' , ['hearthstone','yugi','ow'])
print(u.play('ow',3))
print(u.play('rhcp',5))
print(u.buy('cs'))
print(u.buy('rhcp'))
print(u.play('rhcp',6))
print(u.stats())

# programmer

class Programmer():

    def __init__(self,n,lan,skill):
        self.n = n
        self.lan = lan
        self.skill = skill


    def watches(self,course,lan,learned):
        if self.lan == lan:
            self.skill += learned
            return '{} watched: {}'.format(self.n,course)
        else:
            return '{} he will yet learn {}'.format(self.n,lan)

    def change(self,new,new_skill):
        if self.skill >= new_skill and self.lan != new:
            self.lan = new
            return '{} is doing {} now , previous was {}'.format(self.n,new,self.lan)

        if self.skill >= new_skill and self.lan == new:
            return '{} already knows {}'.format(self.n,new)

        if self.skill < new_skill:
            a = abs(new_skill - self.skill)
            return '{} needs {} more skills'.format(self.n,a)


p = Programmer('H', 'java', 50)
print(p.watches('pyy','python',84))
print(p.change('java',30))
print(p.change('python',100))




        
    





















