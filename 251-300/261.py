# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
#
# Example 1:
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
#


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        m = [[0 for _ in range(n)] for _ in range(n)]
        for i, j in edges:
            m[i][j] = 1
            # m[j][i] = 1
        visited = set()
        visited.add(0)

        def dfs(m, i):
            for j, e in enumerate(m[i]):
                if e == 0:
                    continue
                if j in visited:
                    return False
                visited.add(j)
                if not dfs(m, j):
                    return False
            return True

        if not dfs(m, 0):
            return False
        if len(visited) != n:
            return False
        return True


s = Solution()
print(s.validTree(5,
                  [[0, 1], [0, 2], [0, 3], [1, 4]]))
