#!/usr/bin/python3
"""
Purpose: String slicing operations
"""


# Assignment: reverse each word in given sentence in same order
# input : today is good day
# output: yadot si doog yad

name = "today is good day"
words=name.split()
reverse_string=""
for word in words:
    reverse_word=word[::-1] #reversing the string 
    reverse_string+=reverse_word + ' ' #Append the reversed string's adding spacing 
print("Input String :", name)
print("Reverse String :", reverse_string)