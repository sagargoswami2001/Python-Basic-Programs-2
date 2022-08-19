# Write a Python Program to Retrieve File Properties.
import os.path
import time
print('File         :', __file__)
print('Access Time  :', time.ctime(os.path.getatime(__file__)))
print('Modified Time:', time.ctime(os.path.getmtime(__file__)))
print('Change Time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))