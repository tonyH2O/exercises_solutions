


# person

class Person():

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def getn(self):
        return self.__name

    def geta(self):
        return self.__age

p = Person('Ned',12)
print(p.getn())
print(p.geta())



# email

class Email():

    def __init__(self,minl,mails,dom):
        self.__minl = minl
        self.__mails = mails
        self.__dom = dom

    def __vn(self,name):
        return self.__minl <= len(name)

    def __vm(self,mail):
        return mail in self.__mails

    def __vd(self,doms):
        return doms in self.__dom

    def __parts(self,email):
        start = email.index('@')
        end = email.index('.')
        user = email[:start]
        mail = email[start+1:end]
        domain = email[end+1:]
        return [user,mail,domain]



    def info(self,email):
        [name,mail,doms] = self.__parts(email)

        return self.__vn(name) and\
                self.__vm(mail) and\
                self.__vd(doms)


m = ['gmail','su']
d = ['com','bg']
e = Email(6,m,d)
print(e.info('pe77er@gmail.com'))



# mammal

class Mammal():

    

    def __init__(self,name,typee,sound):
        self.name = name
        self.typee = typee
        self.sound = sound
        self.__kingdom = 'animals'

    def ms(self):
        return '{} makes {}'.format(self.name,self.sound)

    def k(self):
        return self.__kingdom

    def info(self):
        return '{} is of type: {}'.format(self.name,self.typee)


m = Mammal('dog','home','bark')
print(m.ms())
print(m.k())
print(m.info())


# account

class Account():

    def __init__(self,idd,bal,pin):
        self.__idd = idd
        self.bal = bal
        self.__pin = pin

    def i(self,pinn):
        if pinn == self.__pin:
            return self.__idd
        else:
            return 'wrong pin'

    def b(self):
        return self.bal

    def change(self,old,new):
        if old == self.__pin:
            old == new
            return 'pin changed'
        else:
            return 'wrong pin yo'

a = Account(12,100,123)
print(a.i(1111))
print(a.i(123))
print(a.b())
print(a.change(2222,11111))
print(a.change(123,1111))


