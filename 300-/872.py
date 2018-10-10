# Consider
# all
# the
# leaves
# of
# a
# binary
# tree.From
# left
# to
# right
# order, the
# values
# of
# those
# leaves
# form
# a
# leaf
# value
# sequence.
#
# For
# example, in the
# given
# tree
# above, the
# leaf
# value
# sequence is (6, 7, 4, 9, 8).
#
# Two
# binary
# trees
# are
# considered
# leaf - similar if their
# leaf
# value
# sequence is the
# same.
#
# Return
# true if and only if the
# two
# given
# trees
# with head nodes root1 and root2 are leaf-similar.
#
# Note:
#
# Both
# of
# the
# given
# trees
# will
# have
# between
# 1 and 100
# nodes.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import itertools
import collections


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res1, res2 = [], []
        self.dfs(root1, res1)
        self.dfs(root2, res2)
        return all(x == y for x, y in itertools.zip_longest(res1, res2))

    def dfs(self, root, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(root.val)
        else:
            if root.left:
                self.dfs(root.left, res)
            if root.right:
                self.dfs(root.right, res)


s = Solution()
print(s.leafSimilar(None, None))
