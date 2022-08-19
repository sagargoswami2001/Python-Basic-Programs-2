# Write a Python Program to get System Command Output.
import subprocess

# file and directory listing
text = subprocess.check_output("dir", shell = True, universal_newlines = True)
print("dir command to list file and directory")
print(text)