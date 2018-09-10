# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        table = {}
        dummy = RandomListNode(-1)
        pre, cur = dummy, head
        while cur:
            node = RandomListNode(cur.label)
            table[cur] = node
            cur = cur.next
            pre.next = node
            pre = pre.next
        pre, cur = dummy.next, head
        while pre and cur:
            pre.random = table[cur]
            pre = pre.next
            cur = cur.next
        return dummy.next
