# Given a linked list, determine if it has a cycle in it.
#
# Follow up:
# Can you solve it without using extra space?
# # Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if not head.next:
            return False
        if not head.next.next:
            return False
        step1, step2 = head, head
        while step1.next and step2.next and step2.next.next:
            step1 = step1.next
            step2 = step2.next.next
            if step1 == step2:
                return True
        return False

