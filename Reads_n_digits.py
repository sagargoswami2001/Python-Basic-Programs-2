'''Write a Python program that reads n digits (given) chosen from 0 to 9 and prints the number of combinations 
where the sum of the digits equals to another given number (s). Do not use the same digits in a combination.'''

# Input: Two integers as number of combinations and their sum by a single space in a line. Input 0 0 to exit.
import itertools
print('Input Number of Combinations and Sum, Input 0 0 to exit:')
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    s = list(itertools.combinations(range(10), x))
    ctr = 0
    for i in s:
        if sum(i) == y:
            ctr += 1

print(ctr)