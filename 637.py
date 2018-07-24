# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        count = []
        self.average(root, res, 1, count)
        for x in range(len(res)):
            res[x] = float(res[x])/float(count[x])
        return res

    def average(self, root, res, level, count):
        if not root:
            return
        if len(res) < level:
            res.append(0)
            count.append(0)
        res[level - 1] += root.val
        count[level - 1] += 1
        self.average(root.left, res, level + 1, count)
        self.average(root.right, res, level + 1, count)
