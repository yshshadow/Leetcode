# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # O(MN) space dp
        # ls, lt = len(s), len(t)
        # if ls < lt:
        #     return 0
        # dp = [[0 for _ in range(ls + 1)] for _ in range(lt + 1)]
        # dp[0] = [1] * (ls + 1)
        # for i in range(1, lt + 1):
        #     for j in range(1, ls + 1):
        #         if s[j - 1] == t[i - 1]:
        #             dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        #         else:
        #             dp[i][j] = dp[i][j - 1]
        # return dp[-1][-1]

        ls, lt = len(s), len(t)
        if ls < lt:
            return 0
        dp1 = [0] * (ls + 1)
        dp2 = [0] * (ls + 1)
        dp1[0] = 1
        for i in range(1, lt + 1):
            for j in range(1, ls + 1):
                dp2[j] = dp2[j - 1]
                if s[j - 1] == t[i - 1]:
                    dp2[j] += dp1[j - 1]
            dp1, dp2 = dp2, [0] * (ls + 1)
        return dp1[-1]


s = Solution()
s.numDistinct("rabbbit",
              "rabbit")
