#
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    max_length = -2147483648

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_length = -2147483648
        self.helper(root)
        return self.max_length

    def helper(self, root):
        if not root:
            return 0
        l_max = self.helper(root.left)
        r_max = self.helper(root.right)
        self.max_length = max(self.max_length, l_max + r_max + root.val)
        return max(l_max, r_max, 0) + root.val
