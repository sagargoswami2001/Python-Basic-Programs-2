# Write a Python program to count the number of carry operations for each of a set of addition problems.
def carry_no(x, y):
    ctr = 0
    if(x == 0 and y == 0):
        return 0
    z = 0
    for i in reversed(range(10)):
        z = x%10 + y%10 + z
        if z > 9:
            z = 1
        else:
            z = 0
            ctr += z
            x //= 10
            y //= 10

    if ctr == 0:
        return "No Carry Operation."
    elif ctr == 1:
        return ctr
    else:
        return ctr

print(carry_no(786, 457))
print(carry_no(5, 6))