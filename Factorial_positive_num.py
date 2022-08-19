# Write a Python Program to find the number of zeros at the end of a factorial of a given positive number.

# Range of the number(n):(1 ≤ n ≤ 2*109)
def factorialzero(n):
    x = n // 5
    y = x
    while x > 0:
        x /= 5
        y += int(x)
    return y

print(factorialzero(5))
print(factorialzero(12))
print(factorialzero(100))
