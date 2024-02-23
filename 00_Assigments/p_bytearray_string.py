#!/usr/bin/python3
"""
Purpose: bytearray strings
"""

# Assignment
# -------------
# caesar cipher
# ------------------  + 3
# A B C D E F G H I J     Y Z
# 0 1 2 3 4 5 6 7
# D E F

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
shift = 3
encrypted_text = ""
for char in text:
    if char.isalpha():  # Check if the character is alphabetic
        if char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # 
        else:
            #chr((65-65+3)%26+65))
            #chr(68)
            #out 'D'
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) 
    else:
        encrypted_text += char

print("Plaintext:", text)
print("Ciphertext:", encrypted_text)
