"""
Binary Trees - 1/4
Easy

Write a function that takes in a Binary Tree and returns a list of its 
branch sums (ordered from leftmost branch sum to rightmost branch sum). 
A branch sum is the sum of all values in a Binary Tree branch. 
A Binary Tree branch is a path of nodes in a tree that 
starts at the root node and ends at any leaf node. 
Each Binary Tree node has a value stored in a property called "value" and 
two children nodes stored in properties 
called "left" and "right," respectively. Children nodes can either be 
Binary Tree nodes themselves or the None (null) value.
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    res = []

    def dfs(node, running_sum):
        if node.left is None and node.right is None:
            res.append(running_sum + node.value)
            return
        if node.left: dfs(node.left, running_sum + node.value)
        if node.right: dfs(node.right, running_sum + node.value)
        return
    
    dfs(root, 0)

    return res
