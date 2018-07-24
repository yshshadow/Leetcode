# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # if not head.next:
        #     return []
        # n_haed = ListNode(-1)
        # n_haed.next = head
        # f, s = n_haed, n_haed
        # while n > 0:
        #     s = s.next
        #     n -= 1
        # while s.next:
        #     s = s.next
        #     f = f.next
        # f.next = f.next.next
        # return n_haed.next
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

s=Solution()
head = ListNode(1)
head.next=ListNode(2)
print(s.removeNthFromEnd(head,2).val)
