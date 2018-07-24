# 2. Add Two Numbers   QuestionEditorial Solution  My Submissions
# Total Accepted: 198452
# Total Submissions: 780007
# Difficulty: Medium
# Contributors: Admin
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        self.addTwoNumbersWithExtra(l1, l2, 0, result)
        return result

    def addTwoNumbersWithExtra(self, l1, l2, num, result):

        res = 0
        extra = 0
        if not l1 and not l2:
            if num != 0:
                result.append(num)
        elif l1 and not l2:
            res = l1.val + num
            if res >= 10:
                extra = res / 10
                res -= 10
            result.append(res)
            self.addTwoNumbersWithExtra(l1.next, None, extra, result)
        elif l2 and not l1:
            res = l2.val + num
            if res >= 10:
                extra = res / 10
                res -= 10
            result.append(res)
            self.addTwoNumbersWithExtra(None, l2.next, extra, result)
        else:
            res = l1.val+l2.val+num
            if res >= 10:
                extra = res / 10
                res -= 10
            result.append(res)
            self.addTwoNumbersWithExtra(l1.next, l2.next, extra, result)


