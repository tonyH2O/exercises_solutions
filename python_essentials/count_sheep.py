'''

Problem:

If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a
message: '1 sheep...2 sheep...3 sheep...' Input will always be valid, i.e. no negative integers.

Input: 5
Output: 1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...

Solution:

'''

a = int(input(': '))


def main(x):
    for y in range(1, x+1):
        print('{} sheep...'.format(y), end='')
        y += 1


main(a)
