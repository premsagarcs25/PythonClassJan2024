#!/usr/bin/python3
"""
Purpose: Relational Operations
    - These operations will result in a boolean value (True or False)

     <  lesser
     >  greater
     == equal to
     <= less than or equal to
     >= greater than or equal to
     != not equal to
     <> not equal to  ( in python 2 only)
"""

str1 = "abc"
str2 = "abc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")
print()


str1 = "abc"
str2 = "bc"
print(f"{str1 == str2 =}")
print(f"{str1 >  str2 =}")
print(f"{str1 >= str2 =}")
print(f"{str1 <  str2 =}")
print(f"{str1 <= str2 =}")
print(f"{str1 != str2 =}")

# Assignmne: repeat the same for all the data types

# Integers
num1 = 10
num2 = 5

print(f"{num1 == num2 =}")  # Output: False
print(f"{num1 >  num2 =}")  # Output: True
print(f"{num1 >= num2 =}")  # Output: True
print(f"{num1 <  num2 =}")  # Output: False
print(f"{num1 <= num2 =}")  # Output: False
print(f"{num1 != num2 =}")  # Output: True
print()

# Floats
float1 = 3.14
float2 = 6.28

print(f"{float1 == float2 =}")  # Output: False
print(f"{float1 >  float2 =}")  # Output: False
print(f"{float1 >= float2 =}")  # Output: False
print(f"{float1 <  float2 =}")  # Output: True
print(f"{float1 <= float2 =}")  # Output: True
print(f"{float1 != float2 =}")  # Output: True
print()

# Booleans
bool1 = True
bool2 = False

print(f"{bool1 == bool2 =}")  # Output: False
print(f"{bool1 >  bool2 =}")  # Output: True
print(f"{bool1 >= bool2 =}")  # Output: True
print(f"{bool1 <  bool2 =}")  # Output: False
print(f"{bool1 <= bool2 =}")  # Output: False
print(f"{bool1 != bool2 =}")  # Output: True
