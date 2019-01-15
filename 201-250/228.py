# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(nums):
            pre = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] - pre == 1:
                pre += 1
                j += 1
            if j - i > 1:
                res.append('{}->{}'.format(nums[i], nums[j - 1]))
            else:
                res.append(str(nums[i]))
            i = j
        return res
