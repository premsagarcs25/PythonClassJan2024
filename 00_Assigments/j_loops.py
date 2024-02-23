#!/usr/bin/python3
"""
Purpose:
    break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
	sys.exit  - will exit the script execution
"""

students = ["akram", "trusha", "bhavana", "jaya", "chaitra"]

# assignment - try the same using for loop

import sys

students = ["akram", "trusha", "bhavana", "jaya", "chaitra"]

for student in students:
    print(f"Processing student: {student}")
    if student == "jaya":
        print("Found Jaya. Exiting the loop.")
        sys.exit()  
    elif student == "bhavana":
        print("Skipping Bhavana.")
        continue  
    elif student == "trusha":
        print("Trusha is yet to be processed. Adding a placeholder.")
        pass
    else:
        break

print("Loop execution completed.")

