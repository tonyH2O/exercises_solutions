

# Read two names and a delimiter. Print the names joined by the delimiter.


a = 'Name1'
b = 'Name2'
#c = input('delimeter: ')

#print('{} {} {}'.format(a,c,b))




#  A number is special when its sum of digits is 5, 7 or 11.
# Write a program to read an integer n and for all numbers, in the range 1…n, print the number and if it is
# special or not (True / False).

# example 14 is True --> 14 = 1+4 = 5 --> True , 5 is True --> 5+0 = 5



def special(a):


    for x in range(1,a+1):
        sum_nums = 0
        num = x
        while num > 0:
            sum_nums += num%10
            num = int(num/10)
            if (sum_nums == 5) or (sum_nums == 7) or (sum_nums == 11):
                print('{} -> True'.format(x))
            else:
                print('{} -> False'.format(x))

#a = int(input('enter num: '))
#special(a)





# Read four integer numbers. Add first to the second, divide (integer) the sum by the third number and multiply the
#result by the fourth number. Print the result.

# in: 10,20,3,3 --> out: 30




def op():

    b = []

    for x in range(4):
        a = int(input('num: '))
        b.append(a)

    c = b[0]+b[1]
    c2 = c / b[2]
    c3 = c2*b[3]
    print(c3)

op()




