


class Person:

    def __init__(self,name):
        self.name = name

    def hi(self):
        print('hi, my name is {}'.format(self.name))

#p = Person('Mee')
#p.hi()
a = Person('Mee M')
b = Person('Yoo Y')
a.hi()
b.hi()



#Create a class with name Comment. The __init__ method should accept 3 parameters
# username
# content
# likes (optional, 0 by default)
#Use the exact names for your variables


class Comment:

    def __init__(self,user,c,likes=0):
        self.user = user
        self.c = c
        self.likes = likes


a = Comment('user1','I like this book')
print(a.user)
print(a.c)
print(a.likes)






#Create a class Party that only has an attribute called people. The __init__ method should not accept any
#parameters. You will be given names of people (on separate lines) until you receive the command &quot;End&quot;. Use the
#created class to solve this problem. After you receive the end command print 2 lines:



class Party:

    def __init__(self):
        self.b = []


    def people(self):

        command = ' '

        while not command == 'end':
            self.b.append(command)
            command = input('name: ')
            
            
        self.b.pop(0)
        print('Going to the party: {}'.format(', '.join(x for x in self.b)))

        #print(*b)

        print('Total: {}'.format(len(self.b)))

p = Party()
#p.people()









#####

'''

class Email:

    def __init__(self,sender,receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True

    def get_info(self):
        return '{} says to {}: {}. Sent: {}'.format(self.sender,self.receiver,self.content,self.is_sent)

class MailBox:


    def __init__(self):
        self.emails = []

    def add_e(self,email):
        self.emails.append(email)

    def sent_e(self,sent):
        for x in sent:
            self.emails[x].send()

    def printt(self):
        for x in self.emails:
            print(x.get_info())


m = MailBox()

while True:
    command = input('text: ')
    if command == 'stop ':
        break

    a,b,c = command.split(' ')
    e = Email(a,b,c)
    m.add_e(e)


sent = list(map(int, input('id of the mails we need to sent(indexes): ').split(', ')))

m.sent_e(sent)
m.printt()




'''


##############
'''

class Zoo:

    __animals = 0

    def __init__(self,name):
        self.name = name
        self.m = []
        self.f = []
        self.b = []


    def add_a(self,species,n):
        if species == 'mammal':
            self.m.append(n)
        elif species == 'fish':
            self.f.append(n)
        elif species == 'bird':
            self.b.append(n)
        Zoo.__animals += 1

    def get_info(self,e):
        result = ''
        if e == 'mammal':
            result += 'Mammals in {}: {}\n'.format(self.name,','.join(self.m))
        # to be finished
        
        result += 'Total animals in the zoo: {}'.format(Zoo.__animals)
        return result


a = input('name of the zoo: ')
z = Zoo(a)

b = int(input('how many: '))

for x in range(b):
    c,d = input('species and name: ').split()
    z.add_a(c,d)

e = input('what?: ')

print(z.get_info(e))



'''






































