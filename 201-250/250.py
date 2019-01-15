# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# Example :
#
# Input:  root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# Output: 4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def unival(root):
            if not root:
                return True
            if not root.left and not root.right:
                self.count += 1
                return True
            l, r = unival(root.left), unival(root.right)
            if r and l and (not root.left or root.left.val == root.val) and (
                        not root.right or root.right.val == root.val):
                self.count += 1
                return True
            return False

        unival(root)
        return self.count


s = Solution()
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right = TreeNode(5)
root.right.right = TreeNode(5)
s.countUnivalSubtrees(root)
