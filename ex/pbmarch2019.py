




# 6 High Jump


class Jump:

    def res(self):

        target = int(input())

        curr = target - 30
        fail = 0
        c = 0

        while True:
            c+=1
            a = int(input())
            if fail == 3:
                print('Failed to jump {}m after {} jumps'.format(a,c))
                break

            if a > target:
                print('You did it! Jumped over {}m after {} jumps'.format(target,c))
                break

            if a>curr:
                curr+=5
            elif a<curr:
                fail+=1
    

#Jump().res()



# 5

from collections import defaultdict

class Easter:

    def res(self):

        a = int(input())

        c = defaultdict(int)
        cc = 0

        for _ in range(a):
            b = input()
            c[cc]=b
            cc+=1

        c2 = {}
        for x in c.values():
            c2[x] = 1+ c2.get(x,0)

        for x,y in c2.items():
            print('{} eggs: {}'.format(x,y))
        c3 = dict(sorted(c2.items(),key=lambda x:x[1]))
        c4 = list(c3.values())
        c5 = list(c3.keys())
        print('Max eggs --> {} --> {}'.format(c4[-1],c5[-1]))
        

#Easter().res()












