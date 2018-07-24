# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 1:
#
# Input: [1,3,5,6], 0
# Output: 0

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        if length == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        if length == 2:
            if nums[1] < target:
                return 2
            elif nums[0] >= target:
                return 0
            else:
                return 1
        i = 0
        j = length - 1
        while i <= j:
            distance = j-i+1
            if distance == 1:
                if nums[i] < target:
                    return i + 1
                else:
                    return i
            if distance == 2:
                if nums[j] < target:
                    return j + 1
                elif nums[i] >= target:
                    return i
                else:
                    return j
            else:
                mid = (int)((i + j) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    j = mid
                else:
                    i = mid + 1


s = Solution()
print(s.searchInsert([1, 3, 5], 4))

print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 0))
