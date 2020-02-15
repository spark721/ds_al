class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []
        # initialize the matrix with all 0s
        for i in range(m):
            matrix.append([0]*n)

        # set all left columns to 1
        for i in range(m):
            matrix[i][0] = 1

        # set all top row to 1
        for j in range(n):
            matrix[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        
        return matrix[m-1][n-1]
        