

# 1

class Exp:

    def res(self):

        a = (3522 + 52353) * 23 - (2336 * 501 + 23432 - 6743) * 3
        print(a)

Exp().res()

# 2

class Nums:

    def res(self):

        for x in range(1,20+1):
            print(x)

#Nums().res()



# 3

class Stars:

    def res(self):

        a = '*'

        for x in range(55):
            print(a*x)
            

#Stars().res()



# 4

class Area:

    def res(self):

        a = int(input())
        b = int(input())
        c = a*b
        print(c)

#Area().res()




# 5

class StarsQ:

    def res(self):

        a = int(input())
        b = '*'

        print(b*a)
        for x in range(1,a-1):
            print(b+' '*(a-2)+b)
        print(b*a)

#StarsQ().res()



# 6

class Dd:

    def res(self):

        a = int(input())
        print(a*a)

#Dd().res()


# 7


class Inch:

    def res(self):

        a = float(input())
        b = a*2.54
        print(b)

#Inch().res()



# 8

class Hi:

    def res(self):

        a = input()
        b = 'Hello, '+a
        print(b)

#Hi().res()



# 9

class Hii:

    def res(self):

        a,b,c,d = input().split()
        cc = int(c)
        print('You are '+a+' '+b+', a',cc,'-years old person from '+d)

#Hii().res()


# 10


class Tra:

    def res(self):

        a,b,c = map(int, input().split())
        d = (a+b)*c/2
        print(d)

#Tra().res()



# 11

import math

class Perim:

    def res(self):

        a = float(input())
        aa = math.pi*a*a
        p = 2*math.pi*a
        print('Area: {}\nPerimeter: {}'.format(aa,p))

#Perim().res()





# 12

class Pp:

    def res(self):

        x1,y1,x2,y2 = map(int,input().split())
        a = max(x1,x2)-min(x1,x2)
        b = max(y1,y2)-min(y1,y2)
        
        c = a*b
        p = 2*(a+b)
        print(abs(c))
        print(abs(p))

#Pp().res()



# 13

class Tri:

    def res(self):

        a,b = input().split()
        c = int(a)*int(b)/2
        print(round(c,2))

#Tri().res()


# 14

class Fa:

    def res(self):

        a = int(input())
        b = (a/5)*9+32
        print('{:.2f}'.format(b))

#Fa().res()


# 15

class Rad:

    def res(self):

        a = float(input())
        c = a*57.295779513
        print(round(c))

#Rad().res()



# 16

class Con:

    def res(self):

        a = float(input())
        b = a*1.79549
        print('{:.2f}'.format(b))

#Con().res()





# 17

class Su:

    def res(self):

        print('Hello, SU')

Su().res()



# 18

class Conv:

    def res(self):

        a = float(input())
        source = input().lower()
        target = input().lower()

        bgn = 1
        usd = 1.79549
        eur = 1.95583
        gbp = 2.53405

        tot = 0


        if source == 'bgn':
            if target == 'usd':
                tot = a/1.79549
            elif target == 'eur':
                tot = a/1.95583
            elif target == 'gbp':
                tot = a/2.53405

        
        elif source == 'usd':
            if target == 'bgn':
                tot = a*1.79549
            elif target == 'eur':
                tot = a*(usd/eur)
            elif target == 'gbp':
                tot = a*(usd/gbp)



        elif source == 'eur':
            if target == 'usd':
                tot = a/usd
            elif target == 'bgn':
                tot = a*eur
            elif target == 'gbp':
                tot = a*(eur/gbp)



        elif source == 'gbp':
            if target == 'usd':
                tot = a/usd
            elif target == 'eur':
                tot = a/eur
            elif target == 'bgn':
                tot = a*bgp
        
        print(round(tot,2))

#Conv().res()



# 19




class Hall:

    def res(self):

        w = float(input())
        h = float(input())

        w1 = w*100
        h1 = h*100
        w2 = w1//120
        h1-=100
        buro = h1//70
        tot = w2*buro - 3
        print(round(tot))

#Hall().res()

        

# 20

class Garden:

    def res(self):

        a = float(input())
        b = float(input())
        c = int(input())
        d = int(input())

        c1 = c*a
        d1 = d*b
        tot = c1+d1
        tot1 = tot/1.94

        print('{:.2f}'.format(tot1))
        


#Garden().res()


# 21


class Som:

    def res(self):

        n = int(input())
        w = float(input())
        l = float(input())
        m = int(input())
        o = int(input())

        n1 = n*n
        o1 = o*m
        tot1 = n1-o1
        w1 = w*l
        tot2 = tot1/w1
        tot3 = tot2*0.2

        print('{:.2f}'.format(tot2))
        print('{:.2f}'.format(tot3))

#Som().res()




# 22


class Bit:

    def res(self):

        a = int(input())
        b = float(input())
        c = float(input())

        a1 = a*1168
        b1 = b*0.15
        b2 = b1*1.76
        tot = a1 + b2
        tot1 = tot/1.95
        tot2 = tot1 - (5/100*tot1)
        print('{:.2f}'.format(tot2))

#Bit().res()



# 23


class Day:

    def res(self):

        a = int(input())
        b = float(input())
        c = float(input())

        a1 = a*b
        print(a1)
        a2 = (a1*12)+(a1*2.5)
        print(a2)
        a3 = a2 - (25/100*a2)
        print(a3)
        a4 = a3*c
        print(a4)
        a5 = a4/365
        print(a5)

#Day().res()






























        
