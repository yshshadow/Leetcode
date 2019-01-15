# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Example 1:
#
# Input: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# Output: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
# Example 2:
#
# Input: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# Output: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3
# Follow up:
#
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = None
        self.fro = None
        self.to = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        self.fro.val, self.to.val = self.to.val, self.fro.val

    def helper(self, root):
        if not root:
            return
        if root.left:
            self.helper(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.fro:
                self.fro = self.pre
            if self.fro:
                self.to = self.cur
        self.pre = root
        if root.right:
            self.helper(root.right)


root = TreeNode(5)
root.left = TreeNode(3)
root.left.right = TreeNode(2)
s = Solution()
s.recoverTree(root)
