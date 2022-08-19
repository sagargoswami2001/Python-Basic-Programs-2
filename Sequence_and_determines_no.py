# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.
def test_distinct(data):
    if len(data) == len(set(data)):
        return True
    else:
        return False;

print(test_distinct([1,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))