# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# Example:
#
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
#
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        nHead, pHead, pEnd = dummy.next, dummy.next, dummy.next.next
        pre = dummy
        while pEnd:
            t, v = pEnd, k - 2
            while t.next and v > 0:
                t = t.next
                v -= 1
            if v > 0:
                return dummy.next
            steps = k - 1
            while steps > 0 and pEnd:
                nex = pEnd.next
                pEnd.next = pHead
                nHead.next = nex
                pHead = pEnd
                pEnd = nex
                steps -= 1
            pre.next = pHead
            pre = nHead
            nHead = pEnd
            pHead = pEnd
            if pHead:
                pEnd = pHead.next
        return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s = Solution()
s.reverseKGroup(head, 3)
