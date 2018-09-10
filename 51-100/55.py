# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return False
        # dp
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # for i in range(1, len(nums)):
        #     dp[i] = max(nums[i - 1], dp[i - 1]) - 1
        #     if dp[i] < 0:
        #         return False
        # return True

        # greedy
        reach = 0
        for idx, num in enumerate(nums):
            if idx > reach:
                return False
            if reach >= len(nums) - 1:
                return True
            reach = max(reach, idx + num)
        return False
