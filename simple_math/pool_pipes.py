# -*- coding: utf-8 -*-
"""

Problem:

A volume V tank has two pipes from which it is filled.
Each pipe has a specific flow rate (liters of water passing through one pipe in one hour).
The worker runs the pipes simultaneously and exits for N hours.
Write a program that outputs the pool status, the moment the worker returns.


There are four lines read from the console:

The first line contains the number V - volume of the pool in liters - an integer in the range [1… 10000].
The second line contains the number P1 - flow rate of the first tube per hour - integer in the interval [1… 5000].
The third line contains the number P2 - flow rate of the second tube per hour - an integer in the interval [1… 5000].
The fourth line contains the number H - hours in which the employee is absent - floating point number in the interval [1.0… 24.00].


Print one of the two possible states on the console:

How much the pool was filled and which pipe contributed how much.
Format all percentages to an integer (without rounding).
"The pool is [x]% full. Pipe 1: [y]%. Pipe 2: [z]%."
If the pool is overfilled - how many liters it has overflowed in a given time, floating point number.
"For [x] hours the pool overflows with [y] liters."
Note that due to rounding to the whole number, data is lost and normally the sum of the percentages is 99%, not 100%.


Solution:
    
    
Example input:   Output: The pool is 66% full. Pipe 1: 45%. Pipe2: 54%

    1000
    100
    120
    3



"""


import math

v = int(input('vol of the pool in litres: '))
p1 = int(input('pipe #1 for 1h: '))
p2 = int(input('pipe #2 for 1h: '))
h = float(input('worker is missing for N hours: '))


water = (p1 + p2) * h

if water <= v:
    print('The pool is {}% full. Pipe 1: {}%. Pipe 2: {}%.' .format(
        
        math.trunc((water * 0.1)),
        math.trunc(p1 * (h/water) * 100),
        math.trunc(p2 * (h/water) * 100),
        
        ))
    
else:
    print('For {} hours the pool overflows with {} litres.' .format(
        
        h,
        water - v,
        
          ))
    
    
    
    
    
    
    

