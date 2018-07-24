# Given
# a
# binary
# tree, imagine
# yourself
# standing
# on
# the
# right
# side
# of
# it,
# return the
# values
# of
# the
# nodes
# you
# can
# see
# ordered
# from top to
#
# bottom.
#
# For
# example:
# Given
# the
# following
# binary
# tree,
#
# 1 < ---
# / \
#     2
# 3 < ---
# \ \
#     5
# 4 < ---
#
# You
# should
# return [1, 3, 4].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dv_dict = {}
        max_depth = -1
        stack = [(0, root)]
        while len(stack):
            depth, node = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                dv_dict.setdefault(depth, node.val)
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return [dv_dict[d] for d in range(max_depth + 1)]


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(s.rightSideView(root))
