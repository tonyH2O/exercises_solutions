from collections import deque

# 1. - reverse input string


def rev(a):

    r = []

    for x in a:
        r.append(x)

    revv = ''

    while r:
        revv += r.pop()

    return revv

print(rev('I love Python'))


# 2. - matching brackets


def mat(a):

    r = []
    r2 = []

    for x in range(len(a)):
        x1 = a[x]
        if x1 == '(':
            r.append(x)
        elif x1 == ')':
            start = r.pop()
            end = x
            r2.append(a[start:end+1])

    return r2


s = '1+(2-(2+3)*4/(3+1))*5'
for x in mat(s):
    print(x)

# 3. - supermarket


def super():

    names = deque()

    while True:
        command = input('names: ').lower()
        if command == 'end':
            print('{} people remaining'.format(len(names)))
            break

        if command == 'paid':
            while names:
                print(names.popleft())

        else:
            names.append(command)





super()


