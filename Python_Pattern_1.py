# Python Code to print pyramid pattern using recursion.
def sagar(n):
    if n == 0:
        return
    else:
        sagar(n-1)
        print("* "*n)

# Driver Code
n = 7
sagar(n)