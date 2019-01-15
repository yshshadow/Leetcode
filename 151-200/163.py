# Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return ['{}->{}'.format(lower, upper)]
        nums = [lower - 1] + nums + [upper + 1]
        res = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if nums[i] - nums[i - 1] == 2:
                    res.append(str(nums[i - 1] + 1))
                else:
                    res.append('{}->{}'.format(nums[i - 1] + 1, nums[i] - 1))
        return res
