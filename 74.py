# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
#
# Consider the following matrix:
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])
        if width == 0:
            return False
        iy = 0
        for y in range(height):
            if target < matrix[y][0]:
                if y == 0:
                    return False
                else:
                    iy = y - 1
                    break
            iy = height - 1
        for x in matrix[iy]:
            if x == target:
                return True
        return False
