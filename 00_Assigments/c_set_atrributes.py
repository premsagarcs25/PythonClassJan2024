#!/usr/bin/python3
# Assignment
#  1. Try adding a string to both set.add & set.update &
#  observe the difference
#  'tomoto'


my_set1 = set()
my_set2 = set()

my_set1.add('tomato')
my_set2.update('tomato')# it store's the string in a single char's in ASC order and not allowing any duplicates

print("Using set.add():", my_set1)
print("Using set.update():", my_set2) # otuput: {'o','a','t','m'}

