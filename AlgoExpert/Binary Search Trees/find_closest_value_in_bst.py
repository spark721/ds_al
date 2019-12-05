"""
Binary Search Trees - 1/5
Easy

Find Closest Value In BST

You are given a BST data structure consisting of BST nodes. 
Each BST node has an integer value stored in a property called "value" and 
two children nodes stored in properties called "left" and "right," respectively. 
A node is said to be a BST node if and only if it satisfies the BST property: 
its value is strictly greater than the values of every node to its left
its value is less than or equal to the values of every node to its right
and both of its children nodes are either BST nodes themselves or 
None (null) values. You are also given a target integer value; 
write a function that finds the closest value to 
that target value contained in the BST. 
Assume that there will only be one closest value.
"""


def findClosestValueInBst(tree, target):
    # Write your code here.
	res = None
	que = [tree]

	while que:
		node = que.pop(0)
		_diff = abs(node.value - target)
		if res is None or abs(res - target) > _diff:
			res = node.value
		if target > node.value and node.right:
			que.append(node.right)
		elif target < node.value and node.left:
			que.append(node.left)
		elif target == res:
			return res

	return res
