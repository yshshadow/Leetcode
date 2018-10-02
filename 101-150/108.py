# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = (0 + len(nums)-1) // 2
        root = TreeNode(nums[mid])
        self.helper(nums, 0, mid - 1, root, True)
        self.helper(nums, mid + 1, len(nums)-1, root, False)
        return root

    def helper(self, nums, start, end, root, lchild):
        if start > end:
            return
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        if lchild:
            root.left = node
        else:
            root.right = node
        self.helper(nums, start, mid - 1, node, True)
        self.helper(nums, mid + 1, end, node, False)


s = Solution()
nums = [-10, -3, 0, 5, 9]
root = s.sortedArrayToBST(nums)
print(root.val)
