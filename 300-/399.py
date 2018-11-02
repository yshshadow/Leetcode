# Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
#
# According to the example above:
#
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        matrix, kv = self.getMatrix(equations, values)
        res = []
        for query in queries:
            if query[0] not in kv or query[1] not in kv:
                res.append(-1)
            else:
                i, j = kv[query[0]], kv[query[1]]
                res.append(self.dfs(matrix, i, j, set(), 1))
        return res

    def getMatrix(self, equations, values):
        # get matrix and key-idx pairs
        idx = 0
        kv = {}
        for equation in equations:
            if equation[0] not in kv:
                kv[equation[0]] = idx
                idx += 1
            if equation[1] not in kv:
                kv[equation[1]] = idx
                idx += 1
        matrix = [[0 for _ in range(len(kv))] for _ in range(len(kv))]
        for i in range(len(matrix)):
            matrix[i][i] = 1.0
        for i, equation in enumerate(equations):
            matrix[kv[equation[0]]][kv[equation[1]]] = values[i]
            matrix[kv[equation[1]]][kv[equation[0]]] = 1 / values[i]
        return matrix, kv

    def dfs(self, matrix, i, j, visited, res):
        # dfs search the path
        # visited to store visited point, res to store pre result number
        if i in visited:
            return -1
        elif i == j:
            return res
        elif matrix[i][j] != 0:
            return matrix[i][j] * res
        else:
            visited.add(i)
            for idx, num in enumerate(matrix[i]):
                if num:
                    temp = self.dfs(matrix, idx, j, visited, res * num)
                    if temp != -1:
                        return temp
        return -1


s = Solution()
print(
    s.calcEquation([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]],
                   [3.0, 4.0, 5.0, 6.0],
                   [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]))
