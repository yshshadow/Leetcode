# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483647 and divisor >= -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        flag = (dividend > 0) == (divisor > 0)  # True if result is positive
        for i in range(32)[::-1]:  # compare from 2^31
            if (a >> i) - b >= 0:  # in case 40/3, 40=3 * 2^3+3 * 2^2 + 3 * 2^0+1, the first i run into if is 3
                a -= b << i
                res += 1 << i  # use binary form to represent the result, in case res=8+4+1
        return res if flag else -res
