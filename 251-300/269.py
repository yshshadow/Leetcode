# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".
# Note:
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

import collections


class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        def getEdge(word1, word2):
            if not word1 or not word2:
                return "", ""
            if word1[0] != word2[0]:
                return word1[0], word2[0]
            return getEdge(word1[1:], word2[1:])

        graph = collections.defaultdict(set)
        in_degree = collections.defaultdict(int)
        for i, word in enumerate(words):
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0
            if i > 0:
                p, c = getEdge(words[i - 1], word)
                if p and c:
                    if c in graph[p]:
                        continue
                    in_degree[c] += 1
                    graph[p].add(c)

        toVisit = [char for char in in_degree if in_degree[char] == 0]
        ans = []
        while toVisit:
            p = toVisit.pop()
            ans.append(p)
            for c in graph[p]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    toVisit.append(c)
        if len(ans) < len(in_degree):
            return ""
        return "".join(ans)


s = Solution()
print(s.alienOrder([
    "wrt",
    "wrf",
    "er",
    "ett",
    "eftt"
]))
