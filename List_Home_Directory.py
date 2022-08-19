# Write a python Program to list home directory without absolute path.
import os.path
print(os.path.expanduser('~'))