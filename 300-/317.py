# You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
# Example:
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 7
#
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
#              the point (1,2) is an ideal empty land to build a house, as the total
#              travel distance of 3+3+1=7 is minimal. So return 7.
# Note:
# There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
import collections


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        buildings = set([(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 1])
        obstcale = set([(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 2])
        graph = {(x, y): {} for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 0}

        def bfs():
            queue = collections.deque([(x, y, 0, x, y) for x, y in buildings])
            while queue:
                oi, oj, d, x, y = queue.popleft()
                for rd, cd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i, j = oi + rd, oj + cd
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in obstcale and (
                            i, j) not in buildings and (x, y) not in graph[(i, j)]:
                        graph[(i, j)][(x, y)] = d + 1
                        queue.append((i, j, d + 1, x, y))
            cur = 2147483647
            for space in graph:
                if len(graph[space]) == len(buildings):
                    cur = min(cur, sum(graph[space].values()))
            return cur if cur != 2147483647 else -1

        return bfs()


s = Solution()
print(s.shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
