# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k:
            return []
        dp = [[0 for _ in range(len(nums))] for _ in range(k)]
        pre = [-1 for _ in range(len(nums))]
        dp[0][k - 1] = sum(nums[:k])
        for i in range(k):
            for j in range(k, len(nums)):
                for m in range(k):
                    if i == 0:
                        pre[j] = pre[j] if dp[i][i - m] > dp[i][j] else i - m
                        dp[i][j] = max(dp[i][i - m], dp[i][j])
                    else:
                        pre[j] = pre[j] if dp[i][i - m] > dp[i][j] else i - m

        if dp[-1][-1] == -1:
            return []
        else:
            i = len(nums) - 1
            res = []
            while pre[i] != -1:
                res.append(pre[i])
                i = pre[i]
        return res[::-1]


s = Solution()
print(s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1],
                               2))
