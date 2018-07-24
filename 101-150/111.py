# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return self.minD(root)
        else:
            return 0

    def minD(self, root):
        if not root.left and not root.right:
            return 1
        elif not root.left:
            return self.minD(root.right) + 1
        elif not root.right:
            return self.minD(root.left) + 1
        else:
            return min(self.minD(root.left), self.minD(root.right)) + 1
