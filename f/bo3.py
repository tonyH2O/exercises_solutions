



# 1 ---------------------------------- on time for exam

class OnTime:

    def res(self):

        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())

        late = 'late'
        on_time = 'on time'
        early = 'early'

        time1 = (a*60)+b
        time2 = (c*60)+d

        tot = time2 - time1

        s = late

        if tot < -30:
            s = early
        elif tot <=0:
            s = on_time

        res = ''

        if tot !=0:
            hh = abs(tot)//60
            mm = abs(tot)%60
            if hh>0:
                res = '{}:{}:02 hours'.format(hh,mm)
            else:
                res = '{} minutes'.format(mm)

            if tot <0:
                res+=' before the start'
            else:
                res+=' after the start'

        print(s)
        if res:
            print(res)

#OnTime().res()


# 2 ---------------------

class E:

    def res(self):

        a = int(input())
        b = []

        for x in range(a):
            a = int(input())
            b.append(a)
        
        b.sort()
        cc = b.pop()
        c = sum(b)
        if c == cc:
            print('yes\nSum = {}'.format(c))
        else:
            print('no\nDiff = {}',format(cc-c))

#E().res()



# 3  ------------ start from position 1


class E:

    def res(self):

        a = int(input())
        b = []

        for x in range(1,a+1):
            a = int(input())
            b.append(a)
        b1 = []
        b2 = []
        print(b)
        
        for x,y in enumerate(b):
            print('{} - {}'.format(x,y))

        for x in range(1,len(b),2):
            b1.append(b[x]) #even index
        for x in range(0,len(b),2):
            b2.append(b[x]) #odd index
        print(b1)
        print(b2)
        
        oddmi = min(b2)
        oddma = max(b2)
        odds = sum(b2)

        emi = min(b1)
        ema = max(b1)
        es = sum(b1)

        print(oddmi)
        print(oddma)
        print(odds)
        print(emi)
        print(ema)
        print(es)





#E().res()


# 4 ------------------------------------- 2*n nums


from collections import defaultdict

class Nums:

    def res(self):

        a = int(input())

        c = defaultdict(int)
        cc = 0
        cc1 = 0

        for x in range(a):
            a = int(input())
            b = int(input())
            c[cc]+=a+b
            cc+=1
            cc1 = a+b

        print(c)
        sorted_c = dict(sorted(c.items(),key=lambda x: x[1]))
        print(sorted_c)

        c2 = all(x==cc1 for x in c.values())
        c3 = abs(list(c.values())[0] - list(c.values())[-1])
        print(c3)

        if c2 == True:
            print('Yes,sum = {}'.format(cc1))
        else:
            print('No,diff = {}'.format(c3))


#Nums().res()



# 5


class Histogram:

    def res(self):


        a = int(input())
        b = []

        for _ in range(a):
            aa = int(input())
            b.append(aa)

        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0


        for x in b:
            if x <200:
                p1 +=1
            elif x>=200 and x<=399:
                p2+=1
            elif x>=400 and x<=599:
                p3+=1
            elif x>=600 and x<=799:
                p4+=1
            else:
                p5+=1
        
        p11 = p1/a * 100
        p22 = p2/a*100
        p33 = p3/a*100
        p44 = p4/a*100
        p55 = p5/a*100

        print('{}%'.format(p11))


#Histogram().res()



# 6




class Histogram:

    def res(self):


        a = int(input())
        b = []

        for _ in range(a):
            aa = int(input())
            b.append(aa)

        p1 = 0
        p2 = 0
        p3 = 0



        for x in b:
            if x%2 == 0:
                p1 +=1
            if x%3 == 0:
                p2+=1
            if x%4 == 0:
                p3+=1

        
        p11 = p1/a * 100
        p22 = p2/a*100
        p33 = p3/a*100


        print('{}%'.format(p11))
        print(p22)
        print(p33)


#Histogram().res()





































