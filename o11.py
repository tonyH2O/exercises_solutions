


# 1:

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self,fuel_q, fuel_c):
        self.fuel_q = fuel_q
        self.fuel_c = fuel_c

    @abstractmethod
    def drive(self,distance):
        pass

    @abstractmethod
    def refuel(self,fuel):
        pass


class Car(Vehicle):

    def __init__(self,fuel_q,fuel_c):
        super().__init__(fuel_q,fuel_c)

    def drive(self,distance):
        fuel_needed = distance*(self.fuel_c + 0.9)
        if fuel_needed <= self.fuel_q:
            self.fuel_q -= fuel_needed

    def refuel(self,fuel):
        self.fuel_q += fuel






c = Car(20,5)
c.drive(3)
#print(c.fuel_q)
c.refuel(10)
#print(c.fuel_q)





# 2


class Food(ABC):
    @abstractmethod
    def __init__(self,q):
        self.q = q


class Vegi(Food):

    def __init__(self,q):
        super().__init__(q)



class Fruit(Food):

    def __init__(self,q):
        super().__init__(q)


class Meat(Food):

    def __init__(self,q):
        super().__init__(q)



class Seed(Food):

    def __init__(self,q):
        super().__init__(q)




class Animal(ABC):
    @abstractmethod
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0


class Bird(Animal, ABC):
    def __init__(self,name,weight,wings):
        super().__init__(name,weight)
        self.wings = wings




class Owl(Bird):

    def __init__(self,name,weight,wings):
        super().__init__(name,weight,wings)


o = Owl('Micky',5,2)
print(o)












