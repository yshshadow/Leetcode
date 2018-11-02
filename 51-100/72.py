# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for i in range(l2 + 1):
            for j in range(l1 + 1):
                if i > 0 and j > 0:
                    dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1],
                                   self.diff(word2[i - 1], word1[j - 1]) + dp[i - 1][j - 1])
                elif i > 0:
                    dp[i][j] = 1 + dp[i - 1][j]
                elif j > 0:
                    dp[i][j] = 1 + dp[i][j - 1]
        return dp[-1][-1]

    def diff(self, i, j):
        return 0 if i == j else 1


s = Solution()
print(s.minDistance('intention', 'execution'))
