# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = 0
        for i in range(len(matrix)):
            heights = []
            for j in range(len(matrix[0])):
                cur = 0
                for k in range(i, len(matrix)):
                    if matrix[k][j] == '0':
                        break
                    cur += 1
                heights.append(cur)
            res = max(res, self.largestRectangleArea(heights))
        return res

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # stack
        if not heights:
            return 0
        stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                cur = stack.pop()
                res = max(res, heights[cur] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            cur = stack.pop()
            res = max(res, heights[cur] * (len(heights) - stack[-1] - 1))
        return res


s = Solution()
print(s.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
