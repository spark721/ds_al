"""
LeetCode
98
Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Start by defining helper function for recursive calls.
            base case to check if node is None.
            check if lower < value <= upper and return false if not.
            start recursive call with right side first with
                lower as current value and keep the current upper.
            if right side returns false, return false.
            do the same thing for left side with
                keep the current lower and upper and current value.
            if left side returns false, return false.
            at the end of the helper func, returns true.
        in the main func,
            return the call helper func with lower and upper as -inf and inf.
        """
        def _dfs(node, lower, upper):
            # base case
            if node is None:
                return True

            val = node.val
            # compare value with lower and upper
            if val <= lower or val >= upper:
                return False
            
            # recursive calls
            # right side
            if not _dfs(node.right, val, upper):
                return False
            # left side
            if not _dfs(node.left, lower, val):
                return False
            
            return True
        
        return _dfs(root, float('-inf'), float('inf'))
