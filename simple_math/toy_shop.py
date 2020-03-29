# -*- coding: utf-8 -*-
"""
Problem:
    

A man has a toy store. He gets a big order to fulfill. With the money that
he will win, he wants to go on a field trip. Write a program that calculates the profit from the order.
Toy prices:
 Puzzle - 2.60 .
 Talking doll - 3 
 Teddy Bear -  4.10
 Minion - 8.20 
 Truck - 2 
If the toys ordered are 50 or more, the discount is 25% off the total price. Of the winners
money the man has to give 10% for the rent of the store. Calculate if the money will go to his
vacation.    
    

The console reads 6 lines:
1. Price of the excursion - real number;
2. Number of puzzles - integer;
3. Number of talking dolls - whole number;
4. Number of teddy bears - integer;
5. Number of minions - integer;
6. Number of trucks - integer.

Exit
The console prints:
 If enough money is printed:
 Yes! {money remaining} money left. 
 If the money is NOT sufficient, it is printed:
 Not enough money! {missing money} more needed. 
The result should be formatted to the second character after the decimal point.

Solution:

"""


vacation = float(input('price: '))
lego = int(input('num: '))
barbi = int(input('num: '))
bear = int(input('num: '))
minion = int(input('num: '))
truck = int(input('num: '))

lego_p = lego * 2.60
barbi_p = barbi * 3
bear_p = bear * 4.10
minion_p = minion * 8.20
truck_p = truck * 2


total0 = lego + barbi + bear + minion + truck
total = lego_p + barbi_p + bear_p + minion_p + truck_p

toys_discount = total - ((25/100) * total)

rent_no_d = 10/100 * total
rent_d = 10/100 * toys_discount


money_vac = total - rent_no_d
money_vac2 = toys_discount - rent_d

rest = abs(vacation - money_vac)
rest2 = abs(vacation - money_vac2)

if money_vac >= vacation and total0 < 50:
    print('Yes! {:.2f} money left.'.format(rest))
    
elif money_vac2 >= vacation and total0 >= 50:
    print('Yes! {:.2f} money left.'.format(rest2))

elif money_vac2 < vacation and total0 >= 50:
    print('Not enough money! {:.2f} more needed.'.format(rest2))

else:
    print('Not enough money! {:.2f} more needed.'.format(rest))
    
    
    
    
    
    
    
    
