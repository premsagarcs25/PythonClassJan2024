#!/usr/bin/python3
"""
Purpose: Check even-ness of a given number, in runtime.
"""

# Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display, if it is even

# TIP - range, if condition within it, print function

for num in range(45, 138):
    if num % 2 == 0:
        print(f"{num} is Even")
