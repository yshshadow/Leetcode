# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        star = head
        stop = head.next
        while stop.next is not None:
            if star.val == stop.val:
                stop = stop.next
            else:
                star.next = stop
                stop = stop.next
                star = star.next
        if star.val == stop.val:
            star.next = stop.next
        elif star.next != stop:
            star.next = stop
        return head
