# -*- coding: utf-8 -*-
"""

Problem:



A group of dancers are looking for a new hall. 

The hall they liked is rectangular and has the following dimensions:

L - length and W - width (in meters).

The hall has a square wardrobe with side - 'A', and a rectangular bench 10 times smaller than the area of ​​the hall.

The space occupied by one dancer is 40 cm² and additional 7000 cm² is required for free movement.

Write a program that calculates how many dancers can fit in the ballroom and move around freely.

The result obtained must be rounded to the nearest whole number below


Solution:

    
Example Input: 50   Output: 1592
               25
                2

"""


import math

l = float(input('lenght of the Hall in metres: '))
w = float(input('width of the Hall in metres: '))
a = float(input('the side of the wardrobe: '))

wardrobe_metres_to_cm = a * 100

hall_metres_to_cm = (l * 100) * (w * 100)
wardrobe = wardrobe_metres_to_cm * wardrobe_metres_to_cm
bench = hall_metres_to_cm / 10
free_space = hall_metres_to_cm - wardrobe - bench

dancers = free_space / (40 + 7000)

print(math.floor(dancers))