# -*- coding: utf-8 -*-
"""
Problem:

John received a parallelepiped aquarium for his birthday.
It has to be calculated how much
liters of water will the aquarium  collect,
 if it is known that a certain percentage of its capacity is occupied by sand,
plants, heater and pump.
 Its dimensions - length, width and height in inches will be
introduced by the console.
One liter of water equals one cubic decimeter (1 liter = 1 dm 3).
Write a program that calculates the liters of water needed to fill the aquarium.

Example Input: 85   Output: 248.689
               75 
               47 
               17


Solution:

"""


l = int(input('lenght in cm: '))
w = int(input('width in cm: '))
h = int(input('height in cm: '))
v = float(input('volume: '))

volume = l * w * h
litres = volume * 0.001
percent = v * 0.01
cc = 1 - percent

final = litres * cc

print('%.3f'  % final)
