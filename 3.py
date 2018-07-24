# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
import collections


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = collections.defaultdict(int)
        res, b, l = 0, 0, len(s)
        for e in range(l):
            if s[e] in table:
                b = max(b, table[s[e]])
            res = max(res, e - b + 1)
            table[s[e]] = e + 1
        return res

s=Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))