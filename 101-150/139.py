# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for d in range(len(s)):
            for i in range(len(s)):
                if i + d >= len(s):
                    break
                dp[i][i + d] = s[i:i + d + 1] in wordDict
                if d != 0:
                    dp[i][i + d] = dp[i][i+d] or any(dp[i][i + k - 1] and dp[i + k][i + d] for k in range(1, d + 1))
        return dp[0][-1]


s = Solution()
print(s.wordBreak(s="leetcode", wordDict=["leet", "code"]))
