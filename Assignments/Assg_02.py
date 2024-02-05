#!/usr/bin/python3
"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + r/n)^nt

            A = Accrued amount (principal + interest), payable amount
            P = Principal amount
            r = Annual nominal interest rate as a decimal(R/100)
            n = number of compounding periods per unit of time
            t = time in decimal years; e.g., 6 months is calculated as 0.5 years. Divide your partial year number of months by 12 to get the decimal years.(time duration)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""

# # Method 1 - Hard coding Values
# borrowed_amount = 10_000 # Principal
# rate_of_interest = 8.3 /100   # %
# loan_duration = 10 # years

# Method 2 - Getting values in run-time
borrowed_amount = int(input("Enter Borrowed Amount:"))
rate_of_interest = float(input("Enter Rate of Interest :")) / 100
loan_duration = int(input("Enter loan duration (in years):"))
compound_period=int(input("Enter the comppounding periods per year :"))



# A = P (1 + r/n)^nt
payable_amount  = round(borrowed_amount * (1 + (rate_of_interest / compound_period))**(compound_period * loan_duration))
interest_amount = payable_amount - borrowed_amount

print("Principle          :", borrowed_amount)
print("Rate of Interest   :", rate_of_interest)
print("Loan Duration      :", loan_duration)
print("Interest amount    :", interest_amount)
print("total amount to pay:", payable_amount)

# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php