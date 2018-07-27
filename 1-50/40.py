#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        candidates.sort()
        self.combination(candidates, 0, target, res, [])
        return res

    def combination(self, candidates, start, target, res, nums):
        if target < 0:
            return
        if target == 0:
            res.append(nums)
            return
        used = set()
        for i in range(start, len(candidates)):
            if candidates[i] not in used:
                used.add(candidates[i])
            else:
                continue
            self.combination(candidates, i + 1, target - candidates[i], res, nums + [candidates[i]])


s = Solution()
print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
print(s.combinationSum2([2, 5, 2, 1, 2], 5))
print(s.combinationSum2([3], 5))
