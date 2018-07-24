# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur = self.twoSum(nums, 0 - nums[i], i)
            res += cur
        return res

    def twoSum(self, nums, target, start):
        length = len(nums)
        left, right = start + 1, length - 1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res += [[nums[start], nums[left], nums[right]]]
                while left < length and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1  # in every turn, the index must move one step at least
                while right >= 0 and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return res


s = Solution()
s.threeSum([-1, 0, 1, 2, -1, -4])
