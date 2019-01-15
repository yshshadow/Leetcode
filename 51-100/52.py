# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.
#
# Example:
#
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper([0] * n, n, 0)

    def helper(self, matrix, n, level):
        if level == n:
            return 1
        else:
            res = 0
            for i in range(1, n + 1):
                matrix[level] = i
                if self.isvalid(matrix, level):
                    res += self.helper(matrix, n, level + 1)
            return res

    def isvalid(self, matrix, level):
        for i in range(level):
            if matrix[i] == matrix[level] or abs(matrix[i] - matrix[level]) == abs(i - level):
                return False
        return True
