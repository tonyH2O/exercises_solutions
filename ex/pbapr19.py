



# 4


class Kino:

    def res(self):


        a = int(input())

        c = 0
        cc = []
        cc2 = []

        while a > 0:
            command = input()
            if command == 'End':
                break

            if (len(command) > 8) and ((ord(command[0])+ord(command[1])) < a):
                c= ord(command[0])+ord(command[1])
                cc.append(command)
                    

            elif (len(command) <=8) and (ord(command[0]) <a):
                c=ord(command[0])
                cc2.append(command)

            
            a-=c
            

        print(len(cc))
        print(len(cc2))

#Kino().res()




# 5

from collections import defaultdict

class Movie:

    def res(self):

        a = int(input())

        d = defaultdict(int)

        for _ in range(a):
            b = input()
            c = float(input())
            d[b]+=c


        print(d)
        dh = dict(sorted(d.items(), key=lambda x: x[1]))
        print(dh)
        k = list(dh.keys())
        v = list(dh.values())
        vv = sum(dh.values())
        vvv = vv/a
        print('{} is with HIGHEST rating: {:.1f}'.format(k[-1],v[-1]))
        print('{} is with LOWEST rating: {:.1f}'.format(k[0],v[0]))
        print('Average rating: {:.1f}'.format(vvv))



#Movie().res()



# 6




class Ticket:

    def res(self):

        film = input()
        total_standard = 0
        total_students = 0
        total_kids = 0
  
        while film != "Finish":
            free_space = int(input())
            filled_space = 0
            while filled_space < free_space:
                ticket = input()                
                if ticket == "standard":
                    filled_space += 1
                    total_standard += 1
                elif ticket == "student":
                    filled_space += 1
                    total_students += 1
                elif ticket == "kid":  
                    filled_space += 1
                    total_kids += 1
                elif ticket == "End":
                    break
            percent_full = filled_space * 100 / free_space
            print(f"{film} - {percent_full:.2f}% full.")
            film = input()
        total_tickets = total_students + total_standard + total_kids
        percent_students = total_students * 100 / total_tickets
        percent_standard = total_standard * 100 / total_tickets
        percent_kids = total_kids * 100 / total_tickets
        print(f"Total tickets: {total_tickets}")
        print(f"{percent_students:.2f}% student tickets.")
        print(f"{percent_standard:.2f}% standard tickets.")
        print(f"{percent_kids:.2f}% kids tickets.")




Ticket().res()

















