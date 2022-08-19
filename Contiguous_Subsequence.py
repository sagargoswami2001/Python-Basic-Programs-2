'''Write a python program to find the maximum sum of a contiguous subsequence from a given sequence of numbers 
a1, a2, a3, ... An. A subsequence of one element is also a continuous subsequence.'''
# Input: You Can Assume That 1 ≤ N ≤ 5000 and -100000 ≤ Ai ≤ 100000. 
# Input Numbers Are Separated by a Space. Input 0 to Exit.

while True:
    print("Input Number of Sequence of Numbers you want to input (0 to exit): ")
    n = int(input())
    if n == 0:
        break
    else:
        A = []
        Sum = []
        print("Input Number: ")
        for i in range(n):
            A.append(int(input()))
        Wa = 0
        for i in range(0,n):
            Wa += A[i]
            Sum.append(Wa)
        for i in range(0, n):
            for j in range(0, i):
                Num = Sum[i] - Sum[j]
                Sum.append(Num)
        print("Maximum Sum of the Said Contiguous Subsequence: ")
        print(max(Sum))