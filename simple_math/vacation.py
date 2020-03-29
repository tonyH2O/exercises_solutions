# -*- coding: utf-8 -*-
"""

Problem:
    
Oddly enough, most people plan for a break early. A young programmer has a set budget and free time in a given season.

Write a program that accepts budget and season input, and outputs where the programmer will spend and how much to spend.

The budget determines the destination, and the season determines how much of the budget will be spent.
If it is summer, he will rest on a camping site, and for  winter - on a hotel.
If he is outside of his country, regardless of the season, he will rest in a hotel.
Each campsite or hotel, depending on the destination, has its own price that corresponds to a percentage of the budget:

At $ 1000 or less - anywhere in his country.
Summer - 30% of the budget.
Winter - 70% of the budget.
At $ 10 000 or less - somewhere near his country.
Summer - 40% of the budget.
Winter - 80% of the budget.
At more than 10 000 USD - somewhere in another continent.
When traveling in another continent, regardless of the season, he will spend 90% of its budget


Input data
The input is read from the console and consists of two lines:
    
In the first line we get the budget - real number
In the second row - one of the two possible seasons: "summer" or "winter".


Output data
Two lines must be printed on the console.

First - "Somewhere in {destination}" among "Country side", "Near contries" and "Other continent".
Second line - "{Vacation type} - {Spend amount}".
Holidays can be between "Camp" and "Hotel".
The amount must be rounded to the nearest second character after the decimal point.




Solution:

"""


budget = float(input('budget: '))
season = input('enter season: ').lower()

summertime1 = (30/100) * budget
wintertime1 = (70/100) * budget

summertime2 = (40/100) * budget
wintertime2 = (80/100) * budget

summertime3 = (90/100) * budget
wintertime3 = (90/100) * budget

a = 'Country side'
b = 'Near contries'
c = 'Other continent'

d = 'Camp'
e = 'Hotel'
    
    

if budget <= 1000 and season == 'summer':
    print('Somwhere in {}'.format(a))
    print('{} - {:.2f}'.format(d, summertime1))
elif budget <= 1000 and season == 'winter':
    print('Somwhere in {}'.format(a))
    print('{} - {:.2f}'.format(e, wintertime1))
    
    
if budget > 1000 and budget <= 10000 and season == 'summer':
    print('Somwhere in {}'.format(b))
    print('{} - {:.2f}'.format(d, summertime2))
elif budget > 1000 and budget <= 10000 and season == 'winter':
    print('Somwhere in {}'.format(b))
    print('{} - {:.2f}'.format(e, wintertime2))
    
if budget >  10000 and season == 'summer':
    print('Somwhere in {}'.format(c))
    print('{} - {:.2f}'.format(e, summertime3))
elif budget >  10000 and season == 'winter':
    print('Somwhere in {}'.format(c))
    print('{} - {:.2f}'.format(e, wintertime3))



























