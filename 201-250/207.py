# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        matrix = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            matrix[pre[0]].append(pre[1])
        visited = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if not self.dfs(matrix, i, visited):
                return False
        return True

    def dfs(self, matrix, i, visited):
        if visited[i] == 1:
            return False
        elif visited[i] == 2:
            return True
        visited[i] += 1
        for j in matrix[i]:
            if not self.dfs(matrix, j, visited):
                return False
        visited[i] += 1
        return True


s = Solution()
print(s.canFinish(3,
                  [[0, 1], [0, 2], [1, 2]]))
