"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


"""


def generate(numRows: int) -> list[list[int]]:
    
    triangle = [[1], [1, 1]]
    
    
    if numRows == 1:
        return [triangle[0]]
    
    if numRows == 2:
        return [triangle[1]]

    for i in range(1, numRows - 1):
        prev_row = triangle[i]
        curr_row = [1]

        for j in range(len(prev_row)-1):
            curr_row.append(prev_row[j]+prev_row[j+1])
        curr_row.append(1) 

        triangle.append(curr_row)
    return triangle


res = generate(5)
print(res)