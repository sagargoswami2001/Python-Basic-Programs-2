'''Write a python program to check the sum of three elements (each from an array) from three arrays is equal to
a target value. print all those three-element combinations.'''

import itertools
from functools import partial
x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
T = 70

def check_sum_array(N, *nums):
    if sum(x for x in nums) == N:
        return (True, nums)
    else:
        return (False, nums)

pro = itertools.product(x,y,z)
func = partial(check_sum_array, T)
sums = list(itertools.starmap(func, pro))

result = set()
for s in sums:
    if s[0] == True and s[1] not in result:
        result.add(s[1])
        print(result)