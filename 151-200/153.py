# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
# Input: [3,4,5,1,2]
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        begin, end = 0, len(nums) - 1
        return self.search(nums, begin, end)

    def search(self, nums, begin, end):
        if begin == end:
            return nums[begin]
        mid = (begin + end) // 2
        return min(self.search(nums, begin, mid), self.search(nums, mid + 1, end))


s = Solution()
print(s.findMin([3,5,4,1,2]))
