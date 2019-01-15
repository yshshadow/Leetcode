# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
#
# Example:
#
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        m = [[0 for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    m[i][j] = 1
                    if i != 0 and j != 0:
                        m[i][j] += min(m[i - 1][j], m[i - 1][j - 1], m[i][j - 1])
                else:
                    m[i][j] = 0
                res = max(res, m[i][j])
        return res ** 2


s = Solution()
print(s.maximalSquare(
    [["1"]]))
