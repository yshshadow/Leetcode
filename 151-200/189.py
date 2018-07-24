# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#
# [show hint]
#
# Hint:
# Could you do it in-place with O(1) extra space?
#
# Related problem: Reverse Words in a String II

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 0:
            return
        if k == 0:
            return
        self.reverseRotate(nums, k)

    def extraSpace(self, nums, k):
        l = len(nums)
        res = nums[l - k::] + nums[:l - k:]
        for idx in range(l):
            nums[idx] = res[idx]

    def reverseRotate(self, nums, k):
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, begin, end):
        while begin < end:
            temp = nums[begin]
            nums[begin] = nums[end]
            nums[end] = temp
            begin += 1
            end -= 1


s = Solution()
nums = [1, 2]
s.rotate(nums, 3)
print(nums)
