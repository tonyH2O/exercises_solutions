'''

Problem:



Programmer decided to spend his holidays in Ski Town. However, before he leaves, he has to make a reservation for
hotel and calculate how much it would cost him to stay.
There are the following types of premises with the following
prices for stay:
'room for one person' - 18.00 USD per night
'apartment' - 25.00 USD per night
'president apartment' - 35.00 USD per night
According to the number of days he will stay at the hotel (example: 11 days = 10 nights) and the type of room,
whichever he chooses, he may enjoy a different discount. The reductions are as follows:


room type:           'less than 10 days'    'between 10 and 15 days'   'more than 15 days'
room for one person: does not use discount   does not use discount    does not use discount
apartment:           30% of final price       35% of final price         50% of final price
president apartment: 10% of final price       15% of final price         20% of final price

After the stay, the Programmer's assessment of the hotel services may be positive(positive) or negative
(negative). If positive --> the Coder adds 25% of the price.
If his estimate is a negative ---> deduction from the price of 10%.


Example Input:
30
president apartment
negative

Output:

730.80

Solution:

'''

stay = int(input('stay: '))
room = input('room: ').lower()
rate = input('rate: ').lower()

a = 'room for one person'
b = 'apartment'
c = 'president apartment'

d = stay - 1
f1 = d*25
f3 = d * 35
f = 0
p = 25/100 * (d*18)
p1 = 25/100 * f1
n = 10/100 * (d*18)


if room == a and rate == 'positive':
    if stay < 10 or (stay >= 10 and stay <= 15) or stay > 15:
        f = d * 18 + (25/100 * (d*18))
        print('%.2f' % f)

elif room == a and rate == 'negative':
    if stay < 10 or (stay >= 10 and stay <= 15) or stay > 15:
        f = d * 18 - (10/100 * (d*18))
        print('%.2f' % f)

elif room == b and rate == 'positive':
    if stay < 10:
        f = f1 - (30/100*f1) + 25/100*(f1 - (30/100*f1))
        print('%.2f' % f)
    elif stay >= 10 and stay <= 15:
        f = (f1 - (35/100*f1)) + 25/100*(f1 - (35/100*f1))
        print('%.2f' % f)
    elif stay > 15:
        f = (f1 - (50/100*f1)) + 25/100*(f1 - (50/100*f1))
        print('%.2f' % f)

elif room == b and rate == 'negative':
    if stay < 10:
        f = f1 - (30/100*f1) - 10/100*(f1 - (30/100*f1))
        print('%.2f' % f)
    elif stay >= 10 and stay <= 15:
        f = (f1 - (35/100*f1)) - 10/100*(f1 - (35/100*f1))
        print('%.2f' % f)

    elif stay > 15:
        f = (f1 - (50/100*f1)) - 10/100*(f1 - (50/100*f1))
        print('%.2f' % f)

elif room == c and rate == 'positive':
    if stay < 10:
        f = f3 - (10/100*f3) + 10/100*(f3 - (10/100*f3))
        print('%.2f' % f)
    elif stay >= 10 and stay <= 15:
        f = (f3 - (15/100*f3)) + 25/100*(f3 - (15/100*f3))
        print('%.2f' % f)
    elif stay > 15:
        f = (f3 - (20/100*f3)) + 25/100*(f3 - (20/100*f3))
        print('%.2f' % f)

elif room == c and rate == 'negative':
    if stay < 10:
        f = f3 - (10/100*f3) - 10/100*(f3 - (10/100*f3))
        print('%.2f' % f)
    elif stay >= 10 and stay <= 15:
        f = (f3 - (15/100*f3)) - 10/100*(f3 - (15/100*f3))
        print('%.2f' % f)

    elif stay > 15:
        f = (f3 - (20/100*f3)) - 10/100*(f3 - (20/100*f3))
        print('%.2f' % f)
