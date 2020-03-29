
'''
Problem:

The wedding is approaching and John will organize Smith's bachelor party at his restaurant,
 knowing that Smith will invite several groups of your acquaintances.
 John needs your help. Write a program that
calculates how many guests the restaurant will collect,
 what its revenue from the bachelor party will be,
 and whether John will be able to afford to pay the guest artist, knowing that:

 If the reservation is for a group of less than 5 people, the envelope for one person will be 100 USD.
 If the reservation is for a group of 5 or more people, the envelope for one person will be 70 USD.

Sign in
The console reads:

 Amount for guest contractor - integer in the range [1… 4500]
 On each successive line (until receiving the "The restaurant is full" command) - the number of people
in each group.

Exit
Print one of the following lines on the console:

 If John manages to afford a guest performer:
"You have {guests} guests and {leftover} USD left."
 If John fails to afford a guest contractor:
"You have {guests} guests and {income} USD income, but no singer."

Example:
Input:

2800
5
5
4
6
6
12
12
The restaurant is full

Output:

You have 50 guests and 820 USD left.


Solution:

'''


money = int(input('the money for the singer: '))

ppl = 0
data = input('group of guests: ').lower()
total = 0
guests = 0
g = 0

while not data == 'the restaurant is full':
    ppl = int(data)
    if ppl < 5:
        guests = ppl
        ppl *= 100

    elif ppl >= 5:
        guests = ppl
        ppl *= 70

    data = input('group of guests: ').lower()
    total += ppl
    g += guests

final = abs(total - money)

if total >= money:
    print('You have {} guests and {} USD left.'.format(g, final))
else:
    print('You have {} guests and {} USD income, but no singer.'.format(g, total))
