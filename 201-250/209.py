# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1 if nums[0] >= s else 0
        fast, slow = 0, 0
        subsum, res = nums[0], len(nums) + 1
        while slow <= fast < len(nums):
            if subsum >= s:
                res = min(fast - slow + 1, res)
                subsum -= nums[slow]
                slow += 1
            else:
                fast += 1
                if fast >= len(nums):
                    break
                subsum += nums[fast]
        return res if res <= len(nums) else 0

s=Solution()
print(s.minSubArrayLen(100,[2,3,1,2,4,3]))
