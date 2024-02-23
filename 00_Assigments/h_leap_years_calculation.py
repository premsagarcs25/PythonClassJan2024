#!/usr/bin/python3
"""
Purpose: Leap Year Checks

Algorithms
-----------
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)

    Compute the leap years in this century
"""



start_year = 2000
end_year = 2099

leap_years = []

for year in range(start_year, end_year,1):
    if year % 4 != 0:
        print(f"{year} is a common year")
    elif year % 100 != 0:
        leap_years.append(year)
    elif year % 400 != 0:
        print(f"{year} is a common year")
    else:
        leap_years.append(year) 

print(f"Leap years :{leap_years}")

