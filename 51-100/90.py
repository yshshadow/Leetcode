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

s=Solution()
print(s.subsetsWithDup([1,1,2,2,2]))
