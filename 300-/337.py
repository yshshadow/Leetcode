# The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.dfs(root))

    def dfs(self, root):
        if not root:
            return 0, 0
        # if not root.left and not root.right:
        #     return 0, root.val
        l1, l2 = self.dfs(root.left)
        r1, r2 = self.dfs(root.right)
        return max(l2, l1) + max(r1, r2), l1 + r1 + root.val


root = TreeNode(3)
root.left = TreeNode(2)
root.left.right = TreeNode(3)
root.right = TreeNode(3)
root.right.right = TreeNode(1)

s = Solution()
print(s.rob(root))
