# Given a binary tree, find the length of the longest consecutive sequence path.
#
# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
#
# Example 1:
#
# Input:
#
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5
#
# Output: 3
#
# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
# Example 2:
#
# Input:
#
#    2
#     \
#      3
#     /
#    2
#   /
#  1
#
# Output: 2
#
# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1, 1
            left_max, left_conse = 0, 0
            right_max, right_conse = 0, 0
            local_conse = 1
            if root.left:
                left_max, left_conse = helper(root.left)
                if root.left.val + 1 == root.val:
                    local_conse = max(local_conse, left_conse + 1)
            if root.right:
                right_max, right_conse = helper(root.right)
                if root.right.val + 1 == root.val:
                    local_conse = max(local_conse, right_conse + 1)
            return max(left_max, right_max, local_conse), local_conse

        return helper(root)[0]


s = Solution()
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print(s.longestConsecutive(root))
