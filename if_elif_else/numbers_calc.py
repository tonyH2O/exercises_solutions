# -*- coding: utf-8 -*-
"""
Problem:
    
Write a program that reads two integers (n1 and n2) and an operator to perform a mathematical operation on them.
Possible operations are: addition (+), subtraction (-), multiplication (*), division (/) and modular division (%).
When collecting, subtracting and multiplying the console, the result should be printed and whether it is even or odd.
In ordinary division, only the result, and in modular division, the remainder. It must be borne in mind that the divisor can be equal to zero (= 0)
and not divisible by zero.
In this case, a special message must be printed.

Print one line on the console:

If the operation is addition, subtraction or multiplication:
"{N1} {operator} {N2} = {result} - {even / odd}".
If the operation is a division:
"{N1} / {N2} = {result}" - The result is formatted to the second character after the decimal point.
If the operation is modular division:
"{N1}% {N2} = {balance}".
In the case of division by 0 (zero):
"Cannot divide {N1} by zero".


Example Input: 123   Output:
               12           123 / 12 = 10.25
               /


Solution:

"""


n1 = int(input('n1: '))
n2 = int(input('n2: '))
op = input('operator: ')

n = 0
output = ' '



if n2 == 0 and op == '/':
        print('Cannot divide {} by zero'.format(n1))


elif op == '+':
    n = n1 + n2
    output = f'{n1} {op} {n2} = {n} ' \
        f'- {("even" if n%2 == 0 else "odd")}'
    print(output)
elif op == '-':
        
    n = n1 - n2
    output = f'{n1} {op} {n2} = {n} ' \
        f'- {("even" if n%2 == 0 else "odd")}'
    print(output)
elif op == '*':
    n = n1 * n2        
    output = f'{n1} {op} {n2} = {n} ' \
        f'- {("even" if n%2 == 0 else "odd")}'
    print(output)
        
elif op == '/' and n2 > 0:
    n = n1 / n2
    print('{} / {} = {:.2f}'.format(n1, n2, n))
    
  
elif op == '%':
    n = n1 % n2
    print('{} % {} = {}'.format(n1, n2, n))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
