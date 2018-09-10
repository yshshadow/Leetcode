# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(list(range(1, n + 1)), 0, k, [], res)
        return res

    def dfs(self, nums, index, level, path, res):
        if level == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, level - 1, path + [nums[i]], res)

s=Solution()
print(s.combine(4,3))