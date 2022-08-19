# Write a Python Program to Add Trailing and Leading Zeroes to a String.

str = '122.22'
print('Original String: ', str)
print("\nAdded Trailing Zeros:")
str = str.ljust(8, '0')
print(str)

str = str.ljust(10, '0')
print(str)
print('\nAdded Leading Zeros:')
str = '122.22'
str = str.rjust(8, '0')
print(str)
str = str.rjust(10, '0')
print(str)