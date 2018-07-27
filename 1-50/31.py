# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        pos, val = 0, 0
        if length == 0:
            return []
        i = length - 1
        while i >= 0:
            if i == 0:
                nums.reverse()
                return
            if nums[i] > nums[i - 1]:  # from end to start, pos is the first place ascending change to descending
                pos = i - 1
                val = nums[i - 1]
                break
            i -= 1
        i = pos + 1
        while i <= length:
            if i == length or nums[i] <= val:
                # find the min value bigger than nums[pos] on the right side or swap the last value
                nums[pos] = nums[i - 1]
                nums[i - 1] = val
                self.swap(nums, pos + 1, length - 1)
                break
            i += 1

    def swap(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1


s = Solution()
nums = [1, 5, 1]
s.nextPermutation(nums)
print(nums)
