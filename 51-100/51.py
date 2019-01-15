# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.helper([0] * n, n, 0, res)
        return res

    def helper(self, matrix, n, level, res):
        if level == n:
            temp = []
            for num in matrix:
                temp.append('.' * (num - 1) + 'Q' + '.' * (n - num))
            res.append(temp)
        else:
            for i in range(1, n + 1):
                matrix[level] = i
                if self.isvalid(matrix, level):
                    self.helper(matrix, n, level + 1, res)

    def isvalid(self, matrix, level):
        for i in range(level):
            if matrix[i] == matrix[level] or abs(matrix[i] - matrix[level]) == abs(i - level):
                return False
        return True