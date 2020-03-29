'''
Problem:

Annie finds a puppy to look after until she finds someone to adopt it.
It eats daily a certain amount of food.
Write a program that checks if the amount of food that is
purchased for the puppy will be enough until the puppy is adopted.


The console reads:
• The amount of puppy food purchased in kilograms - integer in the range [1… 100]
• Each subsequent line until you receive an 'Adopted' command, you will receive how many grams
the puppy eat for each meal - integer in the range [10… 1000]


1 line is printed on the console:
 If the amount of food is sufficient:
"Food is enough! Leftovers: {grams left over]."
 If the amount of food is insufficient to print:
"Food is not enough. You need grams more."

Example Input:
4
130
345
400
180
230
120
Adopted

Output:
Food is enough! Leftovers: 2595
grams.


Solution:

'''

food_kg = int(input())

gram = food_kg*1000
command = input().lower()
total_food = 0

while not command == 'adopted':
    n = int(command)
    total_food += n

    command = input().lower()

final = abs(total_food - gram)
if gram >= total_food:
    print('Food is enough! Leftovers: {} grams.'.format(final))
else:
    print('Food is not enough. You need {} grams more.'.format(final))
