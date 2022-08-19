# Write a Python Program to Get Numbers Divisible by Fifteen From a List Using an Anonymous Function.

from unittest import result


num_list = [45, 55, 60, 37, 100, 105, 220]

# Use Anonymous Function to Filter
result = list(filter(lambda x: (x % 15 == 0), num_list))
print('Numbers Divisible by 15 are', result)