# Given
# a
# binary
# tree,
# return the
# postorder
# traversal
# of
# its
# nodes
# ' values.
#
# For
# example:
# Given
# binary
# tree[1, null, 2, 3],
#
# 1
# \
# 2
# /
# 3
#
# return [3, 2, 1].
#
# Note: Recursive
# solution is trivial, could
# you
# do
# it
# iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        # self.recursive(root, res)
        self.iterative(root, res)
        return res

    def recursive(self, root, res):
        if not root:
            return
        self.recursive(root.left, res)
        self.recursive(root.right, res)
        res.append(root.val)

    def iterative(self, root, res):
        if not root:
            return
        stack = []

        return
