# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, 0, 0, 0
        num = 1
        while top + bottom < n:
            for i in range(left, n - right):
                matrix[top][i] = num
                num += 1
            top += 1
            for i in range(top, n - bottom):
                matrix[i][n - 1 - right] = num
                num += 1
            right += 1
            for i in range(n - 1 - right, left - 1, -1):
                matrix[n - 1 - bottom][i] = num
                num += 1
            bottom += 1
            for i in range(n - 1 - bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix


s = Solution()
print(s.generateMatrix(3))
