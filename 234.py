# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        mid = self.getmid(head)
        head2 = self.reverse(mid)
        while head and head2:
            if head.val != head2.val:
                return False
            else:
                head = head.next
                head2 = head2.next
        return True

    def reverse(self, head):
        pre = None
        while head:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre

    def getmid(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(s.isPalindrome(head))
