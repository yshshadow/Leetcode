# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5;
#              Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Follow up:
# Could you solve it in O(nk) runtime?

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        l, k = len(costs), len(costs[0])
        # O(nkk) time and O(nk) space
        # dp = [[0 for _ in range(k)] for _ in range(l)]
        # dp[0] = costs[0]
        # for i in range(1, l):
        #     for j in range(k):
        #         dp[i][j] = min(dp[i - 1][:j] + dp[i - 1][j + 1:]) + costs[i][j]
        #
        # return min(dp[-1])

        # O(k) space and O(nk) time
        # if the chosen color is the minimum one in last iteration, it must choose the second minimum one
        # if the chosen is other color, choose the minimum one in last iteration
        # so use m1,m2 to store the minimum and second minimum value
        dp = costs[0]
        m1_i, m1 = 0, float('inf')
        for i, num in enumerate(dp):
            if num < m1:
                m1 = num
                m1_i = i
        m2_i, m2 = 0, float('inf')
        for i, num in enumerate(dp):
            if i != m1_i and m1 <= num < m2:
                m2 = num
                m2_i = i
        for i in range(1, l):
            new_dp = [0] * k
            for j in range(k):
                if j == m1_i:
                    new_dp[j] = costs[i][j] + m2
                else:
                    new_dp[j] = costs[i][j] + m1
            dp = new_dp
            m1_i, m1 = 0, float('inf')
            for i, num in enumerate(dp):
                if num < m1:
                    m1 = num
                    m1_i = i
            m2_i, m2 = 0, float('inf')
            for i, num in enumerate(dp):
                if i != m1_i and m1 <= num < m2:
                    m2 = num
                    m2_i = i
        return min(dp)
