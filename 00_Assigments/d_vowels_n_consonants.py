#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithms:
-------
step1 : take input in runtime
            clean -- strip()
Step2:  len(character) should not be greater than 1
step3: isalpha()
step4 : is it vowel or not

NOTE: logic should accomodate both upper and lower characters
"""

u_input = input("Enter a character: ").strip()

if len(u_input) > 1:
    print("Please enter only a single character.")
else:
    if not u_input.isalpha():
        print("Please enter an alphabet character.")
    else:
        if u_input.lower() in ('a', 'e', 'i', 'o', 'u'):
            print(f"The character '{u_input}' is a vowel.")
        else:
            print(f"The character '{u_input}' is not a vowel.")
