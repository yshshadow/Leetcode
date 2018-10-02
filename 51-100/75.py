#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # two pass
        # r, w, b = 0, 0, 0
        # for num in nums:
        #     if num == 0:
        #         r += 1
        #     elif num == 1:
        #         w += 1
        #     elif num == 2:
        #         b += 1
        # for i in range(len(nums)):
        #     if r > 0:
        #         nums[i] = 0
        #         r -= 1
        #         continue
        #     if w > 0:
        #         nums[i] = 1
        #         w -= 1
        #         continue
        #     if b > 0:
        #         nums[i] = 2
        #         b -= 1
        #         continue

        # one pass
        start, end = 0, len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == 0:
                nums[i] = nums[start]
                nums[start] = 0
                start += 1
                i = start
            elif nums[i] == 2:
                nums[i] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                i += 1


s = Solution()
nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)
print(nums)
