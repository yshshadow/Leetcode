# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
import collections


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if not wordList or endWord not in wordList:
            return []
        queue = collections.deque()
        queue.append(([], beginWord, 1))
        # pre = collections.defaultdict(list)
        min_step = float('inf')
        # visited = set()
        res = []
        while queue:
            parent, cur, depth = queue.popleft()
            if depth > min_step:
                break
            # if cur in visited:
            #     continue
            # else:
            #     visited.add(cur)

            if cur == endWord:
                min_step = min(min_step, depth)
                res.append(parent + [cur])
            for i in range(len(cur)):
                for j in range(26):
                    word = cur[:i] + chr(ord('a') + j) + cur[i + 1:]
                    if word != cur and word in wordList:
                        queue.append((parent + [cur], word, depth + 1))

        return res


s = Solution()
print(s.findLadders("hit",
                    "cog",
                    ["hot", "dot", "dog", "lot", "log", "cog"]))
