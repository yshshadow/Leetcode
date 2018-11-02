# Given
# a
# node
# from a cyclic
#
# linked
# list
# which is sorted in ascending
# order, write
# a
# function
# to
# insert
# a
# value
# into
# the
# list
# such
# that
# it
# remains
# a
# cyclic
# sorted
# list.The
# given
# node
# can
# be
# a
# reference
# to
# any
# single
# node in the
# list, and may
# not be
# necessarily
# the
# smallest
# value in the
# cyclic
# list.
#
# If
# there
# are
# multiple
# suitable
# places
# for insertion, you may choose any place to insert the new value.After the insertion, the cyclic list should remain sorted.
#
# If
# the
# list is empty(i.e., given
# node is null), you
# should
# create
# a
# new
# single
# cyclic
# list and
# return the
# reference
# to
# that
# single
# node.Otherwise, you
# should
# return the
# original
# given
# node.
#
# The
# following
# example
# may
# help
# you
# understand
# the
# problem
# better:
#
# In
# the
# figure
# above, there is a
# cyclic
# sorted
# list
# of
# three
# elements.You
# are
# given
# a
# reference
# to
# the
# node
# with value 3, and we need to insert 2 into the list.
#
# The
# new
# node
# should
# insert
# between
# node
# 1 and node
# 3.
# After
# the
# insertion, the
# list
# should
# look
# like
# this, and we
# should
# still
# return node
# 3.


# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            n = Node(insertVal, None)
            n.next = n
            return n
        cur = head
        while cur:
            # start of ascending is the mini in loop
            # insert is less than mini or insert is max in sequence
            if cur.next.val < cur.val and (cur.next.val > insertVal or cur.val < insertVal):
                n = Node(insertVal, cur.next)
                cur.next = n
                return head
            if cur.next == head:  # same value loop
                n = Node(insertVal, cur.next)
                cur.next = n
                return head
            if cur.val <= insertVal <= cur.next.val:  # normal position in ascending order
                n = Node(insertVal, cur.next)
                cur.next = n
                return head
            cur = cur.next


head = Node(3, None)
head.next = Node(4, Node(1, head))
s = Solution()
s.insert(head, 2)
