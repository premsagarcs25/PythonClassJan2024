#!/usr/bin/python3

"""
Assignment
----------
1) implement the stack mechanism - LIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - stack size

-       -
|       |
|       |
---------
HINT: list.pop(), list.append(), len()
"""
#implement the stack mechanism - LIFO
stack = []

while True:
    option = input("Enter 'push' to add an element,\n 'pop' to delete the last element,\n or 'status' to check stack size: ").strip().lower()

    if option == 'push':
        print("Enter the values to push onto the stact && press 'q' to quit the append")
        while option =='push':
            value = input("Enter the values to push onto the stack: ")
            if(value=='q'):
                break
            elif value.isdigit():
                stack.append(value)
        print(f"Appended Stack : {stack}")
            

    elif option == 'pop':
        if stack:
            value = stack.pop()
            print(f"Popped value: {value} && Stack: {stack}")
        else:
            print("Stack is empty.")
    elif option == 'status':
        print(f"Stack size: {len(stack)}")
    else:
        print("!-------Invalid option. Please try again.-------!")

    if not input("Do you want to continue (y/n)? ").strip().lower().startswith('y'):
        break




"""
2) implement the queue mechanism - FIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - queue size
    --------
 ->         ->
    --------
HINT: list.insert(), list.pop(), len()
"""