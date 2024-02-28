#!/usr/bin/python3
# Assignment
# chr(), ord()
print("chr(77) ", chr(77))
print("ord('M')", ord("M"))
# caesar cipher
# a b c d e f ......
# 0 1 2 3 4 5 .......
# +3
# bad -> edg
# ex: attack is planned to happen on next sunday

# HINT : % operation, chr(), ord(), list comprehension

shift = 3
message = "attack is planned to happen on next sunday"

encrypted_message = ''.join([chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                             if char.islower() else
                             chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                             if char.isupper() else
                             char
                             for char in message])

print("Encrypted message:", encrypted_message)


