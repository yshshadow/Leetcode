# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
#
# You are given a target value to search. If found in the array return true, otherwise return false.
#
# Example 1:
#
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
#
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:
#
# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums or len(nums) == 0:
            return False
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[start] <= nums[mid]:  # from start to mid grow
                if nums[start] <= target < nums[mid]:
                    end = mid
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end - 1]:  # from mid to end grow
                    start = mid + 1
                else:
                    end = mid
        return False


s = Solution()
print(s.search([1,3,1,1], 3))
print(s.search([2, 5, 6, 0, 0, 1, 2], 3))
print(s.search([2, 5, 6, 0, 0, 1, 2], 0))
