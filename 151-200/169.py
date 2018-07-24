# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = nums[0]
        count = 0
        idx = 1
        while idx < len(nums):
            if count == 0:
                candidate = nums[idx]
            count += 1 if candidate == nums[idx] else -1
            idx += 1
        return candidate
