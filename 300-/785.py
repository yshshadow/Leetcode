# Given
# an
# undirected
# graph,
# return true if and only if it is bipartite.
#
# Recall
# that
# a
# graph is bipartite if we
# can
# split
# it
# 's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
#
# The
# graph is given in the
# following
# form: graph[i] is a
# list
# of
# indexes
# j
# for which the edge between nodes i and j exists.Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges:
# graph[i]
# does
# not contain
# i, and it
# doesn
# 't contain any element twice.
#
# Example
# 1:
# Input: [[1, 3], [0, 2], [1, 3], [0, 2]]
# Output: true
# Explanation:
# The
# graph
# looks
# like
# this:
# 0 - ---1
# | |
# | |
# 3 - ---2
# We
# can
# divide
# the
# vertices
# into
# two
# groups: {0, 2} and {1, 3}.
# Example
# 2:
# Input: [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
# Output: false
# Explanation:
# The
# graph
# looks
# like
# this:
# 0 - ---1
# |  \ |
# |   \ |
# 3 - ---2
# We
# cannot
# find
# a
# way
# to
# divide
# the
# set
# of
# nodes
# into
# two
# independent
# subsets.
#
# Note:
#
# graph
# will
# have
# length in range[1, 100].
# graph[i]
# will
# contain
# integers in range[0, graph.length - 1].
# graph[i]
# will
# not contain
# i or duplicate
# values.
# The
# graph is undirected:
# if any element j is in graph[i], then i will be in graph[j].
import collections


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        l = len(graph)
        A = [0 for _ in range(l)]
        B = [0 for _ in range(l)]
        V = [0 for _ in range(l)]
        Q = collections.deque()
        Q.append((0, graph[0]))
        A[0] = 1
        V[0] = 1
        while len(Q) > 0:
            idx, ad = Q.popleft()
            if A[idx] == 1 and B[idx] == 0:
                for n in ad:
                    if A[n] == 1:
                        return False
                    else:
                        if B[n] == 0:
                            B[n] = 1
                            V[n] = 1
                            Q.append((n, graph[n]))
            elif A[idx] == 0 and B[idx] == 1:
                for n in ad:
                    if B[n] == 1:
                        return False
                    else:
                        if A[n] == 0:
                            A[n] = 1
                            V[n] = 1
                            Q.append((n, graph[n]))
            if len(Q) == 0:  # find next SCC
                for i in range(l):
                    if V[i] != 1:
                        Q.append((i, graph[i]))
                        V[i] = 1
                        A[i] = 1
                        break
        return True


s = Solution()
print(s.isBipartite(
    [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
     [2, 4, 5, 6, 7, 8]]))
