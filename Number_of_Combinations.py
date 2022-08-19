'''Write a Python Program which reads an integer n and find the number of combinations of a,b,c and d
(0 ≤ a,b,c,d ≤ 9) where (a+b+c+d) will be equal to n.
'''
# Input: n(1 ≤ n ≤ 50)

import itertools
print("Input the Number(n): ")
n = int(input())
result = 0
for (i,j,k) in itertools.product(range(10),range(10),range(10)):
    result+=(0<=n-(i+j+k)<=9)
print("Number of Combinations: ",result)