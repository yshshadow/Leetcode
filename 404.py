# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        elif not root.left and not root.right:
            return 0
        return self.sumOfLeft(root, True)

    def sumOfLeft(self, root, is_left):
        if not root:
            return 0
        elif is_left and not root.left and not root.right:  # left
            return root.val
        elif not is_left and not root.left and not root.right:  # right
            return 0
        else:
            return self.sumOfLeft(root.left, True) + self.sumOfLeft(root.right, False)

s = Solution()
t = TreeNode(1)
print(s.sumOfLeftLeaves(t))