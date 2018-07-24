# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
#
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums.sort()
        i = 0
        j = 1
        res = 1
        length = len(nums)
        while j < length:
            if nums[i] == nums[j]:
                j += 1
            # elif nums[i] > nums[j]:
            #     break
            else:
                if i != j - 1:
                    tmp = nums[i + 1]
                    nums[i + 1] = nums[j]
                    nums[j] = tmp

                i += 1
                j += 1
                res += 1
        return res


s = Solution()
l = [1, 1, 1, 2, 3, 4, 4, 5, 5]
print(s.removeDuplicates(l))
print(l)
