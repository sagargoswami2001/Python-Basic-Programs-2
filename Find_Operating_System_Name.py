# Write a Python Program to find the Operating System Name, Platform and Platform Release Date.
import os, platform
print("Operating System Name: ")
print(os.name)
print("Platform Name: ")
print(platform.system())
print("Platform Release: ")
print(platform.release())