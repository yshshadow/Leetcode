# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
# Example 2:
#
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
# Note: You may assume that n is not less than 2 and not larger than 58.
#


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        array = [i - 1 for i in range(1, n + 1)]
        array[0] = 1
        for i in range(2, n):
            for j in range(i):
                array[i] = max(array[i], max(array[j], j + 1) * max(array[i - j - 1], i - j))
        return array[-1]


s = Solution()
print(s.integerBreak(10))
