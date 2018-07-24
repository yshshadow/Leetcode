# Given a binary tree, return the inorder traversal of its nodes' values.
#
# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.iterative(root, res)
        # self.recursive(root, res)
        return res

    def recursive(self, root, res):
        if not root:
            return
        self.recursive(root.left, res)
        res.append(root.val)
        self.recursive(root.right, res)

    def iterative(self, root, res):
        if not root:
            return
        stack = []
        top = root
        while top or len(stack) != 0:
            while top:
                stack.append(top)
                top = top.left
            if len(stack) != 0:
                top = stack[len(stack) - 1]
                res.append(top.val)
                stack.pop()
                top = top.right


s = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
s.inorderTraversal(root)
