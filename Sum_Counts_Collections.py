# Write a Python Program to Sum of All Counts in a Collections.

import collections
num = [2,2,4,6,6,8,6,10,4,5,7]
print(sum(collections.Counter(num).values()))