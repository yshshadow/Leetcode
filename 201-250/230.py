# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.idx = -1

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # recursive
        self.idx = k
        return self.helper(root)[0]

    def helper(self, root):
        if not root:
            return None, False
        if root.left:
            l, find = self.helper(root.left)
            if find:
                return l, True
        self.idx -= 1
        if self.idx == 0:
            return root.val, True
        if root.right:
            r, find = self.helper(root.right)
            if find:
                return r, True
        return None, False

        # def kthSmallest(self, root, k):
        #     """
        #     :type root: TreeNode
        #     :type k: int
        #     :rtype: int
        #     """
        #     iterative
        #     stack = []
        #     while stack or root:
        #         while root:
        #             stack.append(root)
        #             root=root.left
        #         root=stack.pop()
        #         k-=1
        #         if k==0:
        #             return root.val
        #         root=root.right
        #     return -1


s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)
s.kthSmallest(root, 3)
