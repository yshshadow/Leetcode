# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.
#
# For example, with A = "abcd" and B = "cdabcdab".
#
# Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").
#
# Note:
# The length of A and B will be between 1 and 10000.

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        la, lb = len(A), len(B)
        t = 0
        while la * t < lb:
            t += 1
        S = A * t
        if B in S:
            return t
        if B in S + A:
            return t + 1
        return -1

s=Solution()
s.repeatedStringMatch('abcd','cdabcdab')