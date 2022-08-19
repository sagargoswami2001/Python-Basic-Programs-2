# Write a Python Program to Prove that Two String Variables of Same Value Point Same Memory Location.

def remove_duplicates(nums):
    for i in range (len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
        return len(nums)

print(remove_duplicates([0,0,1,1,2,2,3,3,4,4,4]))
print(remove_duplicates([1,2,2,3,4,4]))