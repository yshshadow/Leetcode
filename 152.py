# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp solution
        if not nums or len(nums) == 0:
            return 0
        maximum, minimum, res = nums[0], nums[0], nums[0]
        for idx in range(1,len(nums)):
            p_max, p_min = maximum, minimum
            maximum = max(p_max * nums[idx], max(p_min * nums[idx], nums[idx]))
            minimum = min(p_max * nums[idx], min(p_min * nums[idx], nums[idx]))
            res = max(res, maximum)
        return res


s = Solution()
print(s.maxProduct([-2,3,-4]))
