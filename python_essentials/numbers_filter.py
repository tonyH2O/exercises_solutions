'''
Problem:

You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of
the following commands:
 even
 odd
 negative
 positive
Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result:

Input

5
33
19
-2
18
998
even

Output

[-2, 18, 998]


Solution:


'''

n = int(input('num: '))

a = []
c = []

for x in range(n):
    b = int(input('nums: '))
    a.append(b)

command = input('command: ')
if command == 'even':
    for y in a:
        if y % 2 == 0:
            c.append(y)
elif command == 'odd':
    for y in a:
        if y % 2 != 0:
            c.append(y)
elif command == 'negative':
    for y in a:
        if y < 0:
            c.append(y)
elif command == 'positive':
    for y in a:
        if y >= 0:
            c.append(y)


print(c)
