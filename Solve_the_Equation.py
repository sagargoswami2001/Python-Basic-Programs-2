# Write a Python program which solve the equation:

# ax+by=c
# dx+ey=f
# print the values of x,y where a,b,c,d,e and f are given.
# Input: a,b,c,d,e,f separated by a single space. (-1,000 ≤ a,b,c,d,e,f ≤ 1,000)

print("Input the Value of a, b, c, d, e, f: ")
a, b, c, d, e, f = map(float, input().split())
n = a*e - b*d
print("Values of X and Y: ")
if n != 0:
    x = (c*e - b*f) / n
    y = (a*f - c*d) / n
    print('{:.3f} {:.3f}'.format(x+0, y+0))