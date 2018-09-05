# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums or len(nums) == 0:
            return
        self.total_sum = [0 for _ in range(len(nums))]
        self.total_sum[0] = nums[0]
        if len(self.total_sum) == 1:
            return
        for idx in range(1, len(nums)):
            self.total_sum[idx] = self.total_sum[idx - 1] + nums[idx]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.total_sum[j]
        else:
            return self.total_sum[j] - self.total_sum[i - 1]


            # Your NumArray object will be instantiated and called as such:
            # obj = NumArray(nums)
            # param_1 = obj.sumRange(i,j)


array = NumArray([-2, 0, 3, -5, 2, -1])
array.sumRange(0, 2)
