# Remove Element
#
# Given an array and a value, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2, with the first two elements of nums being 2.

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        length = len(nums)
        i = 0
        j = len(nums) - 1
        res = 1

        while i < j:
            while i < length:
                if nums[i] == val:
                    break
                i += 1
            while j >= 0:
                if nums[j] != val:
                    break
                j -= 1
            if i > j:
                break
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        return i


s = Solution()
l = [3, 2, 2, 3]
s.removeElement(l, 3)
