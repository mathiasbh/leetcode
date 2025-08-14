
'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 7
Output: 4

'''


def searchInsert(nums: list[int], target: int) -> int:

    def binary_search(nums, target):
        left = 0
        right = len(nums) - 1 

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            
            if nums[mid] == target:
                return mid
        
        return left

    return binary_search(nums, target)


print(searchInsert([1,3,5,6], 5))