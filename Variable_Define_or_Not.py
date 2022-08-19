# Write a Python Program to Determine Whether Variable is Defined or Not.

try:
    x = 1
except NameError:
    print("Variable is Not Defined...!")
else:
    print("Variable is Defined.")

try:
    y
except NameError:
    print("Variable is Not Defined...!")
else:
    print("Variable is Defined.")
