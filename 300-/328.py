# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# Note:
#
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head  # 0,1 and 2 node, dont do anything
        length = 0
        step = head
        while step:  # get the lenght
            length += 1
            step = step.next
        dummy = tail = ListNode(-1)  # dummy and tail node
        pre, cur = head, head.next
        for i in range(2, length + 1):
            if i % 2 == 0:  # even, move node to tail
                pre.next = cur.next
                cur.next = None
                dummy.next = cur
                dummy = dummy.next
                cur = pre.next
            else:  # odd, dont move
                pre = pre.next
                cur = cur.next
        pre.next = tail.next  # add two parts
        return head


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
s.oddEvenList(head)
