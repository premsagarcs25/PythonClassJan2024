#!/usr/bin/python3
# Assignment - calculate the avergae of numbers provided in runtime
# HINTS - while , input(), eval(), len(), sum()

numbers = []

while True:
    num_str = input("Enter a number (or 'done' to finish): ")
    if num_str.lower() == "done":
        break
    elif num_str.isdigit() or (num_str.startswith('-') and num_str[1:].isdigit()):
        num = int(num_str)
        numbers.append(num)
    elif '.' in num_str:
        num_parts = num_str.split('.')
        if all(part.isdigit() for part in num_parts):
            num = float(num_str)
            numbers.append(num)
        else:
            print("Invalid input! Please enter a valid number or 'done' to finish.")
    else:
        print("Invalid input! Please enter a valid number or 'done' to finish.")

if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers were entered.")

