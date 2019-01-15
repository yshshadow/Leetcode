# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
#
# Return 0 if there is no such transformation sequence.
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
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # visited = set()
        # wordSet = set(wordList)
        #
        # queue = [(beginWord, 1)]
        #
        # while len(queue) > 0:
        #     word, count = queue.pop(0)
        #     if word == endWord:
        #         return count
        #     if word in visited:
        #         continue
        #     else:
        #         visited.add(word)  # mark word as visited
        #     for i in range(len(word)):
        #         for j in range(0, 26):  # try all possible one character permutations
        #             char = ord('a') + j
        #             changed_word = word[0:i] + chr(char) + word[i + 1:]
        #             if changed_word in wordSet:  # if permuted word is in word list then add children
        #                 queue.append((changed_word, count + 1))
        # return 0  # if queue is exhausted and code reachers here then its impossible to reach endWord
        if not wordList or endWord not in wordList:
            return 0
        queue = collections.deque()
        queue.append((beginWord, 1))
        visited = set()
        while queue:
            cur, depth = queue.popleft()
            if cur == endWord:
                return depth
            for i in range(len(cur)):
                for j in range(26):
                    word = cur[:i] + chr(ord('a') + j) + cur[i + 1:]
                    if word in wordList and word not in visited:
                        visited.add(word)
                        queue.append((word, depth + 1))
        return 0


s = Solution()
print(s.ladderLength("hit",
                     "cog",
                     ["hot", "dot", "dog", "lot", "log", "cog"]))
