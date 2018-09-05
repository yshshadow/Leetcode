# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, sum, [], res)
        return res

    def helper(self, root, target, adds, res):
        if root and target == root.val and not root.left and not root.right:
            res.append(adds+[root.val])
            return
        elif not root:
            return
        else:
            if root:
                self.helper(root.left, target - root.val, adds + [root.val], res)
                self.helper(root.right, target - root.val, adds + [root.val], res)

root = TreeNode(5)
root.left=TreeNode(4)
root.right=TreeNode(8)
root.left.left=TreeNode(11)
root.left.left.left=TreeNode(7)
root.left.left.right=TreeNode(2)
root.right.left=TreeNode(13)
root.right.right=TreeNode(4)
root.right.right.left=TreeNode(5)
root.right.right.right=TreeNode(1)

# root = TreeNode(-2)
# root.left=TreeNode(-3)

s=Solution()
print(s.pathSum(root,22))