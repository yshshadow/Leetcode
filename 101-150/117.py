# Given a binary tree
#
# struct TreeLinkNode {
#   TreeLinkNode *left;
#   TreeLinkNode *right;
#   TreeLinkNode *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# Example:
#
# Given the following binary tree,
#
#      1
#    /  \
#   2    3
#  / \    \
# 4   5    7
# After calling your function, the tree should look like:
#
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \    \
# 4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        pre, cur, nex = None, root, None
        while cur:
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                        pre = pre.next
                    else:
                        pre = cur.left
                    if not nex:
                        nex = cur.left
                if cur.right:
                    if pre:
                        pre.next = cur.right
                        pre = pre.next
                    else:
                        pre = cur.right
                    if not nex:
                        nex = cur.right
                cur = cur.next
            cur = nex
            pre = None
            nex = None
