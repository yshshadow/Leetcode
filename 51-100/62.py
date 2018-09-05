# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:
#
# Input: m = 7, n = 3
# Output: 28


import math
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # math solution
        # return int(math.factorial(m + n - 2) / (math.factorial(n - 1) * math.factorial(m - 1)))
        # dp solution
        dp = [[1] * m for _ in range(n)]
        for idx in range(n):
            for idy in range(m):
                if idx == 0:
                    dp[idx][idy] = dp[idx][idy - 1]
                elif idy == 0:
                    dp[idx][idy] = dp[idx - 1][idy]
                else:
                    dp[idx][idy] = dp[idx - 1][idy] + dp[idx][idy - 1]
        return dp[n-1][m-1]