# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
#
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
#
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
import collections


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        res = 0
        i, j = 0, 0
        K = collections.defaultdict(lambda: 0)
        while i <= j < len(s):
            if s[j] in K:
                K[s[j]] = j
                res = max(res, j - i + 1)
                j += 1
            elif len(K) < k:
                K[s[j]] = j
                res = max(res, j - i + 1)
                j += 1
            elif len(K) == k:
                i = min(K.values()) + 1
                res = max(res, j - 1 - i + 1)
                del K[s[i - 1]]
        return res
