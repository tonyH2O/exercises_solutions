


'''
#1

in:
    21
    5.50
    4.40
    6.20

out:
    254.10


'''
import math

class Pool:

    def res(self):

        a = int(input('ppl count: '))
        b = float(input('fee: '))
        c = float(input('fee per 1 bed: '))
        d = float(input('fee per 1 ambrella: '))

        fee = a*b
        percent1 = math.ceil(0.75*a)
        bed = c*percent1
        percent2 = math.ceil(0.50*a)
        ambrella = d*percent2
        
        total = fee + bed + ambrella

        print('{:.2f}.'.format(total))

#Pool().res()





'''
#2

in:
    10
    11
    4
    8

out:
    727.09

'''

class Paint:

    def res(self):
        a = int(input('q: '))
        b = int(input('paint: '))
        c = int(input('n: '))
        d = int(input('h: '))

        q = (a+2)*1.50
        q1 = (b+1.10)*14.50
        q2 = c*5

        r = q+q1+q2 + 0.40
        r2 = ((0.30*r)*d + r)

        print('total: {:.2f}'.format(r2))

#Paint().res()




# 3


class Fam:

    def res(self):
        
        a = float(input())
        b = int(input())
        c = float(input())
        d = int(input())

        if b > 7:
            c = c - (0.05*c)

        r = c*b
        r2 = d/100*a
        r3 = r+r2

        if r3 <= a:
            print('the money is enough, the leftover is : {:.2f}'.format(abs(r3-a)))
        else:
            print('not enough money, {:.2f} more needed'.format(abs(r3-a)))


#Fam().res()





# 4




class Shop:

    def res(self):
    
        a = float(input())
        b = int(input())
        c = int(input())
        d = int(input())

        vid = b*250
        proc = ((35/100) * vid)*c
        ram = (10/100*vid)*d
        
        tot = vid+proc+ram
        if b > c:
            tot = tot - (15/100*tot)

        if tot <= a:
            print('it enough... {:.2f} left'.format(abs(tot-a)))
        else:
            print('not enough... {:.2f} more needed'.format(abs(tot-a)))

#Shop().res()





# 5



class Coff:

    def res(self):

        e = [0.90,1,1.20]
        k = [1,1.20,1.60]
        t = [0.50,0.60,0.70]

        a = input().lower()
        b = input().lower()
        c = int(input())

        tot = 0

        if a == 'espresso':
            if b == 'without':
                tot = (e[0]*c) - (35/100*(e[0]*c))
            elif b == 'normal':
                tot = e[1]*c
            else:
                tot = e[2]*c


        elif a == 'cappuccino':
            if b == 'without':
                tot = (k[0]*c) - (35/100*(k[0]*c))
            elif b == 'normal':
                tot = k[1]*c
            else:
                tot = k[2]*c

        elif a == 'tea':
            if b == 'without':
                tot = (t[0]*c) - (35/100*(t[0]*c))
            elif b == 'normal':
                tot = t[1]*c
            else:
                tot = t[2]*c

        if a == 'espresso' and c>=5:
            tot = tot - (25/100*tot)

        if tot >15:
            tot = tot - (20/100*tot)

        print('you got {} cups of {} for {:.2f}'.format(c,a,tot))


#Coff().res()






# 6

import sys

class Tour:

    def res(self):

        a1 = ['Bansko','Borovets']
        a2 = ['Varna','Burgas']
        b1 = ['noEquipment','withEquipment']
        b2 = ['noBreakfast','withBreakfast']

        c = input()
        p = input()
        v = input()
        d = int(input())
        tot = 0

        if c in a1 and p in b1:
            if v == 'yes':
                if p == b1[0]:
                    tot = d*80 - (5/100*d*80)
                elif p == b1[1]:
                    tot = d*100 - (10/100*d*100)
            elif v == 'no':
                if p == b1[0]:
                    tot = d*80
                elif p == b1[1]:
                    tot = d*100
        
        elif c in a2 and p in b2:
            if v == 'yes':
                if p == b2[0]:
                    tot = d*100 - (7/100*d*100)
                elif p == b2[1]:
                    tot = d*130 - (12/100*d*130)
            elif v == 'no':
                if p == b2[0]:
                    tot = d*100
                elif p == b2[1]:
                    tot = d*130

        else:
            print('Invalid Input')
            sys.exit()
            
    
        if d > 7:
            tot = tot - (tot/d)
        
        if d<1:
            print('day must be more than or 1')
        else:
            print('price: {:.2f}, have a nice day!'.format(tot))




#Tour().res()            




# 7



