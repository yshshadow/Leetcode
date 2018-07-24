# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
import copy


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <= 1:
            return 0
        origin = copy.copy(nums)
        nums.sort()
        l, r = 0, 0
        for idx in range(len(nums)):
            if origin[idx] != nums[idx]:
                l = idx
                break
        for idx in range(len(nums))[::-1]:
            if origin[idx] != nums[idx]:
                r = idx
                break
        return r - l + 1 if r != l else 0


nums = [2, 6, 4, 8, 10, 9, 15]
origin = copy.copy(nums)
nums.sort()
l, r = 0, 0
for idx in range(len(nums)):
    if origin[idx] != nums[idx]:
        l = idx
        break
for idx in range(len(nums))[::-1]:
    if origin[idx] != nums[idx]:
        r = idx
        break
print(r - l + 1)
