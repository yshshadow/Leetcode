# Design
# your
# implementation
# of
# the
# circular
# double - ended
# queue(deque).
#
# Your
# implementation
# should
# support
# following
# operations:
#
# MyCircularDeque(k): Constructor, set
# the
# size
# of
# the
# deque
# to
# be
# k.
# insertFront(): Adds
# an
# item
# at
# the
# front
# of
# Deque.Return
# true if the
# operation is successful.
# insertLast(): Adds
# an
# item
# at
# the
# rear
# of
# Deque.Return
# true if the
# operation is successful.
# deleteFront(): Deletes
# an
# item
# from the front
#
# of
# Deque.Return
# true if the
# operation is successful.
# deleteLast(): Deletes
# an
# item
# from the rear
#
# of
# Deque.Return
# true if the
# operation is successful.
# getFront(): Gets
# the
# front
# item
# from the Deque.If
# the
# deque is empty,
# return -1.
# getRear(): Gets
# the
# last
# item
# from Deque.If the
#
# deque is empty,
# return -1.
# isEmpty(): Checks
# whether
# Deque is empty or not.
# isFull(): Checks
# whether
# Deque is full or not.
#
# Example:
#
# MyCircularDeque
# circularDeque = new
# MycircularDeque(3); // set
# the
# size
# to
# be
# 3
# circularDeque.insertLast(1); // return true
# circularDeque.insertLast(2); // return true
# circularDeque.insertFront(3); // return true
# circularDeque.insertFront(4); // return false, the
# queue is full
# circularDeque.getRear(); // return 2
# circularDeque.isFull(); // return true
# circularDeque.deleteLast(); // return true
# circularDeque.insertFront(4); // return true
# circularDeque.getFront(); // return 4
#
# Note:
#
# All
# values
# will
# be in the
# range
# of[0, 1000].
# The
# number
# of
# operations
# will
# be in the
# range
# of[1, 1000].
# Please
# do
# not use
# the
# built - in Deque
# library.

class ListNode():
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None


class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = 0
        self.cap = k
        self.head = None
        self.rear = None

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size >= self.cap:
            return False
        node = ListNode(value)
        self.size += 1
        if not self.rear:
            self.head = node
            self.rear = node
            self.rear.next = self.head
            self.head.pre = self.rear
        else:
            node.next = self.head
            node.pre = self.rear
            self.head.pre = node
            self.rear.next = node
            self.head = node
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.size >= self.cap:
            return False
        node = ListNode(value)
        self.size += 1
        if not self.rear:
            self.head = node
            self.rear = node
            self.rear.next = self.head
            self.head.pre = self.rear
        else:
            node.next = self.head
            node.pre = self.rear
            self.head.pre = node
            self.rear.next = node
            self.rear = self.rear.next
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size <= 0:
            return False
        self.size -= 1
        if self.size == 0:
            self.rear = None
            self.head = None
        else:
            self.rear.next = self.head.next
            self.head = self.head.next
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.size <= 0:
            return False
        self.size -= 1
        if self.size == 0:
            self.rear = None
            self.head = None
        else:
            self.rear.pre.next = self.head
            self.rear = self.rear.pre
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.size <= 0:
            return -1
        return self.head.val

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.size <= 0:
            return -1
        return self.rear.val

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.cap



        # Your MyCircularDeque object will be instantiated and called as such:


obj = MyCircularDeque(3)
obj.insertLast(1)
obj.deleteFront()
obj.getFront()
obj.getRear()
# obj.insertLast(2)
# obj.insertFront(3)
# obj.insertFront(4)
# obj.getRear()
# obj.isFull()
# obj.deleteLast()
# obj.insertFront(4)
# obj.getFront()
