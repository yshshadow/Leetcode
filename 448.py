# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 0:
            return []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        return [n + 1 for n in range(len(nums)) if nums[n] > 0]


s = Solution()
print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
