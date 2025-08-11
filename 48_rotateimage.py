'''
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to 
modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''


'''
A clockwise rotation can be seen as transposing and then reverse rows
'''

def rotate(matrix: list[list[int]]) -> None:
    # inplace
    
    # Transpose
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)