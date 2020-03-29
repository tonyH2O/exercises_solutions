# -*- coding: utf-8 -*-
"""
Problem:  
    
A vineyard with an area of X square meters accounts for 40% of the wine production.
From 1 sq.m. vineyards are harvested Y kilograms of grapes.
2.5 lbs grapes are needed for 1 liter of wine.
The desired quantity of wine for sale is Z liters.

Write a program that estimates how much wine can be produced and whether that amount is sufficient.
If sufficient, the remainder shall be divided equally between the vineyard workers.


The input is read from the console and consists of exactly 4 lines:

1st row: X sq.m is the vineyard - integer in the interval [10… 5000].
2nd row: Y grapes per square meter - real number in the interval [0.00… 10.00].
3rd row: Z liters of wine needed - integer in the range [10… 600].
Fourth row: number of workers - integer in the interval [1… 20].

The following should be printed on the console:

If the wine produced is less than necessary:
"It will be a tough winter! More {missing wine} liters wine needed." </br> * The result should be rounded to a lower whole number.
If the wine produced is more than necessary:
"Good harvest this year! Total wine: {liters of wine} liters."
* The result must be rounded to a lower whole number.
"{Remaining wine} liters left -> {wine for 1 worker} liters per person."
* Both results must be rounded to the higher integer.


Example Input: 650      Output: Good harvest this year! Total wine: 208 liters.
                                33 liters left -> 11 liters per person.
               2
               175
               3



Solution:

"""

import math
    
x = int(input(' sq.m. of the vineyard: '))
y = float(input(' grapes per 1 sq.m. : '))
z = int(input(' wine needed in litres: '))
b = int(input(' workers: '))   

grape_kg = (x * y) * 0.4
wine_l = grape_kg / 2.5

needed = round(z - wine_l)

wine = round((wine_l + z) - z)
left_overs = wine - z
wine_per_w = math.ceil(left_overs / b)

if wine_l < z:
    print('It will be a tough winter! More {} liters wine needed.'.format(needed))
    
elif wine_l > z:
    print('Good harvest this year! Total wine: {} liters.'.format(wine))
    print('{} liters left -> {} liters per person.'.format(left_overs, wine_per_w))
    
    
    
    
    
    
    
    
    
    
    
    
    
    

