"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""

def twoSum(nums: list[int], target: int) -> list[int]:

    # create hash map for all
    hashmap = {num: idx for idx, num in enumerate(nums)}

    for i in range(len(nums)):
        required_value = target - nums[i]

        # Check if required value in hashmap
        # Do not allow use of same index twice
        if (required_value in hashmap) and (hashmap[required_value] != i):
            return [i, hashmap[required_value]]
    return []


test_case = [2,7,11,15]
print(twoSum(test_case, 9))