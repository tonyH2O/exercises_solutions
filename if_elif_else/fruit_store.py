'''
Problem: 


On weekdays, a fruit shop operates at the following prices:
fruit: banana apple orange grapefruit kiwi pineapple grapes
price: 2.50    1.20 0.85   1.45       2.70   5.50    3.85

On Saturdays and Sundays, the store operates at higher prices:
fruit: banana apple orange grapefruit kiwi pineapple grapes
price: 2.70   1.25  0.90   1.60       3.00   5.60    4.20

Write a program that reads from the console the following three user-entered variables and calculates
the price according to the prices in the tables above:
 fruit - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
 day of the week - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday /
Sunday;
 quantity (real number).
Print the result rounded by 2 digits after the decimal point. In case of an invalid day of the week or
invalid fruit name to print 'error'.

Example Input:
apple
Tuesday
2
Output:
2.40

'''

product = input('product: ').lower()
day = input('day of the week:').lower()
q = float(input('quantity of the product:'))

result = 0

if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if product == 'banana':
        result = 2.50
    elif product == 'apple':
        result = 1.20
    elif product == 'orange':
        result = 0.85
    elif product == 'grapefruit':
        result = 1.45
    elif product == 'kiwi':
        result = 2.70
    elif product == 'pineapple':
        result = 5.50
    elif product == 'grapes':
        result = 3.85
    else:
        print('error')


elif day == 'saturday' or day == 'sunday':
    if product == 'banana':
        result = 2.70
    elif product == 'apple':
        result = 1.25
    elif product == 'orange':
        result = 0.90
    elif product == 'grapefruit':
        result = 1.60
    elif product == 'kiwi':
        result = 3.00
    elif product == 'pineapple':
        result = 5.60
    elif product == 'grapes':
        result = 4.20
    else:
        print('error')


total = result * q
print('%.2f' % total)
