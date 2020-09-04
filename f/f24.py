
a = {'Peter':21, 'George': 18, 'John': 45}
print(a)

sorted_a = dict(sorted(a.items())) # sort in alphabetical
print(sorted_a)


sorted_a = dict(sorted(a.items(), key=lambda x: x[1])) # sort in numberical from small --> big x[1] means we want to sort values
print(sorted_a)

sorted_a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)) # reverse nums big --> small, but can reverse strings as well
print(sorted_a)


sorted_a = dict(sorted(a.items(), key=lambda x: -x[1])) # sorted reversed, when there is nums
print(sorted_a)



b = {'Peter':21, 'George': 45, 'John': 45}
print(b)

sorted_b = dict(sorted(b.items(), key=lambda x: (x[0],x[1]))) # we want to reverse only 2 elements strings
print(sorted_b)

sorted_b = dict(sorted(b.items(), key=lambda x: (-x[1],x[0]), reverse=True)) # we want to reverse only 2 elements strings
print(sorted_b)



# 1

class Bake:

    def res(self):

        data = input()
        data1 = data.split(' ')

        c = {}
        for x in range(0,len(data1),2):
            a = data1[x]
            b = data1[x+1]
            c[a] = int(b)

        print(c)

        c1 = {data1[x]:data1[x+1] for x in range(0,len(data1),2)}
        print(c1)



#Bake().res()
        


# 2


class Search:

    def res(self):

        d = input().split()

        c = {d[x]:int(d[x+1]) for x in range(0,len(d),2)}
        print(c)

        d1 = list(input().split())
        print(d1)

        for x in d1:
            if x in c:
                print('we have {} of {} left'.format(c[x],x))
            else:
                print('sorry we dont have {}'.format(x))



#Search().res()




# 3


from collections import defaultdict

class Stat:

    def res(self):

        d = defaultdict(int)
        while True:
            command = input()
            if command == 'statistics':
                break 

            a,b = command.split(': ')
            d[a] += int(b)

        print('Products in stock: ')
        for x,y in d.items():
            print('- {}: {}'.format(x,y))
        
        print('Total products: {}'.format(len(d.keys())))
        print('total quantity: {}'.format(sum(d.values())))

# without defaultdics module
# --> in while loop:  if a in d: d[a]+=int(b) else: d[a] = int(b) --> above d = {}



#Stat().res()





# 4



class Txt:

    def res(self):

        t = input()

        d = {}

        for x in t:
            if x == ' ':
                continue
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        

        print(d)
        for x,y in d.items():
            print('{} --> {}'.format(x,y))


#Txt().res()




# 5


class Mine:

    def res(self):

        d = defaultdict(int)

        while True:
            command = input()
            if command == 'stop':
                break
            a = int(input())
            #if command not in d:
                #d[command] = 0  # no need to use since we use defaultdict(int)
            d[command] += a



        print(d.items())

        for x,y in d.items():
            print('{} --> {}'.format(x,y))

#Mine().res()





# 6


class Parking:

    def res(self):

        n = int(input())

        parking = {}

        for x in range(n):
            args = input().split()
            command = args[0]
            username = args[1]

            if command == 'register':
                lpn = args[2]

                if username in parking:
                    print('ERROR: car already registered: {}'.format(parking[username]))
                    continue

                parking[username]=lpn
                print('{} registered {} nice'.format(username,lpn))

            elif command == 'unregister':

                if username not in parking:
                    print('ERROR: {} is not in the park'.format(username))


                parking.pop(username)
                print('{} uregistered'.format(username))

        for x,y in parking.items():
            print('{} --> {}'.format(x,y))

Parking().res()



















