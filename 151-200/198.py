# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # init
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for idx in range(2, len(nums)):
        #     dp[idx] = max(dp[idx - 2] + nums[idx], dp[idx - 1])
        one, two, res = max(nums[0], nums[1]), nums[0], 0
        for idx in range(2, len(nums)):
            cur = max(two+nums[idx],one)
            res = max(res, cur)
            two = one
            one = cur
        return res

s=Solution()
s.rob([2,1,1,2])