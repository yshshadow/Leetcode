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
        p = dummy
        step = m
        while step > 1:
            p = p.next
            step -= 1
        pre = p
        # tail = pre.next
        pre.next, tail, rest = self.reverse(p.next, n - m)
        tail.next = rest
        return dummy.next

    def reverse(self, p, remain):
        if not p:
            return None, None, None
        if remain == 0:
            rest = p.next
            p.next = None
            return p, p, rest
        head, tail, rest = self.reverse(p.next, remain - 1)
        tail.next = p
        return head, p, rest


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.reverseBetween(head, 2, 4)
