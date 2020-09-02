# 1:


'''
Play around with a stack. You will be given an integer N representing the number of elements to push into the stack,
an integer S representing the number of elements to pop from the stack and finally an integer X, an element that
you should look for in the stack. If its found, print True on the console. If it isnt, print the smallest element
currently present in the stak.

On the first line you will be given N, S and X, separated by a single space
On the next line you will be given N number of integers

in:

5 2 13
1 13 45 32 4

out:

    True

'''
'''
n = [int(x) for x in input('enter nums in 1 row: ').split()]
push,pop,searched = n

n1 = [int(x) for x in input('new nums: ').split()]

[n1.pop() for _ in range(pop)]
#for _ in range(pop):
    #n1.pop()

#print(n1)

if searched in n1:
    print('True')
else:
    if n1:
        print(min(n1))
    else:
        print(0)
'''

# 2:

'''
Write a program that counts in a given list of float values and prints the number of occurrences of each value.

in:
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

out:
    -2.5 - 3 times
    4.0 - 2 times
    3.0 - 4 times
    -5.5 - 1 times
    '''
'''
n = [float(x) for x in input('give me floats: ').split()]

print(n)

c = {}

for x in n:
    if x not in c:
        c[x] = 0
    c[x] +=1

for x,y in c.items():
    print('{} - {} times'.format(x,y))
'''




'''

Write a program, which reads a name of a student and his/her grades and adds them to the student record, then
prints the student&#39;s names with their grades and their average grade.
The order in which we print the result does not matter.


'''
from statistics import mean

def grade(a):

    d = {}

    for x in range(a):
        b,c = input('name and score: ').split()
        
        if b not in d:
            d[b] = []
        d[b].append(c)

    print(d)
    for (x,y) in d.items():
        #a = ' ',join(map(str,y))
        avg = mean(map(float,y)) # from statistics import mean
        print('{} --> {} (avg: {})'.format(x,y,avg))
    

#a = int(input('num: '))
#grade(a)






# Write a program, which will take a list of names and print only the unique names in the list.



def unq(a):

    b = []

    for x in range(a):
        n = input('name: ')
        b.append(n)

    c = set(b)

    for x in c:
        print(x)

#a = int(input('num: '))
#unq(a)




