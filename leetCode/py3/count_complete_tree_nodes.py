
# LeetCode
# 222
# Medium

# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        init count = 0
        DFS approach as a closure
        	if !node return
        	increment count
        return count
        '''
        self.count = 0
        if not root: return self.count
        
        def dfs(node):
        	self.count += 1
        	if node.left: dfs(node.left)
        	if node.right: dfs(node.right)
                
        dfs(root)
        
        return self.count
