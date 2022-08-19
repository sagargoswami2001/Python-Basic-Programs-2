'''Write a Python program to that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. 
Jan. 1, 2016, is Friday. Note that 2016 is a leap year.'''

# Input: Two integers m and d separated by a single space in a line, m ,d represent the month and the day.

from datetime import date
print("Input Month and Date (Separated by a Single Space): ")
m, d = map(int, input().split())
weeks = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
w = date.isoweekday(date(2016, m, d))
print("Name of the Date: ",weeks[w])