'''
Write a Python program to find the difference between the largest integer and the smallest integer which 
are created by 8 numbers from 0 to 9. The number that can be rearranged shall start with 0 as in 00135668.
'''
# Input: Data is a sequence of 8 numbers (numbers from 0 to 9).
# Output: The difference between the largest integer and the smallest integer.

print("Input an integer Created by 8 Numbers from 0 to 9: ")
num = list(input())
print("Difference Between the Largest and the Smallest Integer from the Given Integer: ")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))