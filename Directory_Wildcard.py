# Write a Python Program to Make File Lists From Current Directory Using a Wildcard.
import glob
file_list = glob.glob('*.*')
print(file_list)