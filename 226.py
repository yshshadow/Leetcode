# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        # recursive
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # temp = root.left
        # root.left = root.right
        # root.right = temp
        # return root

        # iterative
        stack = [root]
        while len(stack) != 0:
            p = stack.pop()
            tmp = p.left
            p.left = p.right
            p.right = tmp
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return root
