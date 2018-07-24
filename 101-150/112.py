# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.hasPath(root, sum)

    def hasPath(self, root, sum):
        if not root.left and not root.right:  # is a leaf
            if root.val == sum:
                return True
            else:
                return False
        elif not root.left:  # left is empty
            sum -= root.val
            return self.hasPath(root.right, sum)
        elif not root.right:  # right is empty
            sum -= root.val
            return self.hasPath(root.left, sum)
        else:
            sum -= root.val
            return self.hasPath(root.left, sum) or self.hasPath(root.right, sum)
