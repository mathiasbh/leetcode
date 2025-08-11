
"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Constraints:
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10

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
        
    
    return [list(perm) for perm in set(tuple(perm) for perm in perms)]


print(permute([1,1,2]))