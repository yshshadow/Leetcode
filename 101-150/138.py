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
    # recursive
    # def __init__(self):
    #     self.visited = {}
    #
    # def copyRandomList(self, head):
    #     """
    #     :type head: RandomListNode
    #     :rtype: RandomListNode
    #     """
    #     if not head:
    #         return None
    #     if head in self.visited:
    #         return self.visited[head]
    #     node = RandomListNode(head.label)
    #     self.visited[head] = node
    #     node.next = self.copyRandomList(head.next)
    #     node.random = self.copyRandomList(head.random)
    #     return node

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # iterate
        if not head:
            return None
        visited = {}
        p = head
        while head:
            if head in visited:
                node = visited[head]
            else:
                node = RandomListNode(head.label)
                visited[head] = node
            if head.random:
                if head.random in visited:
                    node.random = visited[head.random]
                else:
                    node.random = RandomListNode(head.random.label)
                    visited[head.random] = node.random
            if head.next:
                if head.next in visited:
                    node.next = visited[head.next]
                else:
                    node.next = RandomListNode(head.next.label)
                    visited[head.next] = node.next
            head = head.next
        return visited[p]
