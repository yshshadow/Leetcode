# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la, lb = 0, 0
        a, b = headA, headB
        while a:
            a = a.next
            la += 1
        while b:
            b = b.next
            lb += 1
        if a != b:
            return None
        if la > lb:
            while la > lb:
                la -= 1
                headA = headA.next
        elif lb > la:
            while lb > la:
                lb -= 1
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
