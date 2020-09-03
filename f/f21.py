


#You are given a positive integer number and one binary digit B (0 or 1). Your task is to write a program that finds the
#number of binary digits (B) in a number.



class Bin:

    def res(self):

        a = int(input('n: '))
        b = int(input('nn: '))

        c = bin(a)[2::]
        cc = []

        for x in c:
            cc.append(x)
        xx = 0
        print(cc)
        for x in cc:
            if int(x) == b:
                xx+=1
 
        print('{} --> {}'.format(a,c))
        print('{} is found {} times in {}'.format(b,xx,c))

b = Bin()
#b.res()


#Write a program that prints the bit at position 1 of a number.
#Find the value of the bit at position 1 (position 1 is the second bit from right to left:




class Pos:

    def res(self):

        a = int(input('n: '))
        b = bin(a)[2::].split()
        for x in b:
            print(x[-2])

#Pos().res()
        





#Write a program that prints the bit at position p of a number.


class Pos:

    def res(self):
        
        a = int(input('n: '))
        c = int(input('pos: '))
        
        b = bin(a)[2::].split()

        for x in b:
            print(x[c])

#Pos().res()




































