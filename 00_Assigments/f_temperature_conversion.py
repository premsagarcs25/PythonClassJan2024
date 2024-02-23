#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
default should be celcius

HINTS: .strip(), indexing to get to know celecium or farhentient, 
    extract the temprature, adn then convert 
"""

user_input = input("Enter temperature (23c or 23F): ").strip().replace(" ","")

if "C" in user_input or "c" in user_input:
    temperature = float(user_input[:-1])#removing c or C
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C={converted_temperature}°F")

elif "F" in user_input or "f" in user_input:
    temperature = float(user_input[:-1])#removing f or F
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F={converted_temperature}°C")

else:
    temperature = float(user_input)
    print(f"{temperature}°C")
