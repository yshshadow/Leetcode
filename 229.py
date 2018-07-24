# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        candidate1, candidate2, count1, count2 = 0, 0, 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                candidate1 = num
            elif count2 == 0:
                count2 = 1
                candidate2 = num
            else:
                count1 -= 1
                count2 -= 1
        if candidate1 == candidate2:
            return [candidate1]
        else:
            return [n for n in (candidate1, candidate2) if nums.count(n) > (len(nums) / 3)]
