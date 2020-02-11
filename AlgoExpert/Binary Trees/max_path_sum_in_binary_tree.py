# Max Path Sum in Binary Tree

# Write a function that takes in a Binary Tree and returns its max path sum. 
# A path is a collection of connected nodes 
# where no node is connected to more than two other nodes; 
# a path sum is the sum of the values of the nodes in a particular path. 
# Each Binary Tree node has a value stored in a property called "value" and 
# two children nodes stored in properties called "left" and "right," respectively. 
# Children nodes can either be Binary Tree nodes themselves or the None (null) value.


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def maxPathSum(tree):
    _, max_sum = find_max_sum(tree)
    return max_sum

def find_max_sum(tree):
    # base case
    if tree is None:
        return (0, 0)

    left_max_sum_branch, left_max_path_sum = find_max_sum(tree.left)
    right_max_sum_branch, right_max_path_sum = find_max_sum(tree.right)
    max_child_sum_branch = max(left_max_sum_branch, right_max_sum_branch)

    value = tree.value
    max_sum_branch = max(max_child_sum_branch + value, value)
    max_sum_as_root = max(
        left_max_sum_branch + value + right_max_sum_branch,
        max_sum_branch
    )
    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_root)

    return (max_sum_branch, max_path_sum)





# tree1 = BinaryTree(1).insert([2, 3]) # => 6
# tree2 = BinaryTree(1).insert([2, -1]) # => 3
# tree3 = BinaryTree(1).insert([-5, 3, 6]) # => 6
tree4 = BinaryTree(1).insert([2, 3, 4, 5, 6, 7]) # => 18

maxPathSum(tree4)



