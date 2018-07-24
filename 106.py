# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder or len(postorder) == 0 or len(inorder) == 0:
            return None
        return self.build(postorder, inorder, 0, len(postorder), 0, len(inorder))

    def build(self, postorder, inorder, po_from, po_to, in_from, in_to):
        if po_to - po_from == 1:
            return TreeNode(postorder[po_to-1])
        if po_to - po_from == 0:
            return None
        root = TreeNode(postorder[po_to - 1])
        n_idx = 0
        for idx in range(in_from, in_to):
            if inorder[idx] == root.val:
                n_idx = idx
                break
        left_range = n_idx - in_from
        right_range = in_to - n_idx - 1
        root.right = self.build(postorder, inorder, po_to - 1 - right_range, po_to - 1, n_idx + 1, in_to)
        root.left = self.build(postorder, inorder, po_from, po_from + left_range, in_from, in_from + left_range)
        return root
