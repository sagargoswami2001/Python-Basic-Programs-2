# Write a Python program to find the number of divisors of a given integer is even or odd.
def divisors(n):
    for i in range(n):
        x = len([i for i in range (1,n+1) if not n % i])
    return x
print(divisors(3))
print(divisors(6))
print(divisors(9))
print(divisors(12))
print(divisors(15))
