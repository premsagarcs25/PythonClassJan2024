#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

balance =0
min_balance=1500
salary_credited=3300
online_purchase=33.33
paid_house_rent=1500
balance = min_balance+salary_credited-online_purchase-paid_house_rent
print("Balance :",balance) #balance = 3266.67