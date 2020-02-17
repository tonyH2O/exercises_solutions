# -*- coding: utf-8 -*-
"""
Problem:

    
The hotel offers two types of rooms: studio and apartment.
Write a program that calculates the price for the whole stay for a studio and apartment.
Prices depend on the month of your stay:    
         
May and October        June and September             July and August
Studio - 50  /night      Studio - 75.20                Studio - 76  / night
Apartment - 65 /night     Apartment - 68.70           Apartment - 77  / night    
    
The following discounts are also available:

For studios, for more than 7 nights in May and October: 5% discount.
For studio, for more than 14 nights in May and October: 30% discount.
Studio, more than 14 nights in June and September: 20% discount.
For an apartment for more than 14 nights, regardless of the month: 10% discount.   
    
Print two lines on the console:

First line: "Studio: {full stay price} total".
In the second line: "Apartment: {price for the whole stay} total".
The price for the whole stay is formatted to within two characters after the decimal point.   
    
    
Solution:  
    
 
"""


month = input('month: ').lower()
stay = int(input('number of nights at the hotel: '))

studio_d_7_m_o = 50 - ((5/100) * 50)
studio_d_14_m_o = 50 - ((30/100) * 50)
studio_d_14_j_s = 75.20 - ((20/100) * 75.20)

app_d_14_m_o = 65 - ((10/100) * 65)
app_d_14_j_s = 68.70 - ((10/100) * 68.70)
app_d_14_j_a = 77 - ((10/100) * 77)

studio_total_7_m_o = studio_d_7_m_o * stay 
studio_total_14_m_o = studio_d_14_m_o * stay
studio_total_14_j_s = studio_d_14_j_s * stay
studio_total_j_a = 76 * stay

st_total_less_7_m_o = 50 * stay
st_total_less_7_j_s = 75.20 * stay


app_total_14_m_o = app_d_14_m_o * stay
app_total_14_j_s = app_d_14_j_s * stay
app_total_14_j_a = app_d_14_j_a * stay


app_total_less_14_m_o = 65 * stay
app_total_less_14_j_s = 68.70 * stay
app_total_less_14_j_a = 77 * stay

if (month == 'may' or month == 'october') and (stay >= 8 and stay < 14):
    print('Studio:\n {:.2f} total'.format(studio_total_7_m_o))
    print('Appartment:\n {:.2f} total'.format(app_total_less_14_m_o))
    
elif (month == 'may' or month == 'october') and stay < 8:
    print('Studio:\n {:.2f} total'.format(st_total_less_7_m_o))
    print('Appartment:\n {:.2f} total'.format(app_total_less_14_m_o))
          
elif (month == 'may' or month == 'october') and stay >= 15:
    print('Studio:\n {:.2f} total'.format(studio_total_14_m_o))
    print('Appartment:\n {:.2f} total'.format(app_total_14_m_o))
    
elif (month == 'june' or month == 'september') and stay < 15:
    print('Studio:\n {:.2f} total'.format(st_total_less_7_j_s))
    print('Appartment:\n {:.2f} total'.format(app_total_less_14_j_s))
    
elif (month == 'june' or month == 'september') and stay >= 15:
    print('Studio:\n {:.2f} total'.format(studio_total_14_j_s))
    print('Appartment:\n {:.2f} total'.format(app_total_14_j_s))
    
elif (month == 'july' or month == 'august') and stay < 15:
    print('Studio:\n {:.2f} total'.format(studio_total_j_a))
    print('Appartment:\n {:.2f} total'.format(app_total_less_14_j_a))
    
else:
    print('Studio:\n {:.2f} total'.format(studio_total_j_a))
    print('Appartment:\n {:.2f} total'.format(app_total_14_j_a))

