# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.levelOrder2(root, res, 1)
        return res

    def levelOrder2(self, root, res, level):
        if not root:
            return
        if level > len(res):
            res.append([])
        res[level - 1].append(root.val)
        if not root.left and not root.right:
            return
        else:
            self.levelOrder2(root.left, res, level + 1)
            self.levelOrder2(root.right, res, level + 1)


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.levelOrder(root))
