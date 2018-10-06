# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dfs tle
        #     return self.helper(s, p)
        #
        # def helper(self, s, p):
        #     if s == '' and p == '':
        #         return True
        #     elif p != '' and p[0] == '*':
        #         res = False
        #         for i in range(len(s) + 1):
        #             res = res or self.helper(s[i:], p[1:])
        #         return res
        #     elif s == '' or p == '':
        #         return False
        #     elif p[0] == '?' or s[0] == p[0]:
        #         return self.helper(s[1:], p[1:])
        #     else:
        #         return False
        # dp solution
        dp = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]
        dp[0][0] = True  # p and s are empty
        for i in range(1, len(p) + 1):
            dp[i][0] = dp[i - 1][0] and p[i - 1] == '*'  # deal with p start with '*'
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
        # t = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
        # t[0][0] = True
        # for i in range(1, len(p) + 1):
        #     t[i][0] = t[i - 1][0] and p[i - 1] == '*'
        # for i in range(1, len(p) + 1):
        #     for j in range(1, len(s) + 1):
        #         if p[i - 1] != '*':
        #             t[i][j] = (p[i - 1] == s[j - 1] or p[i - 1] == '?') and t[i - 1][j - 1]
        #         else:
        #             t[i][j] = t[i][j - 1] or t[i - 1][j]
        # return t


s = Solution()
print(s.isMatch('acdbe', '*'))
