
# LeetCode
# 240
# Medium

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted in ascending from left to right.
#     Integers in each column are sorted in ascending from top to bottom.

# Example:

# Consider the following matrix:

# [
#     [1,   4,  7, 11, 15],
#     [2,   5,  8, 12, 19],
#     [3,   6,  9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]

# Given target = 5, return true.

# Given target = 20, return false.



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        start at top right corner or bottom left
        move row or col compared to the target
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0: return False
        if target < matrix[0][0] or target > matrix[-1][-1]: return False

        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            if target == matrix[row][col]: return True
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
        
        return False
