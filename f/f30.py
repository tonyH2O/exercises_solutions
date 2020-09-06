
import re


a = '''The Wind in Berlin 
The Wind in Berlin'''

b = r'The.*Berlin$'
x = re.search(b,a, re.MULTILINE)
y = re.findall(b,a)
print(x)
print(y)




# 1


class Findd:

    def res(self):

        a = r'\b([A-Z][a-z]+\s[A-Z][a-z]+)\b'
        b = input()

        c = re.findall(a,b)
        print(''.join(c))

#Findd().res()



# 2

class Nums:

    def res(self):

        a = r'(\+359-2-\d{3}-\d{4}|\+359 2 \d{3} \d{4})\b'
        b = input()
        c = re.findall(a,b)
        print(','.join(c))

Nums().res()







