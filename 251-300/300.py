# Given an unsorted array of integers, find the length of longest increasing subsequence.
#
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.
#
# Your algorithm should run in O(n2) complexity.
#
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        dp = [1] * len(nums)
        for idx in range(len(nums)):
            v = 0
            for idy in range(idx):
                if nums[idy] < nums[idx]:
                    v = max(v, dp[idy])
            dp[idx] = v + 1
        return max(dp)


s = Solution()
print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
