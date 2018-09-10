# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return []
        res = []
        nums.sort()
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, index, sub, res):
        res.append(sub)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.helper(nums, i + 1, sub + [nums[i]], res)

    def subsetsWithDup2(self,nums):
        if not nums or len(nums) == 0:
            return []
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        dup = set()
        for i in range(index, len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
            else:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)


s = Solution()
print(s.subsetsWithDup2([1, 2, 2]))
