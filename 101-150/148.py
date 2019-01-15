# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        pre, fast, slow = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        h1, h2 = head, slow
        pre.next = None
        s1 = self.sortList(h1)
        s2 = self.sortList(h2)
        return self.merge(s1, s2)

    def merge(self, h1, h2):
        dummy = ListNode(-1)
        head = dummy
        while h1 or h2:
            if not h1:
                head.next = h2
                h2 = h2.next
            elif not h2:
                head.next = h1
                h1 = h1.next
            else:
                if h1.val <= h2.val:
                    head.next = h1
                    h1 = h1.next
                else:
                    head.next = h2
                    h2 = h2.next
            head = head.next
        return dummy.next


head = ListNode(4)
head.next = ListNode(2)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(3)
s = Solution()
s.sortList(head)
