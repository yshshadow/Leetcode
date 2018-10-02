# Sort
# a
# linked
# list
# using
# insertion
# sort.
#
# A
# graphical
# example
# of
# insertion
# sort.The
# partial
# sorted
# list(black)
# initially
# contains
# only
# the
# first
# element in the
# list.
# With
# each
# iteration
# one
# element(red) is removed
# from the input
#
# data and inserted in -place
# into
# the
# sorted
# list
#
# Algorithm
# of
# Insertion
# Sort:
#
# Insertion
# sort
# iterates, consuming
# one
# input
# element
# each
# repetition, and growing
# a
# sorted
# output
# list.
# At
# each
# iteration, insertion
# sort
# removes
# one
# element
# from the input
#
# data, finds
# the
# location
# it
# belongs
# within
# the
# sorted
# list, and inserts
# it
# there.
# It
# repeats
# until
# no
# input
# elements
# remain.
#
# Example
# 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example
# 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        head, pre, cur = dummy, dummy, head

        while cur:
            # if cur.val == pre.val:
            #     cur = cur.next
            #     pre = pre.next
            #     continue
            find = head
            while find.next:
                if find.next.val > cur.val:
                    pre.next = cur.next
                    cur.next = find.next
                    find.next = cur
                    cur = pre.next
                    break
                elif find.next == cur:
                    pre = pre.next
                    cur = pre.next
                    break
                find = find.next
        return dummy.next


n = ListNode(4)
n.next = ListNode(3)
n.next.next = ListNode(2)
n.next.next.next = ListNode(1)
s = Solution()
s.insertionSortList(n)
print(n.val)
