# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # dp stack over pre result, oom
        # if not s or not wordDict:
        #     return []
        # dp = [[]]
        # dp[0].append('')
        # for i in range(1, len(s) + 1):
        #     l = []
        #     for j in range(i):
        #         if dp[j] and s[j:i] in wordDict:
        #             for sub in dp[j]:
        #                 l.append(sub + ('' if sub == '' else ' ') + s[j:i])
        #     dp.append(l)
        # return dp[-1]

        # save split position, use dfs to get path
        if not s or not wordDict:
            return []
        dp = [[-1]]
        for i in range(1, len(s) + 1):
            l = []
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    l.append(j)
            dp.append(l)
        res = []

        def search(end, path, res):
            if end == 0:
                res.append(' '.join(path[::-1]))
                return
            for begin in dp[end]:
                search(begin, path + [s[begin:end]], res)

        search(len(s), [], res)
        return res


s = Solution()
s.wordBreak("catsanddog",
            ["cat", "cats", "and", "sand", "dog"])
