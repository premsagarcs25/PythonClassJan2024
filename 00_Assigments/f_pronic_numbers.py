#!/usr/bin/python3
"""
Purpose: Display the pronic numbers.

 Pronic number is a number which is the product
 of two consecutive integers.
 Some pronic numbers: 2*3 = 6

3  - 1 * 3
4  - 2 * 2
5  - 1 * 5
6  - 2 * 3  PRONIC
10 - 2 * 5

break
    - keyword
    - to stop the loop

NOTE:
else block of for loop will be executed, when all
iterations of for loop are completed
"""

print("Pronic numbers:")
for num in range(2, 100):  # upto 100
    for i in range(1, num):
        if i * (i + 1) == num:
            print(f"{num} - {i} * {i+1}")
            break
    else:
        continue  # Skip if pronic number not found
