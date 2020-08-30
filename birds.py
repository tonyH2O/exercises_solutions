#!/usr/bin/env python3

# Birds


class Eagle():

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Eagle'

    def needs(self):
        return 50

    def __repr__(self):
        return 'Name of the Eagle: {}, Age: {}, Gender: {}'.format(self.name,self.age,self.gender)



class Falcon():

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Falcon'

    def needs(self):
        return 45

    def __repr__(self):
        return 'Name of the Falcon: {}, Age: {}, Gender: {}'.format(self.name,self.age,self.gender)



class Crow():

    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
        self.type = 'Crow'

    def needs(self):
        return 60
        

    def __repr__(self):
        return 'Name of the Crow: {}, Age: {}, Gender: {}'.format(self.name,self.age,self.gender)




class Keeper():

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Keeper'

    def __repr__(self):
        return 'The birds keeper name: {}, Age: {}, Salary: {}'.format(self.name,self.age,self.salary)



class Caretaker():

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Caretaker'

    def __repr__(self):
        return 'The caretakers name: {}, Age: {}, Salary: {}'.format(self.name,self.age,self.salary)



class Vet():

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.type = 'Vet'

    def __repr__(self):
        return 'Name of the Vet: {}, Age: {}, Salary: {}'.format(self.name,self.age,self.salary)




class Bird_World():

    def __init__(self,name,budget,birds_capacity,worker_capacity):
        self.__birds_capacity = birds_capacity
        self.__worker_capacity = worker_capacity
        self.__budget = budget
        self.name = name
        self.birds = []
        self.work_force = []

    
    def add_bird(self,bird,price):
        if price <= self.__budget and len(self.birds) < self.__birds_capacity:
            self.birds.append(bird)
            self.__budget -= price
            return '{} the {} is added to Birds World'.format(bird.name,bird.__class__.__name__)

        elif price > self.__budget and len(self.birds) < self.__birds_capacity:
            return 'There is not enough money to get this {} bird {} '.format(bird.__class__.__name__,bird.name)

        else:
            return 'Not enough space for another bird currently'


    def hire_workers(self,worker):
        if len(self.work_force) < self.__worker_capacity:
            self.work_force.append(worker)
            return '{} the {} is hired'.format(worker.name,worker.type)
        else:
            return 'There is not enough space for new workers'


    def remove_worker(self,worker_name):
        if worker_name in self.work_force:
            self.work_force.remove(worker_name)
            return '{} was fired'.format(worker_name)
        else:
            return 'There is no more {} working in Birds World, probably fired.'.format(worker_name)


    def pay_day(self):
        to_pay = sum([x.salary for x in self.work_force])
        if to_pay <= self.__budget:
            self.__budget -= to_pay
            return 'You just paid everybody. They are happy. Budget left: {}'.format(self.__budget)
        else:
            return 'You have no budget to pay the people.'


    def tend_birds(self):
        to_tend = sum([x.needs() for x in self.birds])
        if to_tend <= self.__budget:
            self.__budget -= to_tend
            return 'All birds are being tended. They are happy. Budget left: {}'.format(self.__budget)
        else:
            return 'You have no budget for the birds.'


    def profit(self,amount):
        self.__budget += amount
        


    def birds_status(self):
        result = ''
        result += 'You have {} birds\n'.format(len(self.birds))
        result += '----- {} Eagles:\n'.format(len([x for x in self.birds if x.type == 'Eagle']))
        result += '----- {} Falcons:\n'.format(len([x for x in self.birds if x.type == 'Falcon']))
        result += '----- {} Crows:\n'.format(len([x for x in self.birds if x.type == 'Crow']))

        for a in [x for x in self.birds if x.type == 'Eagle']:
            result += '{}\n'.format(repr(a))
        for b in [x for x in self.birds if x.type == 'Falcon']:
            result += '{}\n'.format(repr(b))
        for c in [x for x in self.birds if x.type == 'Crow']:
            result += '{}\n'.format(repr(c))
        result += '\n'
        return result


    def worker_status(self):
        result = ''
        result += 'You have {} workers\n'.format(len(self.work_force))
        result += '----- {} Keepers:\n'.format(len([x for x in self.work_force if x.type == 'Keeper']))
        result += '----- {} Caretakers:\n'.format(len([x for x in self.work_force if x.type == 'Caretaker']))
        result += '----- {} Vets:\n'.format(len([x for x in self.work_force if x.type == 'Vet']))
        
        for a in [x for x in self.work_force if x.type == 'Keeper']:   
            result += '{}\n'.format(repr(a))
        for b in [x for x in self.work_force if x.type == 'Caretaker']:
            result += '{}\n'.format(repr(b))
        for b in [x for x in self.work_force if x.type == 'Vet']:
              result += '{}\n'.format(repr(b))
        result += '\n'
        return result


a = Bird_World('Uguu', 3000, 5, 8)

b = [Falcon('Yon','Male',2),Falcon('Yoll','Female',1),\
        Eagle('Sharak','Male',4),Crow('Itachi','Male',21),Crow('Samcro','Female',1),\
        Eagle('Lilly','Female',4)]
bp = [200,190,204,156,211,140]

w = [Keeper('Jax',26,100),Keeper('Scofield',29,80),Keeper('Lisa',31,95),\
        Caretaker('Sam',21,68),Caretaker('Jen',32,105),Caretaker('Mon',35,140),
        Vet('Dean',40,300),Vet('Kas',37,280),Vet('Reeves',29,220)]


for x in range(len(b)):
    bird = b[x]
    price = bp[x]
    print(a.add_bird(bird,price))


for y in w:
    print(a.hire_workers(y))

print(a.tend_birds())
print(a.pay_day())
print(a.remove_worker('Dean'))

print(a.birds_status())
print(a.worker_status())





































