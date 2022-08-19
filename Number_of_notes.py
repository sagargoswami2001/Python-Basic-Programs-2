# Write a Python Program to find the number of notes (Sample of notes: 10,20,50,100,200 and 500) against a given

# Range - Number of notes(n): n(1 ≤ n ≤ 1000000)
def no_notes(a):
    Q = [500, 200, 100, 50, 20, 10]
    X = 0
    for i in range(6):
        q = Q[i]
        X += int(a / q) 
        a = int(a % q)
    if a > 0:
        X = -1
    return X
print(no_notes(880))
print(no_notes(1000))