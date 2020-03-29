'''
Problem: 

You will receive a number n and a word.
On the next n lines you will be given some strings.
You have to add them in a list and print them. 
After that you have to filter out only the strings that include the given word and print that list also
 
Input:

4
tomatoes
I love tomatoes
I can eat tomatoes forever
I don't like apples
Yesterday I ate two tomatoes

Output:

["I love tomatoes", "I can eat tomatoes
forever", "I don't like apples", "Yesterday
I ate two tomatoes"]
['I love tomatoes', 'I can eat tomatoes
forever', 'Yesterday I ate two tomatoes']

Solution:


'''

n = int(input('num: '))
w = input('word: ')

a = []
c = []
key = w

for x in range(n):
    b = input('next word: ')
    a.append(b)
    if key in b:
        c.append(b)

print(a)
print(c)
