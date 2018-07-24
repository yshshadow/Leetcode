# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        self.generateTriangle(numRows, res, 3)
        return res

    def generateTriangle(self, numRows, res, level):
        if numRows + 1 == level:
            return
        lev = [1]
        upper = res[level - 2]
        for x in range(level - 2):
            lev.append(upper[x] + upper[x + 1])
        lev.append(1)
        res.append(lev)
        self.generateTriangle(numRows, res, level + 1)


s = Solution()
s.generate(5)
