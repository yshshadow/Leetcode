# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for idx in range(len(grid)):
            for idy in range(len(grid[0])):
                if idx == 0 and idy == 0:
                    continue
                elif idx == 0:
                    dp[idx][idy] = dp[idx][idy - 1]+grid[idx][idy]
                elif idy == 0:
                    dp[idx][idy] = dp[idx - 1][idy]+grid[idx][idy]
                else:
                    dp[idx][idy] = min(dp[idx - 1][idy], dp[idx][idy - 1]) + grid[idx][idy]
        return dp[len(grid)-1][len(grid[0])-1]
