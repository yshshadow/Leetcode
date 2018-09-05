# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        start, end = dummy, dummy
        while m > 1:
            start = start.next
            m -= 1
        while n > 1:
            end = end.next
            n -= 1
        nend = end.next
        start.next, end = self.reverseList(start.next, end)
        end.next = nend
        return dummy.next

    def reverseList(self, head, end):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        cur, pre = None, None
        while head != end:
            pre = cur
            cur = head
            head = head.next
            cur.next = pre
        return cur, head
