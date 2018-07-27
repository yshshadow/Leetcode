# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        result = ListNode()
        point = result
        while l1 is not None and l2 is not None:
            if l1 is None and l2 is not None:
                point.next = l2
                l2 = l2.next
            elif l1 is not None and l2 is None:
                point.next = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
        return result.next


        # best solution
        # res = dummy = ListNode(0)

        # while l1 and l2:
        #     if l1.val < l2.val:
        #         res.next = l1
        #         l1 = l1.next
        #     else:
        #         res.next = l2
        #         l2 = l2.next
        #     res = res.next

        # res.next = l1 or l2
        # return dummy.next
