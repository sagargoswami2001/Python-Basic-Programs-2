# Write a Python Program to Prove that Two String Variables of Same Value Point Same Memory Location.

str1 = 'Python'
str2 = 'Python'

print('\nMemory Location of Str1 =', hex(id(str1)))
print('\nMemory Location of Str2 =', hex(id(str2)))
print()