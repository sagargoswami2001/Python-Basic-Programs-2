# Write a python program to find files and skip directories of a given directory.
import os
print([f for f in os.listdir('/Users/SHIVSHANKAR') if os.path.isfile(os.path.join('/Users/SHIVSHANKAR', f))])