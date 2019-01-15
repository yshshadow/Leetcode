# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.
#
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]
import collections


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x + 1] += 1
            elif count[x + 1] > 0 and count[x + 2] > 0:
                count[x + 1] -= 1
                count[x + 2] -= 1
                tails[x + 3] += 1
            else:
                return False
            count[x] -= 1
        return True

s=Solution()
s.isPossible([1,2,3,3,4,4,5,5])