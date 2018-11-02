# Given
# a
# matrix
# of
# M
# x
# N
# elements(M
# rows, N
# columns), return all
# elements
# of
# the
# matrix in diagonal
# order as shown in the
# below
# image.
#
# Example:
#
# Input:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
#
# Explanation:
#
# Note:
#
# The
# total
# number
# of
# elements
# of
# the
# given
# matrix
# will
# not exceed
# 10, 000.

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        lx, ly = len(matrix), len(matrix[0])
        res = []
        # add lines into result, reverse res[i] when i is odd
        def update(i, j):
            t = []
            while i >= 0 and j < ly:
                t.append(matrix[i][j])
                i -= 1
                j += 1
            res.append(t)

        for i in range(lx):
            update(i, 0)
        for i in range(1, ly):
            update(lx - 1, i)
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return [x for y in res for x in y]
