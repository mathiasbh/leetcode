"""Given an array nums of distinct integers, return all the possible. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Constraints:
    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

"""

def permute(nums: list[int]) -> list[list[int]]:
    # 1) Take first element A
    # 2) Take second element B, construct new results by appending in front and after AB BA
    # 3) Take third element C, append infront, behind, between 
    # AB: ABC, CAB, ACB
    # BA: BAC, CBA, BCA
    
    if len(nums) < 2:
        return [[nums[0]]]
    
    # Manually write two first elements
    perms = [[nums[0], nums[1]], [nums[1], nums[0]]]
    
    # Iteratate, insert next number in all possible positions
    for i in range(2, len(nums)):
        new_perms = []
        for perm in perms:
            for j in range(len(perm) + 1):
                # Cannot use perm.insert(ind, obj) as it changes perm while we iterate.
                p = perm[:j] + [nums[i]] + perm[j:]
                new_perms.append(p)
        perms = new_perms
    return perms


print(permute([1,2,3,8,5]))