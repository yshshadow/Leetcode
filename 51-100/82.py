# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

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
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                end = cur.next
                while end.next and end.next.val == cur.val:
                    end = end.next
                next_p = end.next
                pre.next = next_p
                cur = pre.next
            else:
                cur = cur.next
                pre = pre.next
        return dummy.next


head = ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(3)
s=Solution()
s.deleteDuplicates(head)
