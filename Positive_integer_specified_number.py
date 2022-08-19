# Write a python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller then the specified number.
# Ex.: 8 = 73+63+53+43+33+23+13 = 784

def sum_of_cubes(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
    return total
print("Sum of Cubes: ", sum_of_cubes(9))