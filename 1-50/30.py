# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:
#
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # brute force
        # if not s or not words:
        #     return []
        # l = len(words[0])
        # counter = collections.Counter(words)
        # res = []
        # for i in range(len(s) - (l * len(words)) + 1):
        #     j = i
        #     total = 0
        #     visited = collections.defaultdict(lambda: 0)
        #     while j < len(s):
        #         sub = s[j:j + l]
        #         if sub in counter and visited[sub] < counter[sub]:
        #             visited[sub] += 1
        #             total += 1
        #         else:
        #             break
        #         j += l
        #     if total == len(words):
        #         res.append(i)
        # return res

        if not s or not words or not words[0]:
            return []
        m = len(words[0])
        n = len(words)
        counter = collections.Counter(words)
        res = []
        ### key: use sliding window to gradually increase window
        for starting in range(m):
            sliding = collections.Counter()  ## count the word in the current sliding window
            wordcount = 0  ## count how many word right now
            for i in range(starting, len(s), m):  ## use m as interval
                w = s[i:i + m]
                if w in counter:
                    sliding[w] += 1
                    wordcount += 1
                    ## check whether this word has be repeated counted
                    while sliding[w] > counter[w]:
                        currstarting = i - m * (wordcount - 1)
                        sliding[s[currstarting:currstarting + m]] -= 1
                        wordcount -= 1
                else:
                    sliding.clear()
                    wordcount = 0

                if wordcount == n:
                    res.append(i - m * (wordcount - 1))

        return res


s = Solution()
print(s.findSubstring("wordgoodgoodgoodbestword",
                      ["word", "good", "best", "good"]))
