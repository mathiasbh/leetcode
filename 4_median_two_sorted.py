"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""



def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    new_list = sorted(list(nums1+nums2))
    n = len(new_list)

    if n % 2 == 0:
        med = (new_list[int(n/2)-1] + new_list[int(n/2)]) / 2.0
    else:
        med = new_list[int(n/2)]
    
    return float(med)


print(findMedianSortedArrays([1,2],[3,4]))