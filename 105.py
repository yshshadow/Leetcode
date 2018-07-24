# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder or len(preorder) == 0 or len(inorder) == 0:
            return None
        return self.build(preorder, inorder, 0, len(preorder), 0, len(inorder))

    def build(self, preorder, inorder, pre_from, pre_to, in_from, in_to):
        if in_to - in_from == 0:
            return None
        if in_to - in_from == 1:
            return TreeNode(preorder[pre_from])
        root = TreeNode(preorder[pre_from])
        n_idx = 0
        for idx in range(in_from, in_to):
            if inorder[idx] == root.val:
                n_idx = idx
                break
        left_range = n_idx - in_from
        # right_range = in_to - idx - 1
        root.left = self.build(preorder, inorder, pre_from + 1, pre_from + 1 + left_range, in_from,
                               in_from + left_range)
        root.right = self.build(preorder, inorder, pre_from + 1 + left_range, pre_to, n_idx + 1, in_to)
        return root


s = Solution()
# n = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
m = s.buildTree([1, 2],
                [2, 1])
print(m)
