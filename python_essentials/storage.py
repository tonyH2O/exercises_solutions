'''
Problem:

Create a class Storage. The __init__ method should accept one parameter: the capacity of the storage.
The Storage class should also have an attribute called storage, where all the items will be stored.
 The class should have
two additional methods:
 add_product(product) - adds the product in the storage if there is space for it
 get_products() - returns the storage list

Solution:
'''


class Storage():

    def __init__(self, x):
        self.x = x
        self.store = []

    def add_prod(self, y):
        if len(self.store) < self.x:
            self.store.append(y)

    def get_prod(self, z):
        return z


a = Storage(2)
a.add_prod('apple')
a.add_prod('strawberry')
a.add_prod('milk')
a.add_prod('bread')
print(a.get_prod(a.store))
