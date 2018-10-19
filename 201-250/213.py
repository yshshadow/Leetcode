# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.
# Example 2:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums[1] and nums[n] is adjacent, solve problem rob 1 to n-1 and rob 2 to n
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        rob1 = self.helper(nums, 0)
        rob2 = self.helper(nums, 1)
        return max(rob1, rob2)

    def helper(self, nums, start):
        r1, r2 = nums[start], max(nums[start + 1], nums[start])
        for i in range(start + 2, start + len(nums) - 2 + 1):
            r2, r1 = max(r1 + nums[i], r2), r2
        return r2


s = Solution()
print(s.rob([1, 3, 1, 3, 100]))
