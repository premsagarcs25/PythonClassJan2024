#!/usr/bin/python3

#try exception block
print(1 * 0)

try:
    print(1 / 0)
except Exception as exe:
    print("Got Exception", exe)
finally:
    print("Zero ")

#print function
def wishes(name):
    wish = "How are you {0}?".format(name)
    print(wish)

wishes("PremSagar")

#dynamic typing 

num=2304.22
print("num is ", type(num), "datatype")