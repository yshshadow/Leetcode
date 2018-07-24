# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # length = len(matrix)
        # for x in range(int(length / 2)):
        #     for y in range(x, length - x - 1):
        #         a1, b1 = x, y
        #         a2, b2 = b1, length - a1 - 1
        #         a3, b3 = b2, length - a2 - 1
        #         a4, b4 = b3, length - a3 - 1
        #         temp = matrix[a4][b4]
        #         matrix[a4][b4] = matrix[a3][b3]
        #         matrix[a3][b3] = matrix[a2][b2]
        #         matrix[a2][b2] = matrix[a1][b1]
        #         matrix[a1][b1] = temp
        matrix[::] = zip(*matrix[::-1])

s = Solution()
m = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
s.rotate(m)
print(m)