class Club:

    def res(self):
        
        a = float(input())
        tot = 0
        tot1 = 0
    
        command = ''
        
        while tot < a:
            command = input()
            if command == 'Party!':
                break
            cc = int(input())

            tot1 = cc*len(command)
        
            if tot1%2 != 0:
                tot1 -= 25/100*tot1
            else:
                pass

            tot+=tot1
                
        
        
            
        if tot <a:
            print('we need: {:.2f} more'.format(abs(a-tot)))
        else:
            print('target set!')

        print('income: {:.2f}'.format(tot))


#Club().res()





# 8


class House:

    def res(self):

        h = int(input())
        w = int(input())
        p = int(input())

        r = 4*(w*h)
        r2 = r - (p/100*r)

        while r2 > 0:
            command = input()
            if command == 'Tired!':
                print('{:.0f} left to do'.format(r2))
                break
            cc = int(command)
            r2 = r2 - cc


        if r2 < 0:
            print('all done, you have {:.0f} leftover'.format(abs(r2)))
        elif r2 == 0:
            print('nothing left, all done')



#House().res()




# 9



class Games:

    def res(self):

        a = int(input())
        c = ['Hearthstone','Fornite','Overwatch']

        h = 0
        f = 0
        ow = 0
        o = 0


        for _ in range(a):
            b = input()
            if b in c[0]:
                h+= 100/a
            elif b in c[1]:
                f+=100/a
            elif b in c[2]:
                ow+=100/a
            else:
                o+=100/a

        print('HS - {:.2f}%'.format(h))
        print('F - {:.2f}%'.format(f))
        print('OW - {:.2f}%'.format(ow))
        print('Other games - {:.2f}%'.format(o))

#Games().res()




# 10



class Football:

    def res(self):

        a = input()
        b = int(input())
        if b == 0:
            print('team {} has not played so far'.format(a))
            sys.exit()
        
        cc = []
        w = 0
        d = 0
        l = 0

        for _ in range(b):
            c = input()
            cc.append(c)
            if c == 'W':
                w+=3
            elif c == 'D':
                d+=1
            elif c == 'L':
                l+=0

        total = w+d+l
        per = cc.count('W')/b*100
        print('{} has won {} points.\nTotal stats:\n## W: {}\n## D: {}\n## L: {}\nWin Rate: {:.2f}%'\
                .format(a,total,cc.count('W'),cc.count('D'),cc.count('L'),per))

#Football().res()



# 11



class Name:

    def res(self):

        r = 0
        r1 = []
        r2 = []
    
        while True:
            command = input()
            r2.append(command)
            if command == 'Stop':
                break

            for x in range(len(command)):
                cc = int(input())
                if cc == ord(command[x]):
                    r+=10
                else:
                    r+=2
            r1.append(r) # thanks to putting it here and not inside the FOR, we can append pl1 as index 0, pl2 as index 1
            #r1.append('-')
        
    
        #for x in r1:  # for testing because pl1 always is index 0 , pl2 is index 1 - index 0
            #print(r1[::r1.index('-')]) we might not need the '-'
        
        pl1 = r1[0]
        pl2 = r1[1] - r1[0]
        print(pl1)
        print(pl2)

        if pl1 > pl2:
            print('winner {}: {} points'.format(r2[0],pl1))
        elif pl1 == pl2:
            print('winner {}: {} points, when equal points --> winner is 2nd best'.format(r2[1],pl2))
        else:
            print('winner {}: {} points'.format(r2[1],pl2))

        

#Name().res()


# 12



class Words:

    def res(self):

        a = ['a','e','i','o','u','y']
        a = [x.upper() for x in a]
        b = [ord(x) for x in a]
        r = 0
        r1 = [] # the sums, then cleared and then sums again
        r2 = [] # the final r, sorted so we can find the largest
        r3 = [] # counts the str commands
        r4 = dict() # this way we know the key is command --> r is value

        print(a)
        print(b)

        while True:
            command = input()
            r3.append(command)
            if command == 'End of words':
                break
            
            for x in command:
                r1.append(ord(x))
            cc = sum(r1)
            #print(r1)
            #print(cc)
            #print(command[0])    
            if (command[0] in a) or (command[0] in b):
                r = cc*len(command)
            else:
                r = round(cc/len(command))

            r1.clear()
            #print(r1)
            #print(r)

            r2.append(r)
            r4[command] = r

        r2.sort()
        r3.pop()
        #print(r2)
        tot = r2[-1]
        #print(tot)
        #print(r3[-1])
        #print(r4)
        tot2 = [x for x,y in r4.items() if y == tot]
        tot2 = ' '.join(tot2)

        print('most powerfull word is: {} --> {}'.format(tot2,tot))



Words().res()




















        







              




