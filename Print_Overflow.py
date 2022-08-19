'''Write a Python Program to compute and print sum of two given integers (more than or equal to zero).
if given integers or the sum have more than 80 digits, print "Overflow".'''

print("Input First Integer: ")
x = int(input())
print("Input Second Integer: ")
y = int(input())
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")
else:
    print("Sum of the two Integers: ",x + y)