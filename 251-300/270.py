# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    m_node = None
    m_value = 2147483649.0

    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        # use dfs, not the best
        #     self.m_node = root
        #     self.m_value = abs(root.val - target)
        #     self.dfs(root, target)
        #     return self.m_node.val
        #
        # def dfs(self, root, target):
        #     if not root:
        #         return
        #     if abs(root.val - target) < self.m_value:
        #         self.m_value = abs(root.val - target)
        #         self.m_node = root
        #     self.dfs(root.left, target)
        #     self.dfs(root.right, target)

        # use bst
        if not root:
            return None

        ret = root.val

        while root:
            if abs(target - root.val) < abs(target - ret):
                ret = root.val

            root = root.left if target < root.val else root.right

        return ret


root = TreeNode(1500000000)
root.left = TreeNode(1400000000)
s = Solution()
s.closestValue(root, -1500000000)

[1500000000, 1400000000]
-1500000000.0
