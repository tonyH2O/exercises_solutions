# -*- coding: utf-8 -*-
"""
Problem: 
    
The company receives a request for a project that requires a certain number of hours.
The company has a certain number of days. During 10% of the days,
employees are trained and unable to work on the project.
One normal working day at the company is 8 hours.
The project is important for the company and every employee is obliged to work on the project during off-hours 2 hours a day.

Hours must be rounded to a lower integer (eg → 6.98 hours rounded to 6 hours).

Write a program that calculates whether the company can complete the project on time and how many hours they do not reach or remain.
    

The input is read from the console and contains exactly 3 lines:

The first line requires the required hours - an integer in the range [0… 200,000].
In the second line are the days the company has available - an integer in the range [0… 20,000].
The third line is the number of all employees - an integer in the range [0… 200].

Print one line on the console:

If time is sufficient: "Yes! {Hours remaining} hours left.".
If the time is NOT enough: "Not enough time! {Hours not needed}.".

Example Input: 90      Output: Yes! 99 hours left.
               7
               3

Solution:
    
"""


import math    
    
h = int(input('hours needed: '))
d = int(input('days needed: '))
b = int(input('workers: '))


day = b * (8+2)
training = math.floor(day * 0.1)
work = day - training

end = work * d
left = abs(end - h)


if end >= h:
    print('Yes! {} hours left.'.format(left))
    
elif end < h:
    print('Not enough time! {} hours needed.'.format(left))
    
    
    
    
    
    
    
    
    
    
    
    
