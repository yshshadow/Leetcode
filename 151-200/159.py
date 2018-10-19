# Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.
#
# Example 1:
#
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# Example 2:
#
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
import collections


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i, j = 0, 0
        K = collections.defaultdict(lambda: 0)
        while i <= j < len(s):
            if s[j] in K:
                K[s[j]] = j
                res = max(res, j - i + 1)
                j += 1
            elif len(K) < 2:
                K[s[j]] = j
                res = max(res, j - i + 1)
                j += 1
            elif len(K) == 2:
                i = min(K.values()) + 1
                res = max(res, j - 1 - i + 1)
                del K[s[i - 1]]
        return res


s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct('ababcc'))
