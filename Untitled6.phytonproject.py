#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("="*70)
print("        Automated Tech Campus Multi-Tier Billing & Pass Engine ")
print("="*70)
a=input("Enter User Type (Student Or Faculty) :")
if a=="Student" or a=="student":
    b=input("Enter Student Sub Category (ug/pg) :")
    if b=="ug" or b=="UG":
        basefee=500
        c=float(input("Enter Student Cgpa :"))
        if c>=8.5:
            discount="20%"
            after_discount=(basefee*20)/100
            
        elif c>=7.5 and c<=8.49:
            discount="10%"
            
            after_discount=(basefee*10)/100
            
        else:
            discount="0%"
            after_discount=0
             
    elif b=="pg" or b=="PG":
        basefee=500
        c=float(input("Enter Student Cgpa :"))
        if c>=8.5:
            discount="20%"
            after_discount=(basefee*20)/100
            
        elif c>=7.5 and c<=8.49:
            discount="10%"
            
            after_discount=(basefee*10)/100
            
        else:
            discount="0%"
            after_discount=0
            
    else:
        print("error")
        
    d=int(input("Enter vehicle type 2:two wheeler, 4:four wheeler, 3:none :"))
    if d==2:
        type1="two wheeler"
        charge=200
    elif d==4:
        type1="four wheeler"
        extra=150
        charge=600+150
    elif d==3:
        type1="none"
        charge=0
    else:
        print("Wrong vehicle type")
        
    e=float(input("Enter Electricity Consumption in (kwh) :"))
    if e>=0 and e<=100:
        fixed_charge=50
        elecusage=e*3+fixed_charge
    elif e>=101 and e<=300:
        fixed_charge=100
        elecusage=(e-100)*5+100*3+fixed_charge+50
    elif e>=301 and e<=500:
        fixed_charge=150
        elecusage=(e-300)*7.50+100*3+200*5+fixed_charge+50+100
    elif e>500:
        fixed_charge=250
        elecusage=(e-500)*10+100*3+200*5+200*7.50+fixed_charge+50+100+150
     
    total=basefee-after_discount+charge+extra
    TOTAL=total+elecusage    
    
elif a=="faculty" or a=="Faculty":
    f=input("Enter Faculty Type (Resident, Visiting/Guest) :")
    if f=="resident" or f=="Resident":
        basefee=800
        g=float(input("year of service :"))
        if g>10:
            discount="15%"
            after_discount=(800*15)/100
        elif g<=10:
            discount="0%"
            after_discount=0
    elif f=="visiting" or f=="Visiting" or f=="guest" or f=="Guest":
        basefee=1200
        h=float(input("year of service :"))
        if h>10:
            discount="15%"
            after_discount=(1200*15)/100
        elif h<=10:
            discount="0%"
            after_discount=0
            
    else:
        print("error")
            
    d=int(input("enter vehicle type 2:two wheeler, 4:four wheeler, 3:none :"))
    if d==2:
        type1="two wheeler"
        charge=200
    elif d==4:
        type1="four wheeler"
        charge=600
    elif d==3:
        type1="none"
        charge=0
    else:
        print("Wrong vehicle type")
        
    e=float(input("Enter electricity consumption in (kwh) :"))
    if e>=0 and e<=100:
        fixed_charge=50
        elecusage=e*3+fixed_charge
    elif e>=101 and e<=300:
        fixed_charge=100
        elecusage=(e-100)*5+100*3+fixed_charge+50
    elif e>=301 and e<=500:
        fixed_charge=150
        elecusage=(e-300)*7.50+100*3+200*5+fixed_charge+50+100
    elif e>500:
        fixed_charge=250
        elecusage=(e-500)*10+100*3+200*5+200*7.50+fixed_charge+50+100+150
    total=basefee-after_discount+charge
    TOTAL=total+elecusage
else:
    print('error')

    
    
print("-"*70)
print("             CALCULATED INVOICE BREAKDOWN")
print("-"*70)  

print("Base access pass fee :Rs.{}".format(basefee))
print("Discount({}) :-Rs.{}".format(discount,after_discount))
print("Parking fee({}) :Rs.{}".format(type1,charge))
if a=="student" or a=="Student":
    print("Student peak surcharge :Rs.{}".format(extra))
print("Net pass parking total :Rs.{}".format(total))
print("-"*70)
print("Electricity bill ({}kwh) :Rs.{}".format(e,elecusage)) 
print("-"*70)
print("Total Monthly Payable :Rs.{}".format(TOTAL))
print("="*70)        


# In[ ]:




