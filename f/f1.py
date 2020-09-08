


# 1

class A:

    def res(self):

        a = int(input())

        while True:
            year = str(a)
            if len(set(year)) == len(year):
                print(a)
                break
            a+=1

#A().res()


# 2

class Max:

    def res(self):

        divisor = int(input())
        bound = int(input())
        b = []
        for x in range(divisor,bound+1):
            if x%divisor == 0 and x <=bound:
                b.append(x)
            else:
                pass
        
        print(b)
        print(b[-1])

        
#Max().res()




# 3

class A:

    def res(self):

        a = int(input())
        
        b = a*100
        c = round(b*365.2422)
        d = c*24
        e = d*60

        print('{} centuries = {} years = {} days = {} hours = {} minutes'.format(a,b,c,d,e))




        
#A().res()



# 4

class A:

    def res(self):
        x = []

        for _ in range(4):
            a = int(input())
            x.append(int(a))
        c = (x[0]+x[1])/x[2] * x[3]

        print(c)

#A().res()


# 5

import math
class A:

    def res(self):

        a = int(input())
        b = int(input())

        c = a/b
        if c%2 != 0:
            c+=1
            print(math.trunc(c))
        else:
            print(c)

#A().res()





# 6


class A:

    def res(self):

        a = int(input())

        c = []

        for _ in range(a):
            b = input()
            c.append(ord(b))

        c1 = sum(c)
        print(c1)

#A().res()


# 7


class A:

    def res(self):

        a = int(input())
        b = int(input())

        for x in range(a,b+1):
            print(chr(x))


#A().res()


# 8


class A:

    def res(self):

        a = int(input())

        for x in range(0,a):
            for y in range(0,a):
                for z in range(0,a):
                    print('{}{}{}'.format(chr(97+x),chr(97+y),chr(97+z)))

#A().res()


# 9


class A:

    def res(self):

        

        b = int(input())
        A = 255
        d = 0

        for x in range(b):
            c = int(input())
            if d+c>A:
                print('Not enough space')
                continue
            else:
                d+=c

        
        print(d)

#A().res()



# 10 --------------- Ceaser Decrypt

class A:

    def res(self):

        key = int(input())
        a = int(input())
        c = []
        cc = []

        for x in range(a):
            b = input()
            c.append(b)
        for x in c:
            cc.append(ord(x)+key)

        c2 = ''.join(chr(x) for x in cc)
        print(c2)

#A().res()


# 11 ------------------

class A:

    def res(self):

        a = int(input())
        cc = 0
        left = 0
        right = 0
        c = True

        for x in range(a):
            b = input()
            if b == '(':
                cc+=1
                left+=1
                if cc>=2:
                    c = False
                    break
            elif b == ')':
                cc-=1
                right+=1
                if cc<0:
                    c = False
                    break

        if c == True and left == right:
            print('its good')
        else:
            print('not good')

#A().res()



# 12

class A:

    def res(self):

        a = int(input())
        d = input()
        b = []

        for _ in range(a):
            c = input()
            b.append(c)

        print(b)
        for x,y in enumerate(b):
            if d in y:
                print(y)

#A().res()






