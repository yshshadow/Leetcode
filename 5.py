# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        matrix = [[0] * len(s) for _ in range(len(s))]
        res = ""
        # initialize
        for idx in range(len(s)):
            matrix[idx][idx] = 1
            res=s[idx]
        for idx in range(len(s) - 1):
            if s[idx] == s[idx + 1]:
                matrix[idx][idx + 1] = 1
                res = s[idx:idx+2]
        # dp solution
        for length in range(3, len(s) + 1):
            for idx in range(len(s) - length + 1):
                end = idx + length - 1
                if s[idx] == s[end] and matrix[idx+1][end-1]:
                    matrix[idx][end] = 1
                    res = s[idx:end + 1]
        return res

s=Solution()
print(s.longestPalindrome("abcda"))