# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
#
# Example:
#
# Input:
#
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 6
#
# Explanation: Given three people living at (0,0), (0,4), and (2,2):
#              The point (0,2) is an ideal meeting point, as the total travel distance
#              of 2+2+2=6 is minimal. So return 6.

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # best point must at the median
        # cols, rows = [], []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             cols.append(j)
        #             rows.append(i)
        # cols.sort()
        # rows.sort()
        cols = self.getCols(grid)
        rows = self.getRows(grid)
        col = cols[len(cols) // 2]
        row = rows[len(cols) // 2]
        return self.dist(cols, col) + self.dist(rows, row)

    def dist(self, points, target):
        res = 0
        for p in points:
            res += abs(p - target)
        return res

    def getCols(self, grid):
        res = []
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    res.append(i)
        return res

    def getRows(self, grid):
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res.append(i)
        return res
