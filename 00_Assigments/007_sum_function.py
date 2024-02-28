#!/usr/bin/python3
"""
Assignment
----------
1) write a function to mimick the sum() function.
    Caution: don't create function with same name

2) write a function to implement the following:
    - input: ((1,2), 3,4, [5, 6])
    - output: (1, 2, 3, 4, 5, 6)

    HINT: isinstance() - builtin function
          int(), float(), list(), tuple(), set()
          list.append(), list.extend
          list & tuple concatenation
"""
#1) write a function to mimick the sum() function.
def final_sum_value(itr, start=0):
    total = start
    for item in itr:
        total += item
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = final_sum_value(numbers)
print(result)  # Output: 15

'''2) write a function to implement the following:
    - input: ((1,2), 3,4, [5, 6])
    - output: (1, 2, 3, 4, 5, 6)'''
def final_output(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, (list, tuple)): #check whether it consist of list/tuples
            flattened.extend(item)
        else:
            flattened.append(item)
    return tuple(flattened)

# Example usage:
nested_input = ((1, 2), 3, 4, [5, 6])
output = final_output(nested_input)
print(output)  # Output: (1, 2, 3, 4, 5, 6)
