# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
#
# Note:
#
# The solution set must not contain duplicate quadruplets.
#
# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            cur = self.threeSum(nums, target - nums[i], i)
            res += cur
        return res

    def threeSum(self, nums, target, i):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            cur = self.twoSum(nums, target - nums[j], i, j)
            res += cur
        return res

    def twoSum(self, nums, target, i, j):
        length = len(nums)
        left, right = j + 1, length - 1
        res = []
        while left < right:
            if nums[left] + nums[right] == target:
                res += [[nums[i], nums[j], nums[left], nums[right]]]
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
