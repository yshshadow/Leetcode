# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        dp = [[0] * len(triangle) for _ in range(len(triangle))]
        # initialize
        dp[0][0] = triangle[0][0]
        for idy in range(1, len(triangle)):
            for idx in range(len(triangle[idy])):
                if idx == 0:
                    dp[idy][idx] = dp[idy - 1][idx]
                elif idx == len(triangle[idy]) - 1:
                    dp[idy][idx] = dp[idy - 1][idx - 1]
                else:
                    dp[idy][idx] = min(dp[idy - 1][idx - 1], dp[idy - 1][idx])
                dp[idy][idx] += triangle[idy][idx]

        return min(dp[len(triangle) - 1])


s = Solution()
print(s.minimumTotal([[-1], [-2, -3]]))
