# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
#
# Example 1:
#
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:
#
# Input:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:
#
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        fc, fr = False, False  # first col and first row
        lx, ly = len(matrix), len(matrix[0])
        for i in range(lx):
            for j in range(ly):
                if matrix[i][j] == 0:
                    if i == 0:
                        fr = True
                    if j == 0:
                        fc = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, lx):
            for j in range(1, ly):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if fr:
            for j in range(ly):
                matrix[0][j] = 0
        if fc:
            for i in range(lx):
                matrix[i][0] = 0
