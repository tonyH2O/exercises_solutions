


# Bonus system

# in:
# 5
# 25
# 30
# 12
# 19
# 24
# 16
# 20

# out: Max Bonus - 34 // The student goes to: 24



class Bonus:

    def res(self):

        a = int(input('students count: '))
        b = int(input('lectures count: '))
        c = int(input('bonus: '))
        d = [int(input('where the student goes: ')) for _ in range(a)]
        print(d)
        d.sort()
        print(d)
        total_bonus = d[-1]/b*(5+c)
        print(round(total_bonus))

        print('MaX Bonus: {}'.format(round(total_bonus)))
        print('The student attended: {} lectures'.format(d[-1]))




#Bonus().res()






# Collecting Itams

# in: iron, sword

# drop - bronze
# combine items - sword:bow
# renew - iron
#

# out: sword, bow, iron


class Col:

    def res(self):

        j = list(input('journal items: ').split(', '))
        while True:
            command = input('command: ')
            if command == 'Craft!':
                break

            a,b = command.split(' - ')
            
            if a == 'Collect':
                if b in j:
                    pass
                else:
                    j.append(b)

            elif a == 'Drop':
                if b in j:
                    j.remove(b)

            elif a == 'Combine Items':
                b1 = ''
                b2 = ''
                for x,y in enumerate(b):  # c = b.split(':') --> c1 = c[0], c2 = c[1]
                    if y == ':':   
                        b1 = b[:x]
                        b2 = b[x+1::]
                if b1 in j:
                    j.insert(j.index(b1)+1,b2)
                else:
                    pass

            elif a == 'Renew':
                if b in j:
                    j.append(j.pop(j.index(b)))
                else:
                    pass

        print(', '.join(x for x in j))


#Col().res()

























