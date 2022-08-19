# Write a Python program to compute the digit number of sum of two given integers.
'''
Input: Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 ≤ x,y ≤ 1000000
'''
print("Input Two Integers(A B): ")
a,b = map(int, input().split(" "))
print("Number of Digit of A and B: ")
print(len(str(a+b)))