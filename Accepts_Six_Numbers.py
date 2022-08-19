# Write a Python Program that accepts six numbers as input and sorts them in descending Order.

'''Input: Input Consists of six numbers n1,n2,n3,n4,n5,n6 (-100000 ≤ n1,n2,n3,n4,n5,n6 ≤ 100000).
   The Six Numbers are Separated by a Space.'''

print("Input Six Integers: ")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After Sorting the said integers: ")
print(*nums)