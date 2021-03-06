# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#
# Given nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,0,1,1,1,1,2,3,3],
#
# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
#
# It doesn't matter what values are set beyond the returned length.
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
#
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n

        i = 1
        k = i - 1  # 慢于i一步
        j = i + 1  # 快于i一步

        while j <= n - 1:
            if (nums[j] != nums[i]) or (nums[j] == nums[i] and nums[j] != nums[k]):
                # 如果后一步不等于当前步（即不连续相同），或者后一步等于当前步但是后一步不等于当前步的前一步（即连续三个相同值）
                k = i  # k前进一步
                nums[i + 1] = nums[j]
                i += 1  # i前进一步
            j += 1  # j前进一步

        return i + 1


s = Solution()
# nums = [0, 0, 0, 0, 0]
# print(s.removeDuplicates(nums))
# print(nums)
nums = [0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 4, 4]
print(s.removeDuplicates(nums))
print(nums)
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(s.removeDuplicates(nums))
print(nums)
nums = [0, 1, 2, 2, 2, 2, 2, 3, 4, 4, 4]
print(s.removeDuplicates(nums))
print(nums)
