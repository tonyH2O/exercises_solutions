'''
Problem: 

You will be given a number n. On the next n lines you will receive integers. You have to create and print two lists:
 One with all the positives (including 0)
 One with all the negatives
Finally print the following message: 'Count of positives: {count_positives}. Sum of negatives:
{sum_of_negatives}'

Input:

5
10
3
2
-15
-4

Output

[10, 3, 2]
[-15, -4]
Count of positives: 3. Sum of negatives: -19

Solution:

'''

n = int(input('n: '))

positive = []
negative = []
sums = 0

for x in range(n):
    b = int(input(': '))
    if x >= 0 and b >= 0:
        positive += [b]
    else:
        negative += [b]
        sums += b

print(positive)
print(negative)
count = len(positive)
print('Count of positives: {}. Sum of negatives: {}'.format(count, sums))


