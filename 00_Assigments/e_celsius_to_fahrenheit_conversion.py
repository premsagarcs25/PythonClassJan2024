#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit


farhenheit = (1.8 * celsius) + 32  # PEMDAS

Algorithm:
step 1: take celcius , clear and validate 
step 2: convert and give farhenheit
"""



# Step 1: Take Celsius input and validate
celsius = input("Enter temperature in Celsius: ").lstrip().replace(" ","")
print(celsius)
if not (celsius.isdigit() or celsius.startswith('-')):
    print(f"{celsius} please enter a valid celsius value")
    exit()
celsius = float(celsius)
# Step 2: Convert Celsius to Fahrenheit
fahrenheit = (1.8 * celsius) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")