# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(list(range(1, 10)), k, n, 0, [], res)
        return res

    def helper(self, nums, level, target, index, path, res):
        if level == 0 and target == 0:
            res.append(path)
            return
        if level < 0 or target < 0:
            return
        for i in range(index, len(nums)):
            self.helper(nums, level - 1, target - nums[i], i + 1, path + [nums[i]], res)


s = Solution()
print(s.combinationSum3(3, 9))
