# Write a Python Program to find the median among three given numbers.

x = input("Input the First Number: ")
y = input("Input the Second Number: ")
z = input("Input the Third Number: ")

print("Median of the Above Three Numbers: ")

if y < x and x < z:
    print(x)
elif z < x and x < y:
    print(x)

elif z < y and y < x:
    print(y)
elif x < y and y < z:
    print(y)

elif y < z and z < x:
    print(z)
elif x < z and z < y:
    print(z)
