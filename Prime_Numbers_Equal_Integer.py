# Write a Python program to print the number of prime numbers which are less than or equal to a given integer.
# Input: n(1 ≤ n ≤ 999,999)

primes = [1] * 500000
primes[0] = 0
for i in range(3, 1000, 2):
    if primes[i // 2]:
        primes[(i * i) // 2::i] = [0] * len(primes[(i * i) // 2::i])

print("Input the Number(n): ")
n = int(input())
if n < 4:
    print("Number of prime numbers which are less than or equal to number: ", n-1)
else:
    print("Number of prime numbers which are less than or equal to number: ", sum(primes[:(n + 1) // 2]) + 1)
    