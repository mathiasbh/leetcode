


'''
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

'''




def searchRange(nums: list[int], target: int) -> list[int]:
    # loop through to see how it performs (bruteforce) O(n) ....
    # fi, ei = -1, -1
    # 
    # left = 0
    # right = len(nums)-1
    # for i in range(len(nums)):
    #     if nums[left] == target:
    #         fi = left
    #     else:
    #         left += 1
    #     if nums[right] == target:
    #         ei = right
    #     else:
    #         right -= 1
    # 
    # return [fi, ei]

    # O(log(n)) - binary search


    def left_binary_search(nums):
        left_index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] == target:
                left_index = mid
        return left_index


    
    def right_binary_search(nums):
        right_index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == target:
                right_index = mid
        return right_index

    li = left_binary_search(nums)
    ri = right_binary_search(nums)
    return [li, ri]
        
        
print(searchRange([5,7,7,8,8,10], 8))