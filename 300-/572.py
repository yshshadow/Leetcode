# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
#
# Example 1:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.traverse(s, t)

    def traverse(self, s, t):
        return s is not None and (self.equal(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t))

    def equal(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        else:
            return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)


so = Solution()
s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.right.left = TreeNode(2)
t = TreeNode(3)
t.left = TreeNode(1)
t.right = TreeNode(2)
print(so.isSubtree(s, t))
