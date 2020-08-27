# Given the root of a binary tree where each node contains an integer, determine the sum of all of the integer values in the tree.

# Example:

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# The expected output given the above tree is 5 + 4 + 8 + 11 + 13 + 4 + 7 + 2 + 1, so your function should return 55.

# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def tree_paths_sum(root):
    if root == None:
        return 0
    return root.value + tree_paths_sum(root.left) + tree_paths_sum(root.right)

    # val = root.value
    # if root.left is None and root.right is None:
    #     return val
    # if root.left:
    #     left = tree_paths_sum(root.left)
    #     return left
    # if root.right:
    #     right = tree_paths_sum(root.right)
    #     return right
    # result = val + left + right
    # print(result)
    # return result
