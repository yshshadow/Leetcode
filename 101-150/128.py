# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nset = set(nums)
        for num in nset:
            if num - 1 not in nset:
                cur = num
                seq = 1

                while cur + 1 in nset:
                    cur += 1
                    seq += 1
                res = max(res, seq)
        return res
