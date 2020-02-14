# -*- coding: utf-8 -*-
"""

Problem:
    
The cat Tom loves to sleep all day long,
unfortunately his owner plays with him whenever he has free time.
To get a good night's sleep, Tom's playing rate is 30,000 minutes a year.
Tom's playing time depends on his master's weekends:

When at work, his landlord plays with him 63 minutes a day.
When resting, his landlord plays with him 127 minutes a day.

Write a program that introduces the number of days off and prints whether Tom can sleep well
and how much the difference is from the current year's norm, assuming the year is 365 days.

Example: 20 weekdays -> weekdays are 345 (365 - 20 = 345).
Real-time play time is 24 275 minutes (345 * 63 + 20 * 127).
The difference from the norm is 5 725 minutes (30 000 - 24 275 = 5 725) or 95 hours and 25 minutes.


Example Input: 113   Output: Tom will run away
                             3 hours and 47 minutes for play

Solution:



"""


p = int(input('days-off of the owner: '))

play_norm = 30000
work_days = 365 - p
play_time = (work_days * 63) + (p * 127)

p_norm1 = play_norm - play_time

p_norm = play_norm - play_time

h1 = abs(p_norm1 // 60)
m2 = abs(p_norm1 % 60)

h = abs(p_norm // 60)
m = abs(p_norm % 60)

if play_time > play_norm:
    print('Tom will run away')
    print('{} hours and {} minutes more for play' .format(h, m ))
    
elif play_time < play_norm:
    print('Tom sleeps well')
    print('{} hours and {} minutes less for play' .format(h1, m2 ))
    
    
    
    
    
    
    
    
    
    
    
    
    