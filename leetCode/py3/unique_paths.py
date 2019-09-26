
# Leetcode
# 62
# Medium

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?


# Above is a 7 x 3 grid. How many possible unique paths are there?

# Note: m and n will be at most 100.

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:

# Input: m = 7, n = 3
# Output: 28



class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	'''
    	init list of length == n and each inner as length == m
    	fill it all with 1 to start with

    	start iteration from l[1][1]
    	replace the cur element by adding the left and above

    	return l[-1][-1]
    	'''
    	grid = list()

    	for i in range(n):
    		grid.append([1] * m)

    	i = 1
    	while i < n:
    		j = 1
    		while j < m:
	    		up = grid[i - 1][j]
	    		left = grid[i][j - 1]
	    		grid[i][j] = up + left
	    		j += 1
	    	i += 1

    	return grid[-1][-1]




















