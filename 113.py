# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

    def path(self,root,sum,stack,res):
        
        if not root.left and not root.right:  # is a leaf
            if root.val == sum:
                res.append(stack.copy())
            stack.pop()
        elif not root.left:  # left is empty
            sum -= root.val
            return self.hasPath(root.right, sum)
        elif not root.right:  # right is empty
            sum -= root.val
            return self.hasPath(root.left, sum)
        else:
            sum -= root.val
            return self.hasPath(root.left, sum) or self.hasPath(root.right, sum)