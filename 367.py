# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if num <= 1:
            return True
        start, mid, end = 0, int(num / 2), num
        while start < mid < end:
            if pow(mid, 2) < num:
                start = mid
                mid = int((mid + end) / 2)
            elif pow(mid, 2) > num:
                end = mid
                mid = int((start + mid) / 2)
            else:
                return True
        return False


s=Solution()
print(s.isPerfectSquare(1))
print(s.isPerfectSquare(7))
print(s.isPerfectSquare(256))