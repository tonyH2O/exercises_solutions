'''

Problem:


The head of the company notes that more and more employees are spending time on web sites.
To prevent this, he will cut money from their checks.
According to the site, different fines are imposed:
  Facebook  -  $ 150
  Instagram - $ 100
 Reddit  -  $ 50

Two lines are read from the console:
 Number of tabs opened in browser n - integer in the interval [1 ... 10]
 Salary - number in the interval [700 ... 1500]
Then n - the number of times the website name - text is read

If during the check the salary becomes less than or equal to 0 USD, the console will display
'You have lost your salary.' and the program ends.
Otherwise after checking the
the payroll balance (to be entered as an integer) is displayed on the console.

Example Input:

10
750
Facebook
imdb
Instagram
Facebook
Reddit
Facebook
Facebook

Output:

You have lost
your salary.

Solution:

'''

n = int(input('browser tabs: '))
s = int(input('salary: '))

for x in range(n):
    tabs = input('tabs: ').lower()

    if tabs == 'facebook':
        s -= 150
    elif tabs == 'instagram':
        s -= 100
    elif tabs == 'reddit':
        s -= 50
    if s <= 0:
        break

if s <= 0:
    print('You have lost your salary.')
else:
    print('%.0f' % s)
