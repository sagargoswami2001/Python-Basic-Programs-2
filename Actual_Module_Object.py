# Write a Python Program to Get the Actual Module Object for a Given Object.

from inspect import getmodule
from math import sqrt
print(getmodule(sqrt))