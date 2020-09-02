

# Write a program that receives three whole numbers and print the biggest one


def big():

    b = []

    for x in range(3):
        a = int(input('num: '))
        b.append(a)

    print(b)
    b.sort()
    print(b[-1])

#big()


'''

Write a program that reads a floating-point number and prints zero if the number is zero. Otherwise, print
positive or negative. Add small if the absolute value of the number is less than 1, or large if it
exceeds 1 000 000.

'''

def fl(a):

    if a == 0:
        print('zero')
    elif a >0:
        if a <1:
            print('small positive')
        if a>=1000000:
            print('large positive')
        if a>=1 and a < 1000000:
            print('positive')

    elif a<0:
        if a<=-1 and a>-1000000:
            print('negative')
        if a>-1:
            print('small negative')
        elif a<=-1000000:
            print('large negative')
        

#a = float(input('num: '))
#fl(a)



# Write a program that receives a single word from the user, reverses it and prints it


def rev(a):

    b = a[::-1]
    print(b)

#a = input('word: ')
#rev(a)




# Write a program which reads numbers from the console until it receives a number between 1 and 100 inclusive.


def nums():

    while True:
        a = float(input('num: '))
        if a>=1 and a<=100:
            print('the number {} is between 1 and 100'.format(a))
            break

        

#nums()



# Jenny studies programming with python and wants to create a program that greets a user when he/she gives
# his/her name. Jenny however is in love with Johnny, and would like to greet him differently. Can you help her?
# write names 1 below the other and greet them, if name is Johnny greet with : hello, my love!


def love():

    while True:
        a = input('name: ').lower()

        if a == 'johnny':
            print('Hello, my LOVE!')
            break
        else:
            print('hello, {}'.format(a))

#love()




