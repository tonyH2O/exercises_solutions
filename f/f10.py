


# 1
# You will receive a single number n. On the next n lines you will receive names of courses. You have to create a list of
#them and print it



def cour():

    b = [input('course: ') for x in range(int(input('n: ')))]

    print(b)

#cour()



# 2
#You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
# One with all the positives (including 0)
# One with all the negatives
# and count of positives // sum of negatives


def pos():

    a = int(input('n: '))
    b = []
    b1 = []
    for x in range(a):
        a = int(input('nn: '))
        
        if a >= 0:
            b.append(a)
        else:
            b1.append(a)

    print(b)
    print(b1)
    print(len(b))
    print(sum(b1))

#pos()




# 3
#You will receive a number n and a word. On the next n lines you will be given some strings. You have to add them in
#a list and print them. After that you have to filter out only the strings that include the given word and print that list
#also


def pos():

    a = int(input('n: '))
    b = input('key: ')
    c = []

    for x in range(a):
        a = input('write: ')
        c.append(a)
    print(c)
    for x in c:
        if b in x:
            print(x)
            

#pos()



# 4
#You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of
##the following commands:
###     even
 #    odd
 #    negative
 #    positive
#    Filter all the numbers that fit in the category (0 counts as a positive). Finally, print the result




def pos():

    a = int(input('n: '))
    b = []
    
    for _ in range(a):
        a = int(input('nn: '))
        b.append(a)
    c = input('command: ')

    if c == 'even':
        for x in b:
            if x%2 == 0:
                print(x)

    #finish the rest the same way
    
    
    print(b)

#pos()




# 5 
#Write a program that receives a single string containing numbers separated by a single space. Print a list containing
#the opposite of each number


def pos():

    a = list(map(int,input('str: ').split()))
    print(a)
    b = []

    for x in a:
        if x == 0:
            pass
        elif x > 0:
            x = -(x)
        elif x < 0:
            x = abs(x)
        
        b.append(x)
    print(b)


#pos()







































