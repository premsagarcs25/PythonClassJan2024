#!/usr/bin/python3
"""
    Assignment
    ------------------------
    attempts        points
    -----------------------
    1-3             100
    4-9              60
    10-16            20
    17-25             5
    26-               0
"""


attempts = int(input("Enter a Number :"))

# Assign points 
if attempts >= 1 and attempts <= 3:
    points = 100
elif attempts >= 4 and attempts <= 9:
    points = 60
elif attempts >= 10 and attempts <= 16:
    points = 20
elif attempts >= 17 and attempts <= 25:
    points = 5
else:
    points = 0

print(f"For {attempts} attempts, you earn {points} points.")
