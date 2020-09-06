




# 1

from collections import defaultdict
class Strr:

    def res(self):

        d = {}
        while True:
            a = input()
            if a == 'end':
                break

            b = a[::-1]
            if b in d:
                d[a]+=b
            else:
                d[a]=b
            
        
        print(d)
        for x,y in d.items():
            print('{} == {}'.format(x,y))



#Strr().res()



# 2

class Repeat:

    def res(self):

        a = input().split()
        aa = []
        for x in a:
            x = len(x)*x
            aa.append(x)

        print(aa)
        aaa = ''.join(aa)
        print(aaa)
        


        #this is testing:
        #b = len(a)*a
        #for x in a:
            #x = len(a)*x
            #print(x) 
        #print(b)
        #end testing

#Repeat().res()

'''
a = input().split()
print(''.join(map(lambda x: x*len(x), a)))

'''


# 3


class Substr:

    def res(self):

        a = input()
        b = input()

        while a in b:
            b = b.replace(a,'')

        print(b)

#Substr().res()



# 4

class Ban:

    def res(self):

        ban = input().split(', ')
        a = input()

        for x in ban:
            a = a.replace(x, '*'*len(x))


        print(a)

#Ban().res()




# 5

class Check:

    def res(self):

        a = input()

        digits = ''
        for x in a:
            if x.isdigit():
                digits+=x
        print(digits)

        letters = ''
        for x in a:
            if x.isalpha():
                letters+=x
        print(letters)

        other = ''
        for x in a:
            if not x.isdigit() and not x.isalpha():
                other+=x
        print(other)


#Check().res()




# 6


class Valid:

    def res(self):

        a = input().split(', ')

        valid = []

        for x in a:
            if (len(x) >=3 and len(x)<=16) and x.isalnum() or ('-' in x):
                valid.append(x)

        print(valid)
        print('\n'.join(x for x in valid))

#Valid().res()




# 7


class Lenn:

    def res(self):

        a = input().split()
        a1 = a[0]
        a2 = a[1]

        min_len = min(len(a1), len(a2))
        tot = 0

        for x in range(min_len):
            res = ord(a1[x])*ord(a2[x])
            tot+=res
            #print(res)

        if_a1_bigger = a1

        if len(a2) > len(a1):
            if_a1_bigger = a2

        for x in range(min_len,len(if_a1_bigger)):
            tot+=ord(if_a1_bigger[x])
        
        print(tot)



#Lenn().res()


# 8


class Split:

    def res(self):

        a = input().split('\\')
        b = []
        bb = ''
        for x in a:
            b.append(x)
        print(b)
        x = b[-1]
        bb+=x
        print(bb)
        for y in bb:
            if y=='.':
                bb=bb[0:bb.index(y)]
        print(bb)

        print('File name: {}'.format(bb))

        


#Split().res()




# 9 Ceaser


class Ceaser:

    def res(self):

        a = input()
        aa = ''
        for x in a:
            b = chr(ord(x)+3)
            aa+=b

        print(aa)

#Ceaser().res()





# 10


class Emo:

    def res(self):

        a = input()

        for x in range(len(a)-1):
            if a[x] == ':':
                print(':{}'.format(a[x+1]))


#Emo().res()



# 11



class Rep:

    def res(self):

        a = input()
        
        for x in range(len(a)):
            b = a[x]
            if  x+1 == len(a) or  b != a[x+1]:
                print(b,end='')
        print('\n')

'''
        for x in a:
            b.append(x)

        c = set(b)
        b.clear()
        for x in c:
            b.append(x)
        cc = ''.join(x for x in b)
        print(cc)
'''
        

#Rep().res()





# 12


class Sol:

    def res(self):

        line = input()
        tot = 0
        x = 0

        while x < len(line):
            a = line[x]

            if a == '>':
                s = int(line[x+1])
                tot+=s
            else:
                if tot > 0:
                    line = line[:x]+line[x+1:]
                    x-=1
                    tot-=1
            x+=1

        print(line)




#Sol().res()























