'''Write a Python program to reverse the digits of a given number and add it to the original, if the sum is 
not a palindrome repeat this procedure.'''

'''NOTE: A palindrome is a word, number, or other sequence of characters which reads the same backward as 
forward, such as madam or racecar.'''

def rev_num(n):
    s = 0
    while True:
        k = str(n)
        if k == k[::-1]:
            break
        else:
            m = int(k[::-1])
            n += m
            s += 1
    return n

print(rev_num(1234))
print(rev_num(1473))