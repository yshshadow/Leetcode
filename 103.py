# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.zigzag(root, res, 1)
        for x in range(len(res)):
            if x % 2 != 0:
                res[x].reverse()
        return res

    def zigzag(self, root, res, level):
        if not root:
            return
        if len(res) < level:
            res.append([])
        res[level - 1].append(root.val)
        self.zigzag(root.left, res, level + 1)
        self.zigzag(root.right, res, level + 1)
