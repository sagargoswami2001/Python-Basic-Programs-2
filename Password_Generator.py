# Password Generator Using Python.
import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}#@()!$&*;.^_-:~"

merge = lower_case + upper_case + numbers + symbols
lenght = 9

password = "".join(random.sample(merge,lenght))
print("Generated Password is ",password)