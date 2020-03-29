# -*- coding: utf-8 -*-
"""
Problem:
    
    
A group of fans decided to buy tickets for the games. Ticket price is determined by two categories:

VIP - 499.99
Normal - 249.99
Fans have a certain budget, and the number of people in the group determines what percentage of the budget should be allocated to transportation:

1 to 4 - 75% of the budget.
From 5 to 9 - 60% of the budget.
10 to 24 - 50% of the budget.
25 to 49 - 40% of the budget.
50 or more - 25% of the budget.
Write a program to calculate whether they can buy tickets for the selected category
with the rest of their budget money, and how much money they will need or need.


Output data
Print one line on the console:

If the budget is sufficient:
"Yes! You have {N} money left." - where N is the remaining money of the group.
If the budget is NOT sufficient:
"Not enough money! You need {M} more." - where M is the sum that does not reach.
Amounts must be formatted to within two characters after the decimal point.

Solution:


"""

budget = float(input('budget: '))
seats = input('vip or normal: ').lower()
group = int(input('number of ppl: '))

vip_ticket = 499.99
normal_ticket = 249.99

transport_1_4 = (75/100) * budget     
transport_5_9 = (60/100) * budget
transport_10_24 = (50/100) * budget 
transport_25_49 = (40/100) * budget   
transport_50_more = (25/100) * budget   

change_1_4 = budget - transport_1_4     
change_5_9 = budget - transport_5_9
change_10_24 = budget - transport_10_24
change_25_49 = budget - transport_25_49  
change_50_more = budget  - transport_50_more

cost_normal = normal_ticket * group
cost_vip = vip_ticket * group

final__n_1_4 = abs(change_1_4 - cost_normal)
final__n_5_9 = abs(change_5_9 - cost_normal)
final__n_10_24 = abs(change_10_24 - cost_normal)
final__n_25_49 = abs(change_25_49 - cost_normal)
final__n_50_more = abs(change_50_more - cost_normal)

final__v_1_4 = abs(change_1_4 - cost_vip)
final__v_5_9 = abs(change_5_9 - cost_vip)
final__v_10_24 = abs(change_10_24 - cost_vip)
final__v_25_49 = abs(change_25_49 - cost_vip)
final__v_50_more = abs(change_50_more - cost_vip)


if seats == 'vip' and cost_vip < change_1_4:
    print('Yes! You have {:.2f} money left.'.format(final__v_1_4))
elif seats == 'vip' and cost_vip > change_1_4:
        print('Not enough money! You need {:.2f} more.'.format(final__v_1_4))
        
elif seats == 'vip' and cost_vip < change_5_9:
    print('Yes! You have {:.2f} money left.'.format(final__v_5_9))
elif seats == 'vip' and cost_vip > change_5_9:
        print('Not enough money! You need {:.2f} more.'.format(final__v_5_9))

elif seats == 'vip' and cost_vip < change_10_24:
    print('Yes! You have {:.2f} money left.'.format(final__v_10_24))
elif seats == 'vip' and cost_vip > change_10_24:
        print('Not enough money! You need {:.2f} more.'.format(final__v_10_24))                            
              
elif seats == 'vip' and cost_vip < change_25_49:
    print('Yes! You have {:.2f} money left.'.format(final__v_25_49))
elif seats == 'vip' and cost_vip > change_25_49:
        print('Not enough money! You need {:.2f} more.'.format(final__v_25_49))
        
elif seats == 'vip' and cost_vip < change_50_more:
    print('Yes! You have {:.2f} money left.'.format(final__v_50_more))
elif seats == 'vip' and cost_vip > change_50_more:
        print('Not enough money! You need {:.2f} more.'.format(final__v_50_more))


elif seats == 'normal' and cost_normal < change_1_4:
    print('Yes! You have {:.2f} money left.'.format(final__n_1_4))
elif seats == 'normal' and cost_normal > change_1_4:
        print('Not enough money! You need {:.2f} more.'.format(final__n_1_4))
        
elif seats == 'normal' and cost_normal < change_5_9:
    print('Yes! You have {:.2f} money left.'.format(final__n_5_9))
elif seats == 'normal' and cost_normal > change_5_9:
        print('Not enough money! You need {:.2f} more.'.format(final__n_5_9))

elif seats == 'normal' and cost_normal < change_10_24:
    print('Yes! You have {:.2f} money left.'.format(final__n_10_24))
elif seats == 'normal' and cost_normal > change_10_24:
        print('Not enough money! You need {:.2f} more.'.format(final__n_10_24))                            
              
elif seats == 'normal' and cost_normal < change_25_49:
    print('Yes! You have {:.2f} money left.'.format(final__n_25_49))
elif seats == 'normal' and cost_normal > change_25_49:
        print('Not enough money! You need {:.2f} more.'.format(final__n_25_49))
        
elif seats == 'normal' and cost_normal < change_50_more:
    print('Yes! You have {:.2f} money left.'.format(final__n_50_more))
elif seats == 'normal' and cost_normal > change_50_more:
        print('Not enough money! You need {:.2f} more.'.format(final__n_50_more)) 




