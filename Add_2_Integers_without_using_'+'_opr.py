# Write a Python Program to add two positive integers without using '+' operator.
# Note: Use bitwise operations to add two numbers.

def add_without_plus_operator(a, b):
    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1
    return a
print(add_without_plus_operator(2, 10))
print(add_without_plus_operator(-20, 10))
print(add_without_plus_operator(-10, -20))