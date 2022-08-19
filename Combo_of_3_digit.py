# Write a Python program to create the combinatons of 3 digit combo.

nums = []
for num in range(1000):
    num = str(num).zfill(3)
print(num)
nums.append(num)