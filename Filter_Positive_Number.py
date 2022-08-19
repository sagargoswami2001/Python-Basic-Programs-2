# Write a Python Program to Filter the Positive Number from the List.

num = [34, 1, 0, -23]
print("Original Numbers in the List: ", num)

new_nums = list(filter(lambda x: x>0, num))
print('Positive Number in the List: ', new_nums)