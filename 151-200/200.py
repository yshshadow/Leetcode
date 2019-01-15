# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    self.dfs(grid, visited, i, j)
                    res += 1
        return res

    def dfs(self, grid, visited, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] != 0 or grid[i][j] == '0':
            return
        visited[i][j] = 1
        self.dfs(grid, visited, i - 1, j)
        self.dfs(grid, visited, i + 1, j)
        self.dfs(grid, visited, i, j - 1)
        self.dfs(grid, visited, i, j + 1)


s = Solution()
print(s.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "1"]]))


