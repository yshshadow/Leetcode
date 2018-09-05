#
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
#
# The update(i, val) function modifies nums by updating the element at index i to val.
#
# Example:
#
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
#
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.total_sum = [0] + nums
        for idx in range(1, len(self.total_sum)):
            self.total_sum[idx] += self.total_sum[idx - 1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = self.nums[i] - val
        self.nums[i] = val
        for idx in range(i + 1, len(self.total_sum)):
            self.total_sum[idx] -= diff

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.total_sum[j + 1] - self.total_sum[i]



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)


array = NumArray([-2, 0, 3, -5, 2, -1])
print(array.sumRange(0, 2))
array.update(1, 2)
print(array.sumRange(0, 2))
