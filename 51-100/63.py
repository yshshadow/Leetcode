# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[1] * m for _ in range(n)]
        for idx in range(n):
            for idy in range(m):
                if obstacleGrid[idx][idy] == 1:
                    dp[idx][idy] = 0
                elif idx == 0:
                    dp[idx][idy] = dp[idx][idy - 1]
                elif idy == 0:
                    dp[idx][idy] = dp[idx - 1][idy]
                else:
                    dp[idx][idy] = dp[idx - 1][idy] + dp[idx][idy - 1]
        return dp[n - 1][m - 1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0]]))
