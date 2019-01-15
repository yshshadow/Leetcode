# Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
# Example:
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
#     4
#    / \
#   2   5
#  / \
# 1   3
#
# Output: [4,3]
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        res = collections.deque()

        def helper(root):
            if not root:
                return
            if root.left:
                helper(root.left)
            cur = root.val
            if len(res) < k:
                res.append(cur)
            else:
                if target < res[0]:
                    return
                else:
                    res.popleft()
                    res.append(cur)
            if root.right:
                helper(root.right)

        return list(res)
