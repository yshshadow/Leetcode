#
# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        cloest, mindiff = 0, 2147483647
        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                res = nums[left] + nums[right] + nums[i]
                diff = abs(target - res)
                if mindiff > diff:
                    cloest = res
                    mindiff = diff
                if res < target:
                    left += 1
                elif res > target:
                    right -= 1
                else:
                    return res
        return cloest


s = Solution()
s.threeSumClosest([-1, 2, 1, -4], 1)
