'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, 
you need to do the following things:

    . Change the array nums such that the first k elements of nums contain the 
    unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    . Return k.


'''


def removeDuplicates(nums: list[int]) -> int:
    # 0 0 1 1 1 2 2 3 3 4
    # i j, duplicate, ignore, increase j by 1

    # 0 0 1 1 1 2 2 3 3 4
    # i   j, non-dupe, move j value to i+1 and increase i by one

    # 0 1 1 1 1 2 2 3 3 4
    # i   j
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
            

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))