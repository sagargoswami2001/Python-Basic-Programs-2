# Write a Python Program to Compute the Product of a List of Integers (Without Using For Loop)

from functools import reduce
nums = [10, 20, 30]

nums_product = reduce((lambda x, y: x * y), nums)
print("Product of the Numbers:", nums_product)