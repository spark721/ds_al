"""
Binary Trees - 2/4
Medium

Write a function that takes in a Binary Tree and inverts it. 
In other words, the function should swap every left node in the tree 
for its corresponding (mirrored) right node. 
Each Binary Tree node has a value stored in a property called "value" and 
two children nodes stored in properties 
called "left" and "right," respectively. 
Children nodes can either be 
Binary Tree nodes themselves or the None (null) value.
"""

def invertBinaryTree(tree):
    # iterative BFS
	queue = [tree]
	while len(queue):
		node = queue.pop(0)
		node.left, node.right = node.right, node.left
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return tree


    # # recursive
    # if tree is None:
    #     return
    # tree.left, tree.right = tree.right, tree.left
    # invertBinaryTree(tree.left)
    # invertBinaryTree(tree.right)
