# Given a binary tree, return the preorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.recursive(root, res)
        return res

    def recursive(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.recursive(root.left, res)
        self.recursive(root.right, res)

    def iterative(self, root, res):
        if not root:
            return
        stack = [root]
        while root or len(stack) != 0:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
