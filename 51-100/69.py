# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return 0
        if x == 1:
            return 1
        start, end = 0, x
        while start < end:
            if end - start == 1:
                return start
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid
                continue
            else:
                start = mid
                continue
        return 0

s=Solution()
print(s.mySqrt(8))
print(s.mySqrt(4))
print(s.mySqrt(3))
print(s.mySqrt(1))
print(s.mySqrt(10))