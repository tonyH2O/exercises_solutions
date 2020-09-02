

# Write program that reads a matrix from the console and print:
# Sum of all matrix elements
# The matrix itself


def matrix():

    a,b = map(int,input('2 nums for row and cols: ').split(','))

    d = []
    s = 0

    for x in range(a):
        c = list(map(int, input('nums: ').split(',')[:b])) # [:b] sets limit of "b" numbers in the row
        d.append(c)

    for x in range(len(d)):
        s += sum(d[x])
        
    return '{}\n{}'.format(s,d)


    

#print(matrix())




# write program that reads a matrix from console and print the sum for each column. On first line you will get matrix
#rows. On the next rows lines, you will get eliements for each column separated with a space.






def matrix2():

    a,b = map(int,input('row and col: ').split(','))

    d = []
    

    for x in range(a):
        c = list(map(int, input('n: ').split()[:b]))
        d.append(c)
    
    s = [0]*len(d[0])
    for x in range(len(d)):
        for y in range(len(d[0])):
            s[y] += d[x][y]

    for x in s:
        print(x)


#matrix2()






# Write a program that finds the sum of matrix primary diagonal. starting from left [0] index
# 


def matrix3():

    a = int(input('enter num: '))

    b = []

    for x in range(a):
        c = list(map(int,input('n: ').split()[:a]))
        b.append(c)

    s = 0


    for x in range(len(b)):
        s+= b[x][x]
        

    print(s)

#matrix3()



# compare the left and right diagonals of a matrix


def m4():

    a = int(input('num: '))

    b = []

    for x in range(a):
        c = list(map(int, input('n: ').split()[:a]))
        b.append(c)

    s = 0
    s2 =0

    for x in range(len(b)):
        s+=b[x][x]
        s2+= b[x][a-x-1]

    print(s)
    print(s2)
    t = abs(s-s2)
    print(t)

#m4()








