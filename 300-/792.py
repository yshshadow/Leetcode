# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# Note:
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
import collections


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(lambda: [])
        res = 0
        for word in words:
            dic[word[0]].append(word)
        for s in S:
            if len(dic[s]) > 0:
                for word in list(dic[s]):
                    if len(word) == 1:
                        res+=1
                    else:
                        dic[word[1]].append(word[1:])
                    dic[s].remove(word)
        return res

s=Solution()
print(s.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"]))
