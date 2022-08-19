'''Write a Python program to check whether three given lengths(integers) of three sides from a right triangle.
Print "Yes" if the given sides form a right triangle otherwise print "No".
'''

# Input: Integers Separated by a single space. 1 ≤ lenght of the side ≤ 1,000
print("Input three integers(sides of a triangle)")
int_num = list(map(int, input().split()))
x,y,z = sorted(int_num)

if x**2+y**2==z**2:
    print('Yes')
else:
    print('No')