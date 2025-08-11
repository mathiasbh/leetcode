

"""
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

    
def maxArea(height: list[int]) -> int:

    # two pointers, start at left and right edges
    # move lowest valued pointer

    pointer_left = 0
    pointer_right = len(height) - 1

    max_area = 0

    while pointer_left < pointer_right:
        container_height = min(height[pointer_left], height[pointer_right])
        container_width = pointer_right - pointer_left
        new_area = container_height * container_width
        if max_area < new_area:
            max_area = new_area

        if height[pointer_left] > height[pointer_right]:
            pointer_right -= 1
        else:
            pointer_left += 1


    return max_area
            
            
            
print(maxArea([1,8,6,2,5,4,8,3,7]))