


# 1

class Bonus:

    def res(self):

        a = int(input())

        b1 = 0

        if a%2==0:
            b1+=1
        elif a%10==5:
            b1+=2

        b = 0

        if a <=100:
            b+=5
        elif a>100 and a<=1000:
            b+=20/100*a
        elif a>1000:
            b+=10/100*a

        bb = b1+b
        tot = bb+a
        print(bb)
        print(tot)

#Bonus().res()



# 2 ---------------------------------------------------------------

class Seconds:

    def res(self):


        a = int(input())
        b = int(input())
        c = int(input())

        sec = a+b+c
        mins = 0

        if sec > 59:
            mins+=1
            sec-=60
        if sec > 59:
            mins+=1
            sec-=60
        if sec < 10:
            print('{}:0{}'.format(mins,sec))
        else:
            print('{}:{}'.format(mins,sec))


#Seconds().res()



# 3

class Met:

    def res(self):

        a = int(input())
        b = input()
        c = input()

        d = 0

        if b == 'm':
            if c == 'mm':
                d = a*1000

        print(d)

#Met().res()



# 4 + 5

class Grade:

    def res(self):

        a = float(input())
        b = float(input())

        if a >=5.50:
            print('nicee')
        else:
            print('fail')

        if b>=5.50:
            print('hi')

#Grade().res()



# 6

class OddEven:

    def res(self):

        a = int(input())

        if a%2 == 0:
            print('even')
        else:
            print('odd')

#OddEven().res()


# 7


class Big:

    def res(self):

        a = int(input())
        b = int(input())

        c = [a,b]

        print(max(c))

#Big().res()



# 8

class NumLetter:

    def res(self):

        a = int(input())

        if a == 5:
            print('five')

#NumLetter().res()




# 9


class Pass:

    def res(self):

        a = input()

        if a =='s3cr3t!P@ssw0rd':
            print('Hi')
        else:
            print('wrong')

#Pass().res()


# 10

class Check:

    def res(self):

        a = int(input())

        if a <100:
            print('less than 100')
        elif a >=100 and a<=200:
            print('between 100 and 200')
        else:
            print('bigger than 200')

#Check().res()


# 11

class W:

    def res(self):

        a = input().lower()
        b = input().lower()

        if a == b:
            print('yes')
        else:
            print('no')

#W().res()



# 12

class Speed:

    def res(self):

        a = float(input())

        if a <=10:
            print('slow')
        elif a>10 and a<50:
            print('average')
        elif a>=50 and a<150:
            print('fast')
        else:
            print('super fast')

#Speed().res()


# 13

class Fig:

    def res(self):

        print('a: quadrat')
        a = 5
        print('{}*{} = {}'.format(a,a,a*a))

Fig().res()




# 14 --------------------------------------------------------------


class Time:

    def res(self):

        a = int(input())
        b = int(input())
        mins = a*60+b
        mins+=15
        hours = mins//60
        mins = mins%60

        if hours > 23:
            hours-=24

        if mins < 10:
            print('{}:0{}'.format(hours,mins))
        else:
            print('{}:{}'.format(hours,mins))


#Time().res()




# 15 ----------------- as # 2

class Time:

    def res(self):

        a = int(input())
        b = int(input())
        c = int(input())

        summ = a+b+c
        minutes = summ//60
        seconds = summ % 60

        if seconds < 10:
            print('{}:0{}'.format(minutes,seconds))
        else:
            print('{}:{}'.format(minutes,seconds))


#Time().res()
        



# 16


class E:

    def res(self):

        a = int(input())
        b = int(input())
        c = int(input())

        if a==b and b == c:
            print('yes')
        else:
            print('no')

#E().res()


# 17  --------------------------------------------


class Hundred:

    def res(self):

        a = int(input())

        b = ['zero','one','two','three','four','five','six',\
                'seven','eight','nine','ten','eleven','twelve',\
                'thirteen','fourteen','fifteen','sixteen',\
                'seventeen','eighteen','nineteen']

        c = ['twenty','thirty','fourty','fifty','sixty',\
                'seventy','eighty','ninety']

        if a<0 or a>100:
            print('not valid')
        
        if a == 100:
            print('one hundred')

        elif a>=0 and a<=19:
            print(b[a])
        elif a>=20 and a <100:
            if a%10 == 0:
                print(c[(a//10)-2])
            else:
                print('{} {}'.format(c[(a//10)-2],b[a%10]))

#Hundred().res()


# 18



class Drive:

    def res(self):

        a = int(input())
        b = input()

        taxi_d = 0.70 + (0.79*a)
        taxi_n = 0.70 + (0.90*a)
        bus_dn = 0.09*a
        train_dn = 0.06*a
        tot_d = [taxi_d,bus_dn,train_dn]
        tot_d.sort()

        if b == 'day':
            if a<=20:
                print(tot_d[0])
         
#Drive().res()

















